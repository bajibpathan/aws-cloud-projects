from typing import Any

import boto3
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError

from config import (
    BEDROCK_REGION,
    DYNAMODB_TABLE_NAME
)


class HistoryServiceError(Exception):
    """
    Raised when enhancement history cannot be
    stored or retrieved from DynamoDB.
    """


def create_dynamodb_table():
    """
    Return the configured DynamoDB table resource.
    """

    dynamodb = boto3.resource(
        "dynamodb",
        region_name=BEDROCK_REGION
    )

    return dynamodb.Table(
        DYNAMODB_TABLE_NAME
    )


def save_enhancement(
    item: dict[str, Any]
) -> None:
    """
    Store a completed resume enhancement.
    """

    table = create_dynamodb_table()

    try:
        table.put_item(
            Item=item
        )

    except ClientError as error:
        print(
            "DynamoDB save error:",
            error.response["Error"]["Message"]
        )

        raise HistoryServiceError(
            "Unable to save enhancement history."
        ) from error


def get_enhancement_history(
    user_id: str,
    limit: int = 10
) -> list[dict[str, Any]]:
    """
    Retrieve recent resume enhancements
    for the supplied user.
    """

    table = create_dynamodb_table()

    try:
        response = table.query(
            KeyConditionExpression=Key(
                "userId"
            ).eq(user_id),
            ScanIndexForward=False,
            Limit=limit
        )

    except ClientError as error:
        error_code = error.response[
            "Error"
        ][
            "Code"
        ]

        error_message = error.response[
            "Error"
        ][
            "Message"
        ]

        print(
            f"DynamoDB history error code: "
            f"{error_code}"
        )

        print(
            f"DynamoDB history error message: "
            f"{error_message}"
        )

        raise HistoryServiceError(
            "Unable to retrieve enhancement history."
        ) from error

    return response.get(
        "Items",
        []
    )