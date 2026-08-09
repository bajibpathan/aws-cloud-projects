import json

from lambda_function import lambda_handler


def run_test(name, event, expected_status):

    print("=" * 70)
    print(name)

    response = lambda_handler(event, None)

    actual_status = response["statusCode"]

    result = (
        "PASS"
        if actual_status == expected_status
        else "FAIL"
    )

    print(
        f"[{result}] "
        f"Expected: {expected_status} "
        f"Actual: {actual_status}"
    )

    print(
        json.dumps(
            json.loads(response["body"]),
            indent=2
        )
    )

    print()


def api_event(body):

    return {
        "version": "2.0",
        "routeKey": "POST /enhance",
        "rawPath": "/enhance",
        "requestContext": {
            "http": {
                "method": "POST",
                "path": "/enhance"
            }
        },
        "body": (
            None
            if body is None
            else json.dumps(body)
        ),
        "isBase64Encoded": False
    }


def history_event():

    return {
        "version": "2.0",
        "routeKey": "GET /history",
        "rawPath": "/history",
        "requestContext": {
            "http": {
                "method": "GET",
                "path": "/history"
            }
        }
    }


def unknown_route_event():

    return {
        "version": "2.0",
        "routeKey": "GET /unknown",
        "rawPath": "/unknown",
        "requestContext": {
            "http": {
                "method": "GET",
                "path": "/unknown"
            }
        }
    }


def main():

    print(
        "Running Serverless AI CV Enhancer tests\n"
    )

    valid_request = {
        "jobDescription":
            (
                "Cloud Engineer with AWS, "
                "automation and observability."
            ),

        "resumeBullets": [

            "Created Dynatrace dashboards.",

            "Supported production incidents.",

            "Automated OneAgent deployment."
        ]
    }

    run_test(
        "Valid Request",
        api_event(valid_request),
        200
    )

    run_test(
        "Missing Body",
        api_event(None),
        400
    )

    invalid_json_event = api_event(valid_request)

    invalid_json_event["body"] = "{"

    run_test(
        "Invalid JSON",
        invalid_json_event,
        400
    )

    run_test(
        "Missing Job Description",
        api_event({
            "resumeBullets": [
                "Example"
            ]
        }),
        400
    )

    run_test(
        "Empty Job Description",
        api_event({
            "jobDescription": "",
            "resumeBullets": [
                "Example"
            ]
        }),
        400
    )

    run_test(
        "Resume Bullets Not List",
        api_event({
            "jobDescription": "Cloud Engineer",
            "resumeBullets": "Example"
        }),
        400
    )

    run_test(
        "Empty Resume Bullets",
        api_event({
            "jobDescription": "Cloud Engineer",
            "resumeBullets": []
        }),
        400
    )

    run_test(
        "Oversized Job Description",
        api_event({
            "jobDescription": "A" * 10001,
            "resumeBullets": [
                "Example"
            ]
        }),
        400
    )

    run_test(
        "Too Many Resume Bullets",
        api_event({
            "jobDescription": "Cloud Engineer",
            "resumeBullets": [
                "Bullet"
            ] * 21
        }),
        400
    )

    run_test(
        "Oversized Resume Bullet",
        api_event({
            "jobDescription": "Cloud Engineer",
            "resumeBullets": [
                "A" * 1001
            ]
        }),
        400
    )

    run_test(
        "GET History",
        history_event(),
        200
    )

    run_test(
        "Unknown Route",
        unknown_route_event(),
        404
    )


if __name__ == "__main__":
    main()