import json
from typing import Any


def build_response(
    status_code: int,
    body: dict[str, Any]
) -> dict[str, Any]:
    """
    Build a consistent API Gateway-compatible response.
    """

    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(body)
    }