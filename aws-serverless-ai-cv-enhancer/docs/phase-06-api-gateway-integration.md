# Phase 6 – API Gateway Integration

## Overview

In this phase, the Serverless AI CV Enhancer was deployed to AWS and exposed through an Amazon API Gateway HTTP API.

## Objectives

- Deploy AWS Lambda
- Configure environment variables
- Configure Lambda execution role
- Create an HTTP API
- Integrate API Gateway with Lambda
- Configure CORS
- Validate end-to-end functionality

## Architecture

```text
Client
   │
   ▼
Amazon API Gateway (HTTP API)
   │
   ▼
AWS Lambda
   │
   ▼
Amazon Bedrock
   │
   ▼
JSON Response
```

## AWS Resources

| Service | Purpose |
|---|---|
| AWS Lambda | Backend logic |
| Amazon API Gateway | HTTPS endpoint |
| Amazon Bedrock | AI resume enhancement |
| AWS IAM | Execution permissions |
| Amazon CloudWatch | Logging |

## Implementation

### Lambda
- Deployed Lambda function
- Configured handler
- Configured environment variables
- Increased timeout for AI inference

### Environment Variables

| Variable | Purpose |
|---|---|
| BEDROCK_MODEL_ID | Bedrock inference profile |
| BEDROCK_REGION | AWS Region |

### IAM

Required permission:

```text
bedrock:InvokeModel
```

### API Gateway

- HTTP API
- Route: `POST /enhance`
- Lambda proxy integration
- CORS enabled

## Testing

| Test | Result |
|---|---|
| Lambda Console Test | ✅ |
| API Gateway Request | ✅ |
| Valid Request | ✅ HTTP 200 |
| Invalid Request | ✅ HTTP 400 |
| Bedrock Integration | ✅ |

## Lessons Learned

- HTTP API is lightweight and cost-effective.
- Environment variables simplify deployment.
- Validate requests before invoking Bedrock.
- Lambda execution roles require explicit permissions.

## Deliverables

- Lambda deployed
- HTTP API created
- HTTPS endpoint available
- End-to-end testing completed
- CORS configured

## Next Phase

**Phase 7 – DynamoDB Enhancement History**
