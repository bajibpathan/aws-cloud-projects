import boto3
from botocore.exceptions import ClientError

from config import (
    BEDROCK_MODEL_ID,
    BEDROCK_REGION,
    MAX_OUTPUT_TOKENS,
    TEMPERATURE
)


class BedrockServiceError(Exception):
    """
    Raised when Amazon Bedrock cannot complete
    a resume enhancement request.
    """


def create_bedrock_client():
    """
    Create the Amazon Bedrock Runtime client.
    """

    return boto3.client(
        "bedrock-runtime",
        region_name=BEDROCK_REGION
    )


def enhance_resume(prompt: str) -> str:
    """
    Send the completed prompt to Amazon Bedrock
    and return the generated text.
    """

    if not BEDROCK_MODEL_ID:
        raise BedrockServiceError(
            "BEDROCK_MODEL_ID is not configured."
        )

    client = create_bedrock_client()

    try:
        response = client.converse(
            modelId=BEDROCK_MODEL_ID,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "text": prompt
                        }
                    ]
                }
            ],
            inferenceConfig={
                "maxTokens": MAX_OUTPUT_TOKENS,
                "temperature": TEMPERATURE
            }
        )

    except ClientError as error:
        error_code = error.response["Error"]["Code"]
        error_message = error.response["Error"]["Message"]

        print(f"Bedrock error code: {error_code}")
        print(f"Bedrock error message: {error_message}")

        raise BedrockServiceError(
            f"Amazon Bedrock request failed: {error_code}"
        ) from error

    content_blocks = (
        response
        ["output"]
        ["message"]
        ["content"]
    )

    generated_text = "\n".join(
        block["text"]
        for block in content_blocks
        if "text" in block
    ).strip()

    if not generated_text:
        raise BedrockServiceError(
            "Amazon Bedrock returned an empty response."
        )

    return generated_text