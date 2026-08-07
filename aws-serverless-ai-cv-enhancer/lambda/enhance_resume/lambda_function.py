import json
from typing import Any


def build_response(status_code: int, body: dict[str, Any]) -> dict[str, Any]:
    """
    Build a consistent API Gateway response.
    """

    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(body)
    }


def lambda_handler(event: dict[str, Any], context: Any) -> dict[str, Any]:
    """
    Handle a resume-enhancement request.

    This phase reads the request and returns the supplied values.
    Amazon Bedrock integration will be added later.
    """

    print("Resume enhancement request received")

    request_body_text = event.get("body", "{}")
    request_body = json.loads(request_body_text)

    job_description = request_body.get("jobDescription")
    resume_bullets = request_body.get("resumeBullets")

    return build_response(
        200,
        {
            "message": "Request received successfully",
            "jobDescription": job_description,
            "resumeBullets": resume_bullets
        }
    )