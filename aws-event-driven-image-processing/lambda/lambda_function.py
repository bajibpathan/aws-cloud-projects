import hashlib
import json
import logging
import os
import time
from datetime import datetime, timezone
from typing import Any
from urllib.parse import unquote_plus

import boto3
from botocore.exceptions import ClientError


logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource("dynamodb")

TABLE_NAME = os.environ.get("TABLE_NAME", "ImageMetadata")
table = dynamodb.Table(TABLE_NAME)

SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".png"}


def log_event(
    level: str,
    message: str,
    request_id: str,
    status: str,
    **details: Any
) -> None:
    """
    Write a structured JSON log entry to CloudWatch.
    """
    log_entry = {
        "message": message,
        "requestId": request_id,
        "status": status,
        **details
    }

    log_message = json.dumps(log_entry, default=str)

    if level == "warning":
        logger.warning(log_message)
    elif level == "error":
        logger.error(log_message)
    else:
        logger.info(log_message)


def create_image_id(
    bucket_name: str,
    object_key: str,
    version_id: str
) -> str:
    """
    Create a deterministic identifier for an S3 object version.
    """
    unique_value = f"{bucket_name}:{object_key}:{version_id}"

    return hashlib.sha256(
        unique_value.encode("utf-8")
    ).hexdigest()


def is_supported_image(object_key: str) -> bool:
    """
    Check whether the object has a supported image extension.
    """
    lowercase_key = object_key.lower()

    return any(
        lowercase_key.endswith(extension)
        for extension in SUPPORTED_EXTENSIONS
    )


def build_response(status_code: int, body: dict) -> dict:
    """
    Create a consistent Lambda response.
    """
    return {
        "statusCode": status_code,
        "body": json.dumps(body)
    }


def lambda_handler(event, context):
    """
    Process an Amazon S3 ObjectCreated event.

    The function:
    1. Parses the S3 event.
    2. Validates the uploaded file extension.
    3. Creates a deterministic ImageId.
    4. Stores metadata in DynamoDB.
    5. Prevents duplicate records.
    6. Writes structured status logs to CloudWatch.
    """

    start_time = time.perf_counter()
    request_id = context.aws_request_id

    bucket_name = "Unknown"
    object_key = "Unknown"
    image_id = None

    log_event(
        level="info",
        message="Lambda invocation started",
        request_id=request_id,
        status="RECEIVED"
    )

    try:
        record = event["Records"][0]
        s3_object = record["s3"]["object"]

        bucket_name = record["s3"]["bucket"]["name"]
        object_key = unquote_plus(s3_object["key"])
        file_size = s3_object.get("size", 0)
        etag = s3_object.get("eTag", "NotAvailable")
        version_id = s3_object.get("versionId", etag)

        event_name = record.get("eventName", "Unknown")
        event_time = record.get(
            "eventTime",
            datetime.now(timezone.utc).isoformat()
        )

        log_event(
            level="info",
            message="S3 event parsed successfully",
            request_id=request_id,
            status="RECEIVED",
            bucket=bucket_name,
            objectKey=object_key,
            eventName=event_name
        )

        if not is_supported_image(object_key):
            processing_time_ms = round(
                (time.perf_counter() - start_time) * 1000,
                2
            )

            log_event(
                level="warning",
                message="Unsupported file type rejected",
                request_id=request_id,
                status="REJECTED",
                bucket=bucket_name,
                objectKey=object_key,
                processingTimeMs=processing_time_ms
            )

            return build_response(
                400,
                {
                    "message": "Unsupported file type",
                    "objectKey": object_key,
                    "status": "REJECTED",
                    "supportedExtensions": sorted(
                        SUPPORTED_EXTENSIONS
                    )
                }
            )

        log_event(
            level="info",
            message="Image validation completed",
            request_id=request_id,
            status="VALIDATED",
            bucket=bucket_name,
            objectKey=object_key
        )

        image_id = create_image_id(
            bucket_name,
            object_key,
            version_id
        )

        processed_at = datetime.now(
            timezone.utc
        ).isoformat()

        item = {
            "ImageId": image_id,
            "BucketName": bucket_name,
            "ObjectKey": object_key,
            "FileSize": file_size,
            "UploadTime": event_time,
            "Status": "METADATA_STORED",
            "ETag": etag,
            "VersionId": version_id,
            "EventName": event_name,
            "RequestId": request_id,
            "ProcessedAt": processed_at
        }

        table.put_item(
            Item=item,
            ConditionExpression="attribute_not_exists(ImageId)"
        )

        processing_time_ms = round(
            (time.perf_counter() - start_time) * 1000,
            2
        )

        log_event(
            level="info",
            message="Image metadata stored successfully",
            request_id=request_id,
            status="METADATA_STORED",
            imageId=image_id,
            bucket=bucket_name,
            objectKey=object_key,
            processingTimeMs=processing_time_ms
        )

        return build_response(
            200,
            {
                "message": "Image metadata stored successfully",
                "imageId": image_id,
                "bucket": bucket_name,
                "objectKey": object_key,
                "status": "METADATA_STORED"
            }
        )

    except ClientError as error:
        error_code = error.response.get(
            "Error",
            {}
        ).get(
            "Code",
            "UnknownClientError"
        )

        processing_time_ms = round(
            (time.perf_counter() - start_time) * 1000,
            2
        )

        if error_code == "ConditionalCheckFailedException":
            log_event(
                level="info",
                message="Duplicate event ignored",
                request_id=request_id,
                status="DUPLICATE",
                imageId=image_id,
                bucket=bucket_name,
                objectKey=object_key,
                processingTimeMs=processing_time_ms
            )

            return build_response(
                200,
                {
                    "message": "Duplicate event ignored",
                    "imageId": image_id,
                    "status": "DUPLICATE"
                }
            )

        log_event(
            level="error",
            message="DynamoDB operation failed",
            request_id=request_id,
            status="FAILED",
            imageId=image_id,
            bucket=bucket_name,
            objectKey=object_key,
            errorCode=error_code,
            errorMessage=str(error),
            processingTimeMs=processing_time_ms
        )

        raise

    except (KeyError, IndexError, TypeError) as error:
        processing_time_ms = round(
            (time.perf_counter() - start_time) * 1000,
            2
        )

        log_event(
            level="error",
            message="Invalid S3 event structure",
            request_id=request_id,
            status="FAILED",
            bucket=bucket_name,
            objectKey=object_key,
            errorType=type(error).__name__,
            errorMessage=str(error),
            processingTimeMs=processing_time_ms
        )

        return build_response(
            400,
            {
                "message": "Invalid S3 event",
                "status": "FAILED"
            }
        )

    except Exception as error:
        processing_time_ms = round(
            (time.perf_counter() - start_time) * 1000,
            2
        )

        log_event(
            level="error",
            message="Unexpected processing failure",
            request_id=request_id,
            status="FAILED",
            imageId=image_id,
            bucket=bucket_name,
            objectKey=object_key,
            errorType=type(error).__name__,
            errorMessage=str(error),
            processingTimeMs=processing_time_ms
        )

        raise