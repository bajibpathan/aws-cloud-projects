# Enhance Resume Lambda

## Purpose

The `enhance_resume` Lambda function is the core backend component of the **Serverless AI CV Enhancer** application.

It is responsible for:

- Receiving API Gateway HTTP API requests
- Parsing and validating the request payload
- Building the AI prompt from the approved prompt template
- Invoking Amazon Bedrock using the Converse API
- Returning enhanced resume bullet points
- Returning consistent error responses

Amazon DynamoDB integration and API Gateway deployment will be added in later phases.

---

## Lambda Handler

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

## Request Flow

```text
API Gateway Event
        │
        ▼
Lambda Handler
        │
        ▼
Parse JSON
        │
        ▼
Validate Request
        │
        ▼
Build Prompt
        │
        ▼
Amazon Bedrock
(Converse API)
        │
        ▼
Enhanced Resume
        │
        ▼
API Response
```

---

## Expected Input

```json
{
  "jobDescription": "Cloud Engineer with AWS and observability experience",
  "resumeBullets": [
    "Worked on Dynatrace dashboards",
    "Helped application teams troubleshoot production incidents",
    "Used Ansible to deploy and configure Dynatrace OneAgent"
  ]
}
```

The request body is received through an Amazon API Gateway HTTP API (Payload Format Version 2.0).

---

## Example Response

```json
{
  "statusCode": 200,
  "headers": {
    "Content-Type": "application/json"
  },
  "body": "{\"message\":\"Resume enhanced successfully.\",\"enhancedResume\":\"- Developed and maintained Dynatrace dashboards...\"}"
}
```

---

## Current Responsibilities

- Receive API Gateway requests
- Parse JSON request bodies
- Validate incoming requests
- Build prompts from the approved template
- Invoke Amazon Bedrock using the Converse API
- Return enhanced resume bullets
- Handle Bedrock and validation errors

---

## Project Structure

```text
lambda/
└── enhance_resume/
    ├── config.py
    ├── lambda_function.py
    ├── validator.py
    ├── response.py
    ├── local_test.py
    ├── prompts/
    │   └── prompt_builder.py
    ├── services/
    │   └── bedrock_service.py
    └── README.md
```

---

## File Responsibilities

| File | Purpose |
|------|---------|
| `lambda_function.py` | Orchestrates the request flow |
| `validator.py` | Validates incoming requests |
| `response.py` | Builds API Gateway responses |
| `config.py` | Stores application configuration |
| `prompts/prompt_builder.py` | Loads the prompt template and builds the final prompt |
| `services/bedrock_service.py` | Invokes Amazon Bedrock |
| `local_test.py` | Executes local integration tests |

---

## Local Testing

Run:

```bash
python3 lambda/enhance_resume/local_test.py
```

The test suite validates:

- Valid request
- Missing request body
- Invalid JSON
- Missing job description
- Empty job description
- Invalid resume bullets
- Empty resume bullets

The valid request invokes Amazon Bedrock and returns AI-generated resume bullets.

---

## Dependencies

The application uses:

- boto3
- botocore

AWS Lambda includes these libraries by default.

For local development:

```bash
pip install boto3
```

---

## Security Considerations

- Validate requests before invoking Amazon Bedrock
- Do not store AWS credentials in code
- Use IAM for authentication
- Avoid logging complete resumes or job descriptions
- Prevent the model from inventing achievements or metrics
- Follow the principle of least privilege

---

## Current Status

```text
Phase 5 – Lambda + Amazon Bedrock Integration
```

### Completed

- ✅ Lambda handler
- ✅ Request validation
- ✅ Prompt builder
- ✅ Amazon Bedrock integration
- ✅ Converse API integration
- ✅ Dynamic prompt loading
- ✅ Local end-to-end AI testing
- ✅ Bedrock error handling

---

## Not Yet Implemented

- API Gateway deployment
- Amazon DynamoDB enhancement history
- Static frontend
- CloudWatch structured logging
- AWS X-Ray tracing

---

## Next Phase

```text
Phase 6 – API Gateway Integration
```

Objectives:

- Deploy the Lambda function
- Configure environment variables
- Create an HTTP API
- Connect API Gateway to Lambda
- Test the complete end-to-end workflow
