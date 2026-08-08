import json
from typing import Any


def parse_request_body(
    event: dict[str, Any]
) -> tuple[dict[str, Any] | None, str | None]:
    """
    Parse the JSON request body from an API Gateway event.

    Returns:
        (request_body, error_message)
    """

    body = event.get("body")

    if body is None or body == "":
        return None, "Request body is required."

    try:
        request_body = json.loads(body)
    except json.JSONDecodeError:
        return None, "Request body contains invalid JSON."

    if not isinstance(request_body, dict):
        return None, "Request body must be a JSON object."

    return request_body, None


def validate_request(
    request_body: dict[str, Any]
) -> str | None:
    """
    Validate the resume-enhancement request.

    Returns:
        None when valid.
        Error message when invalid.
    """

    job_description = request_body.get("jobDescription")

    if job_description is None:
        return "Job description is required."

    if not isinstance(job_description, str):
        return "Job description must be a string."

    if not job_description.strip():
        return "Job description cannot be empty."

    resume_bullets = request_body.get("resumeBullets")

    if resume_bullets is None:
        return "Resume bullets are required."

    if not isinstance(resume_bullets, list):
        return "Resume bullets must be a list."

    if not resume_bullets:
        return "Resume bullets cannot be empty."

    for bullet in resume_bullets:
        if not isinstance(bullet, str):
            return "Each resume bullet must be a string."

        if not bullet.strip():
            return "Resume bullets cannot contain empty values."

    return None