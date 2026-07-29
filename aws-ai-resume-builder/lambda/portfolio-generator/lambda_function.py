from __future__ import annotations

import json
import logging
import os
from typing import Any
from urllib.parse import unquote_plus

import boto3
from botocore.exceptions import ClientError

from normalizer import normalize_portfolio
from renderer import read_portfolio_css, render_portfolio_html
from validators import validate_portfolio


logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3_client = boto3.client("s3")

WEBSITE_BUCKET = os.environ.get("WEBSITE_BUCKET", "").strip()
CLOUDFRONT_DOMAIN = os.environ.get(
    "CLOUDFRONT_DOMAIN",
    "",
).strip()

EXPECTED_INPUT_PREFIX = os.environ.get(
    "EXPECTED_INPUT_PREFIX",
    "ai-output/",
).strip()


def lambda_handler(
    event: dict[str, Any],
    context: Any,
) -> dict[str, Any]:
    """
    Process S3 ObjectCreated events and generate portfolio websites.
    """
    logger.info(
        "Received event: %s",
        json.dumps(event),
    )

    if not WEBSITE_BUCKET:
        raise ValueError(
            "WEBSITE_BUCKET environment variable is required."
        )

    records = event.get("Records", [])

    if not records:
        raise ValueError(
            "The event does not contain any S3 records."
        )

    results = []

    for record in records:
        result = process_s3_record(record)
        results.append(result)

    response = {
        "statusCode": 200,
        "processedRecords": len(results),
        "results": results,
    }

    logger.info(
        "Portfolio generation completed: %s",
        json.dumps(response),
    )

    return response


def process_s3_record(
    record: dict[str, Any],
) -> dict[str, str]:
    """
    Process one S3 event record.
    """
    event_name = record.get("eventName", "")

    if not event_name.startswith("ObjectCreated:"):
        raise ValueError(
            f"Unsupported S3 event type: {event_name}"
        )

    try:
        source_bucket = record["s3"]["bucket"]["name"]
        encoded_key = record["s3"]["object"]["key"]
    except KeyError as error:
        raise ValueError(
            "Invalid S3 event record."
        ) from error

    source_key = unquote_plus(encoded_key)

    logger.info(
        "Processing source object s3://%s/%s",
        source_bucket,
        source_key,
    )

    validate_source_key(source_key)

    source_document = read_json_from_s3(
        bucket=source_bucket,
        key=source_key,
    )

    portfolio_data = normalize_portfolio(source_document)

    validate_portfolio(portfolio_data)

    portfolio_prefix = build_portfolio_prefix(source_key)

    rendered_html = render_portfolio_html(portfolio_data)
    stylesheet = read_portfolio_css()

    html_key = f"{portfolio_prefix}/index.html"
    css_key = f"{portfolio_prefix}/style.css"

    upload_text_file(
        bucket=WEBSITE_BUCKET,
        key=html_key,
        content=rendered_html,
        content_type="text/html; charset=utf-8",
        cache_control="no-cache",
    )

    upload_text_file(
        bucket=WEBSITE_BUCKET,
        key=css_key,
        content=stylesheet,
        content_type="text/css; charset=utf-8",
        cache_control="public, max-age=3600",
    )

    portfolio_url = build_portfolio_url(html_key)

    logger.info(
        "Generated portfolio: %s",
        portfolio_url,
    )

    return {
        "sourceBucket": source_bucket,
        "sourceKey": source_key,
        "destinationBucket": WEBSITE_BUCKET,
        "htmlKey": html_key,
        "cssKey": css_key,
        "portfolioUrl": portfolio_url,
    }


def validate_source_key(source_key: str) -> None:
    """
    Validate that the object belongs to the expected input location.
    """
    if EXPECTED_INPUT_PREFIX:
        if not source_key.startswith(EXPECTED_INPUT_PREFIX):
            raise ValueError(
                "Unexpected source key prefix: "
                f"{source_key}"
            )

    if not source_key.lower().endswith(".json"):
        raise ValueError(
            f"Unsupported source file type: {source_key}"
        )


def read_json_from_s3(
    bucket: str,
    key: str,
) -> dict[str, Any]:
    """
    Download and parse one JSON object from S3.
    """
    try:
        response = s3_client.get_object(
            Bucket=bucket,
            Key=key,
        )

        body = response["Body"].read()

    except ClientError:
        logger.exception(
            "Unable to read s3://%s/%s",
            bucket,
            key,
        )
        raise

    try:
        document = json.loads(
            body.decode("utf-8")
        )
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise ValueError(
            f"Object is not valid UTF-8 JSON: s3://{bucket}/{key}"
        ) from error

    if not isinstance(document, dict):
        raise ValueError(
            "AI output must contain a JSON object."
        )

    return document


def build_portfolio_prefix(
    source_key: str,
) -> str:
    """
    Convert the AI-output key into a portfolio destination prefix.

    Example:
        ai-output/user-id/resume-name.json

    Becomes:
        portfolios/user-id/resume-name
    """
    relative_key = source_key

    if (
        EXPECTED_INPUT_PREFIX
        and source_key.startswith(EXPECTED_INPUT_PREFIX)
    ):
        relative_key = source_key[
            len(EXPECTED_INPUT_PREFIX):
        ]

    relative_key = relative_key.strip("/")

    if not relative_key:
        raise ValueError(
            "Unable to determine the relative source key."
        )

    without_extension = relative_key.rsplit(
        ".",
        maxsplit=1,
    )[0]

    return f"portfolios/{without_extension}"


def upload_text_file(
    bucket: str,
    key: str,
    content: str,
    content_type: str,
    cache_control: str,
) -> None:
    """
    Upload a UTF-8 text file to S3.
    """
    try:
        s3_client.put_object(
            Bucket=bucket,
            Key=key,
            Body=content.encode("utf-8"),
            ContentType=content_type,
            CacheControl=cache_control,
            ServerSideEncryption="AES256",
        )
    except ClientError:
        logger.exception(
            "Unable to upload s3://%s/%s",
            bucket,
            key,
        )
        raise

    logger.info(
        "Uploaded s3://%s/%s",
        bucket,
        key,
    )


def build_portfolio_url(
    html_key: str,
) -> str:
    """
    Build the CloudFront URL when a domain is configured.

    Otherwise, return the destination S3 URI for troubleshooting.
    """
    if CLOUDFRONT_DOMAIN:
        domain = CLOUDFRONT_DOMAIN.rstrip("/")
        return f"https://{domain}/{html_key}"

    return f"s3://{WEBSITE_BUCKET}/{html_key}"