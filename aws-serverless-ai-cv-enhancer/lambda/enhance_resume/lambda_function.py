from typing import Any

from prompts.prompt_builder import build_prompt
from prompts.output_parser import parse_enhanced_bullets
from config import PROMPT_VERSION
from response import build_response
from services.bedrock_service import (
    BedrockServiceError,
    enhance_resume
)
from validator import (
    parse_request_body,
    validate_request
)


def lambda_handler(
    event: dict[str, Any],
    context: Any
) -> dict[str, Any]:
    """
    Handle a resume enhancement request.
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

    prompt = build_prompt(
        job_description,
        resume_bullets
    )

    try:
        enhanced_resume = enhance_resume(prompt)
        enhanced_bullets = parse_enhanced_bullets(
            enhanced_resume
        )

    except BedrockServiceError:
        return build_response(
            502,
            {
                "error": (
                    "Unable to enhance resume at this time."
                )
            }
        )

    return build_response(
        200,
        {
            "message": "Resume enhanced successfully.",
            "enhancedBullets": enhanced_bullets,
            "promptVersion": PROMPT_VERSION
        }
    )