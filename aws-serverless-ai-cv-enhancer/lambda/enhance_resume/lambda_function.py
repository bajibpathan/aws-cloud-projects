from datetime import datetime, timezone
from typing import Any
from uuid import uuid4

from config import (
    BEDROCK_MODEL_ID,
    PROMPT_VERSION
)
from prompts.output_parser import parse_enhanced_bullets
from prompts.prompt_builder import build_prompt
from response import build_response
from services.bedrock_service import (
    BedrockServiceError,
    enhance_resume
)
from services.history_service import (
    HistoryServiceError,
    get_enhancement_history,
    save_enhancement
)
from validator import (
    parse_request_body,
    validate_request
)


DEMO_USER_ID = "USER#demo"


def handle_history_request() -> dict[str, Any]:
    """
    Retrieve recent resume enhancement history
    for the demo user.
    """

    try:
        history = get_enhancement_history(
            DEMO_USER_ID
        )

    except HistoryServiceError:
        return build_response(
            500,
            {
                "error": (
                    "Unable to retrieve "
                    "enhancement history."
                )
            }
        )

    return build_response(
        200,
        {
            "history": history
        }
    )


def handle_enhance_request(
    event: dict[str, Any]
) -> dict[str, Any]:
    """
    Process a resume enhancement request.

    Flow:
    1. Parse request body
    2. Validate input
    3. Build prompt
    4. Invoke Amazon Bedrock
    5. Parse enhanced bullets
    6. Save enhancement to DynamoDB
    7. Return response
    """

    request_body, parse_error = parse_request_body(
        event
    )

    if parse_error:
        return build_response(
            400,
            {
                "error": parse_error
            }
        )

    validation_error = validate_request(
        request_body
    )

    if validation_error:
        return build_response(
            400,
            {
                "error": validation_error
            }
        )

    job_description = request_body[
        "jobDescription"
    ]

    resume_bullets = request_body[
        "resumeBullets"
    ]

    prompt = build_prompt(
        job_description,
        resume_bullets
    )

    try:
        generated_text = enhance_resume(
            prompt
        )

    except BedrockServiceError:
        return build_response(
            502,
            {
                "error": (
                    "Unable to enhance resume "
                    "at this time."
                )
            }
        )

    enhanced_bullets = parse_enhanced_bullets(
        generated_text
    )

    if not enhanced_bullets:
        return build_response(
            502,
            {
                "error": (
                    "Amazon Bedrock returned "
                    "an invalid response."
                )
            }
        )

    enhancement_id = str(
        uuid4()
    )

    timestamp = (
        datetime.now(timezone.utc)
        .isoformat()
    )

    history_item = {
        "userId": DEMO_USER_ID,
        "createdAt": (
            f"{timestamp}#{enhancement_id}"
        ),
        "enhancementId": enhancement_id,
        "jobDescription": job_description,
        "resumeBullets": resume_bullets,
        "enhancedBullets": enhanced_bullets,
        "promptVersion": PROMPT_VERSION,
        "modelId": BEDROCK_MODEL_ID
    }

    try:
        save_enhancement(
            history_item
        )

    except HistoryServiceError:
        return build_response(
            500,
            {
                "error": (
                    "Resume was enhanced, but "
                    "the enhancement history "
                    "could not be saved."
                )
            }
        )

    return build_response(
        200,
        {
            "enhancementId": enhancement_id,
            "message": (
                "Resume enhanced successfully."
            ),
            "enhancedBullets": enhanced_bullets,
            "promptVersion": PROMPT_VERSION
        }
    )


def lambda_handler(
    event: dict[str, Any],
    context: Any
) -> dict[str, Any]:
    """
    Main AWS Lambda entry point.

    Supported routes:

    POST /enhance
        Enhance resume bullets and store the result.

    GET /history
        Retrieve recent enhancement history.
    """

    print(
        "Serverless AI CV Enhancer "
        "request received"
    )

    request_context = event.get(
        "requestContext",
        {}
    )

    http_context = request_context.get(
        "http",
        {}
    )

    http_method = http_context.get(
        "method"
    )

    raw_path = event.get(
        "rawPath"
    )

    if (
        http_method == "POST"
        and raw_path == "/enhance"
    ):
        return handle_enhance_request(
            event
        )

    if (
        http_method == "GET"
        and raw_path == "/history"
    ):
        return handle_history_request()

    return build_response(
        404,
        {
            "error": "Route not found."
        }
    )