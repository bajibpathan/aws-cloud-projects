# Enhance Resume Lambda

## Purpose

The `enhance_resume` Lambda function handles resume-enhancement requests for the Serverless AI CV Enhancer application.

In the current phase, the function:

* Receives an API Gateway event
* Reads the JSON request body
* Extracts the target job description
* Extracts the resume bullets
* Returns an API Gateway-compatible response

Amazon Bedrock and DynamoDB integrations will be added in later phases.

---

## Handler

```text
lambda_function.lambda_handler
```

The handler configuration consists of:

```text
lambda_function
```

This is the Python filename:

```text
lambda_function.py
```

And:

```text
lambda_handler
```

This is the function inside that file.

---

## Expected Input

The function expects an Amazon API Gateway HTTP API event.

The business request is stored inside the event's `body` field.

Example request body:

```json
{
  "jobDescription": "We are looking for a Cloud Engineer with experience in AWS, infrastructure automation, observability, incident troubleshooting and production support.",
  "resumeBullets": [
    "Worked on Dynatrace dashboards",
    "Helped application teams troubleshoot production incidents",
    "Used Ansible to deploy and configure Dynatrace OneAgent"
  ]
}
```

---

## API Gateway Event Example

The complete event received by Lambda looks similar to:

```json
{
  "version": "2.0",
  "routeKey": "POST /enhance",
  "rawPath": "/enhance",
  "rawQueryString": "",
  "headers": {
    "content-type": "application/json",
    "host": "example.execute-api.ca-central-1.amazonaws.com"
  },
  "requestContext": {
    "http": {
      "method": "POST",
      "path": "/enhance",
      "protocol": "HTTP/1.1"
    },
    "requestId": "local-test-request-001",
    "stage": "$default"
  },
  "body": "{\"jobDescription\":\"We are looking for a Cloud Engineer with experience in AWS, infrastructure automation, observability, incident troubleshooting and production support.\",\"resumeBullets\":[\"Worked on Dynatrace dashboards\",\"Helped application teams troubleshoot production incidents\",\"Used Ansible to deploy and configure Dynatrace OneAgent\"]}",
  "isBase64Encoded": false
}
```

The `body` value is a JSON string.

The Lambda function converts it into a Python dictionary using:

```python
request_body = json.loads(event["body"])
```

---

## Current Request Flow

```text
API Gateway event
        |
        v
Lambda handler
        |
        v
Read event body
        |
        v
Parse JSON
        |
        v
Extract job description
        |
        v
Extract resume bullets
        |
        v
Return temporary response
```

---

## Current Responsibilities

The function currently performs the following tasks:

* Receives the Lambda `event`
* Reads the request `body`
* Converts the JSON string into a Python dictionary
* Extracts `jobDescription`
* Extracts `resumeBullets`
* Builds a consistent API response
* Returns HTTP status code `200`

---

## Current Response

Example response:

```json
{
  "statusCode": 200,
  "headers": {
    "Content-Type": "application/json"
  },
  "body": "{\"message\":\"Request received successfully\",\"jobDescription\":\"We are looking for a Cloud Engineer with experience in AWS, infrastructure automation, observability, incident troubleshooting and production support.\",\"resumeBullets\":[\"Worked on Dynatrace dashboards\",\"Helped application teams troubleshoot production incidents\",\"Used Ansible to deploy and configure Dynatrace OneAgent\"]}"
}
```

The response `body` is returned as a JSON string because API Gateway expects the body in string format.

---

## Folder Structure

```text
lambda/
└── enhance_resume/
    ├── lambda_function.py
    ├── local_test.py
    └── README.md
```

### File Purpose

| File                 | Purpose                                                           |
| -------------------- | ----------------------------------------------------------------- |
| `lambda_function.py` | Contains the Lambda handler and response builder                  |
| `local_test.py`      | Loads a sample event and invokes the Lambda handler locally       |
| `README.md`          | Documents the function's purpose, input, output and testing steps |

---

## Local Testing

From the project root, run:

```bash
python3 lambda/enhance_resume/local_test.py
```

Expected output:

```text
Resume enhancement request received

Lambda response:
{
  "statusCode": 200,
  "headers": {
    "Content-Type": "application/json"
  },
  "body": "{\"message\": \"Request received successfully\", \"jobDescription\": \"We are looking for a Cloud Engineer with experience in AWS, infrastructure automation, observability, incident troubleshooting and production support.\", \"resumeBullets\": [\"Worked on Dynatrace dashboards\", \"Helped application teams troubleshoot production incidents\", \"Used Ansible to deploy and configure Dynatrace OneAgent\"]}"
}

Decoded response body:
{
  "message": "Request received successfully",
  "jobDescription": "We are looking for a Cloud Engineer with experience in AWS, infrastructure automation, observability, incident troubleshooting and production support.",
  "resumeBullets": [
    "Worked on Dynatrace dashboards",
    "Helped application teams troubleshoot production incidents",
    "Used Ansible to deploy and configure Dynatrace OneAgent"
  ]
}
```

---

## Sample Event

The local test uses:

```text
sample-events/api-gateway-enhance-request.json
```

This file simulates an API Gateway HTTP API payload version `2.0` event.

---

## Dependencies

The current function only uses Python standard-library modules:

```python
import json
from typing import Any
```

No third-party packages are required.

A `requirements.txt` file is not needed in this phase.

---

## Not Yet Implemented

The current version does not yet include:

* Input validation
* Invalid JSON handling
* Missing field handling
* Empty value handling
* Amazon Bedrock integration
* DynamoDB history
* Structured logging
* Request tracing
* API authentication
* API throttling
* Streaming responses

These features will be added gradually in later phases.

---

## Security Notes

The function should not:

* Store AWS credentials in code
* Log complete resumes
* Log full job descriptions
* Accept unlimited input sizes
* Generate unsupported metrics
* Invent user experience

Least-privilege IAM permissions will be added when AWS services are integrated.

---

## Current Status

```text
Phase 2: Basic Lambda Request Handling
```

Completed:

* Lambda handler created
* API Gateway event simulated
* JSON body parsed
* Job description extracted
* Resume bullets extracted
* Temporary API response returned
* Local test completed

---

## Next Phase

```text
Phase 3: Input Validation
```

The next phase will add validation for:

* Missing request body
* Invalid JSON
* Missing job description
* Empty job description
* Missing resume bullets
* Empty resume bullet list
* Invalid resume bullet types
* Empty resume bullet values
* Consistent error responses
