import json
from pathlib import Path

from lambda_function import lambda_handler


PROJECT_ROOT = Path(__file__).resolve().parents[2]


TEST_CASES = [
    (
        "Valid Request",
        PROJECT_ROOT / "sample-events" / "api-gateway-enhance-request.json",
        200
    ),
    (
        "Missing Body",
        PROJECT_ROOT / "sample-events" / "invalid" / "missing-body.json",
        400
    ),
    (
        "Invalid JSON",
        PROJECT_ROOT / "sample-events" / "invalid" / "invalid-json.json",
        400
    ),
    (
        "Missing Job Description",
        PROJECT_ROOT / "sample-events" / "invalid" / "missing-job-description.json",
        400
    ),
    (
        "Empty Job Description",
        PROJECT_ROOT / "sample-events" / "invalid" / "empty-job-description.json",
        400
    ),
    (
        "Resume Bullets Not List",
        PROJECT_ROOT / "sample-events" / "invalid" / "resume-bullets-not-list.json",
        400
    ),
    (
        "Empty Resume Bullets",
        PROJECT_ROOT / "sample-events" / "invalid" / "empty-resume-bullets.json",
        400
    )
]

def prepare_enhance_event(event: dict) -> dict:
    """
    Ensure test events contain the API Gateway
    routing information required for POST /enhance.
    """

    event.setdefault(
        "rawPath",
        "/enhance"
    )

    request_context = event.setdefault(
        "requestContext",
        {}
    )

    http_context = request_context.setdefault(
        "http",
        {}
    )

    http_context.setdefault(
        "method",
        "POST"
    )

    return event

def load_event(file_path: Path) -> dict:
    with file_path.open("r", encoding="utf-8") as file:
        return json.load(file)


def run_test(
    test_name: str,
    event_file: Path,
    expected_status: int
) -> None:

    event = load_event(
    event_file
    )

    event = prepare_enhance_event(
        event
    )

    response = lambda_handler(
        event,
        None
    )

    actual_status = response["statusCode"]

    result = (
        "PASS"
        if actual_status == expected_status
        else "FAIL"
    )

    print(f"\n[{result}] {test_name}")
    print(
        f"Expected status: {expected_status}, "
        f"Actual status: {actual_status}"
    )

    print(
        json.dumps(
            json.loads(response["body"]),
            indent=2
        )
    )


def main() -> None:

    print("Running resume enhancer Lambda tests")

    for test_case in TEST_CASES:
        run_test(*test_case)


if __name__ == "__main__":
    main()