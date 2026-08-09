import os


BEDROCK_MODEL_ID = os.environ.get(
    "BEDROCK_MODEL_ID",
    ""
)

BEDROCK_REGION = os.environ.get(
    "BEDROCK_REGION",
    "ca-central-1"
)

DYNAMODB_TABLE_NAME = os.environ.get(
    "DYNAMODB_TABLE_NAME",
    "ResumeEnhancementHistory"
)

PROMPT_VERSION = "v1"

MAX_OUTPUT_TOKENS = 800
TEMPERATURE = 0.2
