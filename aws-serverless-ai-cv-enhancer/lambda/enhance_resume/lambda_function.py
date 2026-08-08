from typing import Any

from response import build_response
from validator import parse_request_body, validate_request


def lambda_handler(
    event: dict[str, Any],
    context: Any
) -> dict[str, Any]:
    """
    Handle a resume-enhancement request.
    """

    print("Resume enhancement request received")

    request_body, parse_error = parse_request_body(event)

    if parse_error:
        return build_response(
            400,
            {
                "error": parse_error
            }
        )

    validation_error = validate_request(request_body)

    if validation_error:
        return build_response(
            400,
            {
                "error": validation_error
            }
        )

    job_description = request_body["jobDescription"]
    resume_bullets = request_body["resumeBullets"]

    return build_response(
        200,
        {
            "message": "Request validated successfully.",
            "jobDescription": job_description,
            "resumeBullets": resume_bullets
        }
    )