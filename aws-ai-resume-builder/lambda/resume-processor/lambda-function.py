import json
import logging
import os
from datetime import datetime, timezone
from pathlib import PurePosixPath
from typing import Any
from urllib.parse import unquote_plus

import boto3
from botocore.exceptions import BotoCoreError, ClientError


logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3_client = boto3.client("s3")
textract_client = boto3.client("textract")

PROCESSED_BUCKET_NAME = os.environ["PROCESSED_BUCKET_NAME"]
OUTPUT_PREFIX = os.environ.get("OUTPUT_PREFIX", "processed").strip("/")
ALLOWED_UPLOAD_PREFIX = os.environ.get(
    "ALLOWED_UPLOAD_PREFIX",
    "uploads/",
)

SUPPORTED_EXTENSIONS = {".pdf", ".png", ".jpg", ".jpeg", ".tif", ".tiff"}


class UnsupportedFileTypeError(ValueError):
    """Raised when an uploaded file cannot be processed by Amazon Textract."""


def lambda_handler(
    event: dict[str, Any],
    context: Any,
) -> dict[str, Any]:
    """
    Process S3 ObjectCreated events.

    For each supported resume:
    1. Read the S3 bucket and object key from the event.
    2. Call Amazon Textract DetectDocumentText.
    3. Extract LINE blocks.
    4. Save the extracted text and metadata as JSON.
    """
    request_id = getattr(context, "aws_request_id", "unknown")

    logger.info(
        json.dumps(
            {
                "message": "Resume processing event received",
                "requestId": request_id,
                "recordCount": len(event.get("Records", [])),
            }
        )
    )

    records = event.get("Records", [])

    if not records:
        raise ValueError("The event does not contain any S3 records.")

    processed_documents: list[dict[str, Any]] = []
    failed_documents: list[dict[str, str]] = []

    for record in records:
        try:
            result = process_s3_record(record, request_id)
            processed_documents.append(result)

        except UnsupportedFileTypeError as error:
            logger.warning(
                json.dumps(
                    {
                        "message": "Unsupported document skipped",
                        "requestId": request_id,
                        "error": str(error),
                    }
                )
            )

            failed_documents.append(
                {
                    "reason": "UNSUPPORTED_FILE_TYPE",
                    "error": str(error),
                }
            )

        except (ClientError, BotoCoreError) as error:
            logger.exception(
                json.dumps(
                    {
                        "message": "AWS service call failed",
                        "requestId": request_id,
                        "error": str(error),
                    }
                )
            )

            failed_documents.append(
                {
                    "reason": "AWS_SERVICE_ERROR",
                    "error": str(error),
                }
            )

        except Exception as error:
            logger.exception(
                json.dumps(
                    {
                        "message": "Unexpected processing failure",
                        "requestId": request_id,
                        "error": str(error),
                    }
                )
            )

            failed_documents.append(
                {
                    "reason": "UNEXPECTED_ERROR",
                    "error": str(error),
                }
            )

    response = {
        "processedCount": len(processed_documents),
        "failedCount": len(failed_documents),
        "processedDocuments": processed_documents,
        "failures": failed_documents,
    }

    logger.info(
        json.dumps(
            {
                "message": "Resume processing event completed",
                "requestId": request_id,
                **response,
            }
        )
    )

    if failed_documents:
        # Raising an exception allows Lambda retry behavior or a future DLQ
        # to capture failed processing attempts.
        raise RuntimeError(
            f"{len(failed_documents)} document(s) failed processing."
        )

    return response


def process_s3_record(
    record: dict[str, Any],
    request_id: str,
) -> dict[str, Any]:
    """Process one S3 event record."""

    event_name = record.get("eventName", "")

    if not event_name.startswith("ObjectCreated:"):
        raise ValueError(f"Unsupported S3 event type: {event_name}")

    source_bucket = record["s3"]["bucket"]["name"]
    encoded_object_key = record["s3"]["object"]["key"]
    source_object_key = unquote_plus(encoded_object_key)

    validate_source_object(source_object_key)

    logger.info(
        json.dumps(
            {
                "message": "Starting document text extraction",
                "requestId": request_id,
                "sourceBucket": source_bucket,
                "sourceObjectKey": source_object_key,
            }
        )
    )

    textract_response = textract_client.detect_document_text(
        Document={
            "S3Object": {
                "Bucket": source_bucket,
                "Name": source_object_key,
            }
        }
    )

    lines = extract_lines(textract_response)
    document_text = "\n".join(line["text"] for line in lines)

    output_key = build_output_key(source_object_key)

    output_document = {
        "schemaVersion": "1.0",
        "source": {
            "bucket": source_bucket,
            "objectKey": source_object_key,
            "eventName": event_name,
            "objectSize": record["s3"]["object"].get("size"),
            "eTag": record["s3"]["object"].get("eTag"),
        },
        "processing": {
            "service": "Amazon Textract",
            "operation": "DetectDocumentText",
            "processedAt": datetime.now(timezone.utc).isoformat(),
            "requestId": request_id,
            "textractRequestId": textract_response.get(
                "ResponseMetadata",
                {},
            ).get("RequestId"),
            "documentPages": textract_response.get("DocumentMetadata", {}).get(
                "Pages",
                0,
            ),
        },
        "statistics": {
            "lineCount": len(lines),
            "characterCount": len(document_text),
            "averageConfidence": calculate_average_confidence(lines),
        },
        "text": document_text,
        "lines": lines,
    }

    s3_client.put_object(
        Bucket=PROCESSED_BUCKET_NAME,
        Key=output_key,
        Body=json.dumps(
            output_document,
            ensure_ascii=False,
            indent=2,
        ).encode("utf-8"),
        ContentType="application/json",
        ServerSideEncryption="AES256",
        Metadata={
            "source-bucket": source_bucket,
            "processing-status": "completed",
        },
    )

    logger.info(
        json.dumps(
            {
                "message": "Extracted document saved successfully",
                "requestId": request_id,
                "sourceObjectKey": source_object_key,
                "destinationBucket": PROCESSED_BUCKET_NAME,
                "destinationObjectKey": output_key,
                "lineCount": len(lines),
                "pageCount": output_document["processing"]["documentPages"],
            }
        )
    )

    return {
        "sourceBucket": source_bucket,
        "sourceObjectKey": source_object_key,
        "destinationBucket": PROCESSED_BUCKET_NAME,
        "destinationObjectKey": output_key,
        "lineCount": len(lines),
        "pageCount": output_document["processing"]["documentPages"],
    }


def validate_source_object(object_key: str) -> None:
    """Validate the uploaded object before sending it to Textract."""

    if not object_key.startswith(ALLOWED_UPLOAD_PREFIX):
        raise ValueError(
            f"Object is outside the allowed prefix: {object_key}"
        )

    file_extension = PurePosixPath(object_key).suffix.lower()

    if file_extension not in SUPPORTED_EXTENSIONS:
        raise UnsupportedFileTypeError(
            f"Amazon Textract does not support '{file_extension}' files: "
            f"{object_key}"
        )


def extract_lines(
    textract_response: dict[str, Any],
) -> list[dict[str, Any]]:
    """Extract LINE blocks from the Amazon Textract response."""

    extracted_lines: list[dict[str, Any]] = []

    for block in textract_response.get("Blocks", []):
        if block.get("BlockType") != "LINE":
            continue

        geometry = block.get("Geometry", {}).get("BoundingBox", {})

        extracted_lines.append(
            {
                "text": block.get("Text", ""),
                "confidence": round(
                    float(block.get("Confidence", 0.0)),
                    2,
                ),
                "page": int(block.get("Page", 1)),
                "boundingBox": {
                    "width": geometry.get("Width"),
                    "height": geometry.get("Height"),
                    "left": geometry.get("Left"),
                    "top": geometry.get("Top"),
                },
            }
        )

    return extracted_lines


def calculate_average_confidence(
    lines: list[dict[str, Any]],
) -> float:
    """Calculate the average confidence across extracted lines."""

    if not lines:
        return 0.0

    total_confidence = sum(
        float(line["confidence"])
        for line in lines
    )

    return round(total_confidence / len(lines), 2)


def build_output_key(source_object_key: str) -> str:
    """
    Preserve the upload UUID and replace the filename extension with .json.

    Input:
        uploads/abc-123/alex-morgan-resume.pdf

    Output:
        processed/abc-123/alex-morgan-resume.json
    """
    source_path = PurePosixPath(source_object_key)

    relative_parts = source_path.parts[1:]

    if not relative_parts:
        raise ValueError(
            f"Unable to generate output key for: {source_object_key}"
        )

    output_path = PurePosixPath(*relative_parts).with_suffix(".json")

    return f"{OUTPUT_PREFIX}/{output_path.as_posix()}"