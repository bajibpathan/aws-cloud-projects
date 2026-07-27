import base64
import json
import logging
import os
import re
import uuid
from typing import Any

import boto3
from botocore.exceptions import BotoCoreError, ClientError


logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3_client = boto3.client("s3")

UPLOAD_BUCKET_NAME = os.environ["UPLOAD_BUCKET_NAME"]
UPLOAD_PREFIX = os.environ.get("UPLOAD_PREFIX", "uploads")
PRESIGNED_URL_EXPIRY = int(
    os.environ.get("PRESIGNED_URL_EXPIRY", "300")
)
MAX_FILE_SIZE_BYTES = int(
    os.environ.get("MAX_FILE_SIZE_BYTES", "5242880")
)

ALLOWED_CONTENT_TYPES = {
    "application/pdf": ".pdf",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document": ".docx"
}


def response(
    status_code: int,
    body: dict[str, Any]
) -> dict[str, Any]:
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(body)
    }


def parse_request_body(event: dict[str, Any]) -> dict[str, Any]:
    raw_body = event.get("body")

    if not raw_body:
        return {}

    if event.get("isBase64Encoded"):
        raw_body = base64.b64decode(raw_body).decode("utf-8")

    if isinstance(raw_body, str):
        return json.loads(raw_body)

    return raw_body


def sanitize_filename(filename: str) -> str:
    filename = filename.strip()
    filename = re.sub(r"[^A-Za-z0-9._-]", "-", filename)
    return filename[:100]


def lambda_handler(
    event: dict[str, Any],
    context: Any
) -> dict[str, Any]:
    try:
        request_body = parse_request_body(event)

        filename = sanitize_filename(
            request_body.get("filename", "")
        )

        content_type = request_body.get("contentType", "")
        file_size = request_body.get("fileSize")

        if not filename:
            return response(
                400,
                {"message": "filename is required"}
            )

        if content_type not in ALLOWED_CONTENT_TYPES:
            return response(
                400,
                {
                    "message": (
                        "Only PDF and DOCX files are supported"
                    )
                }
            )

        if not filename.lower().endswith(
            ALLOWED_CONTENT_TYPES[content_type]
        ):
            return response(
                400,
                {
                    "message": (
                        "The filename extension does not match "
                        "the supplied content type"
                    )
                }
            )

        if not isinstance(file_size, int) or file_size <= 0:
            return response(
                400,
                {"message": "A valid fileSize is required"}
            )

        if file_size > MAX_FILE_SIZE_BYTES:
            return response(
                400,
                {
                    "message": (
                        f"File exceeds the maximum size of "
                        f"{MAX_FILE_SIZE_BYTES} bytes"
                    )
                }
            )

        upload_id = str(uuid.uuid4())

        object_key = (
            f"{UPLOAD_PREFIX}/"
            f"{upload_id}/"
            f"{filename}"
        )

        upload_url = s3_client.generate_presigned_url(
            ClientMethod="put_object",
            Params={
                "Bucket": UPLOAD_BUCKET_NAME,
                "Key": object_key,
                "ContentType": content_type
            },
            ExpiresIn=PRESIGNED_URL_EXPIRY
        )

        logger.info(
            "Generated upload URL for object key: %s",
            object_key
        )

        return response(
            200,
            {
                "uploadId": upload_id,
                "objectKey": object_key,
                "uploadUrl": upload_url,
                "expiresIn": PRESIGNED_URL_EXPIRY
            }
        )

    except json.JSONDecodeError:
        return response(
            400,
            {"message": "Request body must contain valid JSON"}
        )

    except (ClientError, BotoCoreError):
        logger.exception("Unable to generate presigned URL")

        return response(
            500,
            {"message": "Unable to generate upload URL"}
        )

    except Exception:
        logger.exception("Unexpected error")

        return response(
            500,
            {"message": "Internal server error"}
        )