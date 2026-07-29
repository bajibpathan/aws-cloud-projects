import json
import os
import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

PROJECT_DIR = Path(__file__).resolve().parents[1]

sys.path.insert(0, str(PROJECT_DIR))

os.environ["WEBSITE_BUCKET"] = (
    "ai-resume-builder-websites-dev"
)

os.environ["EXPECTED_INPUT_PREFIX"] = (
    "ai-output/"
)

import lambda_function


def load_sample_document() -> dict:
    sample_file = (
        Path(__file__).parent
        / "sample-ai-output.json"
    )

    with sample_file.open(
        "r",
        encoding="utf-8",
    ) as file:
        return json.load(file)


def build_s3_event() -> dict:
    return {
        "Records": [
            {
                "eventName": "ObjectCreated:Put",
                "s3": {
                    "bucket": {
                        "name": (
                            "ai-resume-builder-ai-output-dev"
                        )
                    },
                    "object": {
                        "key": (
                            "ai-output/"
                            "3ae938af-6c4e-4e35-81ad-"
                            "ae5cac0722c1/"
                            "sample-resume-alex-morgan.json"
                        )
                    },
                },
            }
        ]
    }


def test_build_portfolio_prefix() -> None:
    source_key = (
        "ai-output/"
        "3ae938af-6c4e-4e35-81ad-ae5cac0722c1/"
        "sample-resume-alex-morgan.json"
    )

    result = lambda_function.build_portfolio_prefix(
        source_key
    )

    assert result == (
        "portfolios/"
        "3ae938af-6c4e-4e35-81ad-ae5cac0722c1/"
        "sample-resume-alex-morgan"
    )


def test_lambda_handler_generates_portfolio() -> None:
    sample_document = load_sample_document()

    fake_body = MagicMock()
    fake_body.read.return_value = json.dumps(
        sample_document
    ).encode("utf-8")

    with patch.object(
        lambda_function.s3_client,
        "get_object",
        return_value={"Body": fake_body},
    ) as mock_get_object:
        with patch.object(
            lambda_function.s3_client,
            "put_object",
        ) as mock_put_object:
            response = lambda_function.lambda_handler(
                build_s3_event(),
                None,
            )

    assert response["statusCode"] == 200
    assert response["processedRecords"] == 1

    mock_get_object.assert_called_once()

    assert mock_put_object.call_count == 2

    uploaded_keys = [
        call.kwargs["Key"]
        for call in mock_put_object.call_args_list
    ]

    assert (
        "portfolios/"
        "3ae938af-6c4e-4e35-81ad-ae5cac0722c1/"
        "sample-resume-alex-morgan/index.html"
        in uploaded_keys
    )

    assert (
        "portfolios/"
        "3ae938af-6c4e-4e35-81ad-ae5cac0722c1/"
        "sample-resume-alex-morgan/style.css"
        in uploaded_keys
    )


def test_invalid_file_extension_is_rejected() -> None:
    event = build_s3_event()

    event["Records"][0]["s3"]["object"]["key"] = (
        "ai-output/user-id/resume.pdf"
    )

    try:
        lambda_function.lambda_handler(
            event,
            None,
        )
    except ValueError as error:
        assert "Unsupported source file type" in str(
            error
        )
    else:
        raise AssertionError(
            "Expected ValueError was not raised."
        )