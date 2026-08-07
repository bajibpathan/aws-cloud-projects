import json
from pathlib import Path

from lambda_function import lambda_handler


def load_test_event() -> dict:
    """
    Load the API Gateway sample event from the project sample-events folder.
    """

    project_root = Path(__file__).resolve().parents[2]
    event_file = project_root / "sample-events" / "api-gateway-enhance-request.json"

    with event_file.open("r", encoding="utf-8") as file:
        return json.load(file)


def main() -> None:
    event = load_test_event()

    response = lambda_handler(event, None)

    print("\nLambda response:")
    print(json.dumps(response, indent=2))

    print("\nDecoded response body:")
    print(json.dumps(json.loads(response["body"]), indent=2))


if __name__ == "__main__":
    main()