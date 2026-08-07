# Phase 2 – Basic Lambda Request Handling

## Overview

This phase introduces the first Python AWS Lambda function for the Serverless AI CV Enhancer.

The Lambda function is developed and tested locally before deploying to AWS.

---

## Objectives

- Understand the Lambda handler
- Understand the `event` and `context` parameters
- Simulate an API Gateway request
- Parse the request body
- Extract the job description
- Extract the resume bullets
- Return an API Gateway compatible response

---

## Request Flow

```text
Local Test Event
        |
        v
Lambda Handler
        |
        v
Read Event Body
        |
        v
Parse JSON
        |
        v
Extract Job Description
        |
        v
Extract Resume Bullets
        |
        v
Return Temporary Response
```

---

## Files Added

```text
lambda/
└── enhance_resume/
    ├── lambda_function.py
    ├── local_test.py
    └── README.md

sample-events/
└── api-gateway-enhance-request.json
```

---

## What Was Implemented

- Basic Lambda handler
- Response builder helper
- Local API Gateway event
- Local test runner
- JSON request parsing
- Temporary success response

---

## What Was Learned

- AWS Lambda receives an `event` object, not just business data.
- API Gateway wraps the HTTP request inside the event.
- The request body must be parsed using `json.loads()`.
- API Gateway expects the response body to be a JSON string.

---

## Current Limitations

The function does not yet:

- Validate input
- Handle invalid JSON
- Call Amazon Bedrock
- Store history in DynamoDB
- Perform structured logging

---

## Local Test

Run from the project root:

```bash
python3 lambda/enhance_resume/local_test.py
```

Expected result:

- Lambda executes successfully.
- Request body is parsed.
- Job description is extracted.
- Resume bullets are extracted.
- Temporary response is returned.

---

## Next Phase

Implement robust input validation for:

- Missing body
- Invalid JSON
- Missing job description
- Missing resume bullets
- Empty values
- Consistent error responses
