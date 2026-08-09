# Phase 7 – DynamoDB Enhancement History

## Overview

In this phase, the Serverless AI CV Enhancer was enhanced to persist resume enhancement history using Amazon DynamoDB.

Previously, every successful enhancement was immediately returned to the client and then discarded. With this implementation, each successful enhancement is stored in DynamoDB and can later be retrieved through a dedicated API endpoint.

This transforms the application from a stateless AI demo into a production-style serverless application with persistent storage.

---

## Objectives

- Create a DynamoDB table for enhancement history
- Store successful resume enhancements
- Generate unique enhancement identifiers
- Retrieve previous enhancements
- Extend Lambda to support multiple API routes
- Follow DynamoDB access-pattern-first design principles

---

# Architecture

## Before Phase 7

```text
Client
   │
   ▼
API Gateway
   │
   ▼
Lambda
   │
   ▼
Amazon Bedrock
   │
   ▼
Response
```

## After Phase 7

```text
                    ┌──────────────┐
                    │ Amazon       │
                    │ Bedrock      │
                    └──────┬───────┘
                           │
                           ▼
Client
   │
   ▼
API Gateway
   │
   ▼
Lambda
   │
   ├──────────────┐
   ▼              ▼
Bedrock      DynamoDB
                 │
                 ▼
       Enhancement History
```

---

# AWS Services Used

| Service | Purpose |
|----------|---------|
| AWS Lambda | Backend application logic |
| Amazon API Gateway | Public HTTPS API |
| Amazon Bedrock | AI resume enhancement |
| Amazon DynamoDB | Enhancement history |
| AWS IAM | Permissions |
| Amazon CloudWatch | Logging |

---

# DynamoDB Table Design

## Table Name

```text
ResumeEnhancementHistory
```

## Primary Key

| Key | Type |
|-----|------|
| userId | Partition Key |
| createdAt | Sort Key |

Example:

```text
USER#demo

2026-08-09T20:30:42.123456+00:00#b35b36fa-5d2e-43d5-a1f2-f7d53c3dcb72
```

This allows enhancement history to be queried efficiently in chronological order.

---

# Item Structure

Example item:

```json
{
  "userId": "USER#demo",
  "createdAt": "2026-08-09T20:30:42.123456+00:00#b35b36fa-5d2e-43d5-a1f2-f7d53c3dcb72",
  "enhancementId": "b35b36fa-5d2e-43d5-a1f2-f7d53c3dcb72",
  "jobDescription": "...",
  "resumeBullets": [
    "...",
    "..."
  ],
  "enhancedBullets": [
    "...",
    "..."
  ],
  "promptVersion": "v1",
  "modelId": "amazon.nova-lite-v1:0"
}
```

---

# Application Changes

## New Service

```text
services/history_service.py
```

Responsibilities:

- Save enhancement history
- Retrieve enhancement history
- Handle DynamoDB exceptions

---

## Lambda Routing

The Lambda function now supports multiple API routes.

### POST /enhance

```text
Request
    │
    ▼
Validate Request
    │
    ▼
Build Prompt
    │
    ▼
Amazon Bedrock
    │
    ▼
Parse Response
    │
    ▼
Generate UUID
    │
    ▼
Save to DynamoDB
    │
    ▼
Return Response
```

### GET /history

```text
Request
    │
    ▼
Query DynamoDB
    │
    ▼
Return Latest Enhancements
    │
    ▼
Return Response
```

---

# Environment Variables

| Variable | Purpose |
|----------|---------|
| BEDROCK_MODEL_ID | Amazon Bedrock inference profile |
| BEDROCK_REGION | AWS Region |
| DYNAMODB_TABLE_NAME | DynamoDB table name |

---

# IAM Permissions

Lambda execution role requires:

```text
bedrock:InvokeModel

dynamodb:PutItem

dynamodb:Query
```

Lambda resource policy allows API Gateway to invoke:

```text
POST /enhance

GET /history
```

---

# API Endpoints

## POST /enhance

Returns:

```json
{
  "enhancementId": "...",
  "message": "Resume enhanced successfully.",
  "enhancedBullets": [
    "...",
    "..."
  ],
  "promptVersion": "v1"
}
```

---

## GET /history

Returns:

```json
{
  "history": [
    {
      "enhancementId": "...",
      "createdAt": "...",
      "enhancedBullets": [
        "...",
        "..."
      ]
    }
  ]
}
```

---

# Testing

| Test | Result |
|------|--------|
| Local Lambda Test | ✅ Passed |
| Amazon Bedrock Integration | ✅ Passed |
| DynamoDB Save | ✅ Passed |
| GET /history | ✅ Passed |
| POST /enhance | ✅ Passed |

---

# Screenshots

```text
screenshots/
└── phase-07/
    ├── phase-07-dynamodb-table-created.png
    ├── phase-07-dynamodb-item.png
    ├── phase-07-post-enhance-success.png
    ├── phase-07-get-history-success.png
    └── phase-07-cloudwatch-history.png
```

---

# Lessons Learned

- DynamoDB should be designed around access patterns.
- Store metadata with every AI response.
- Separate service layers improve maintainability.
- API Gateway requires explicit Lambda invoke permissions for each route.
- UUIDs provide globally unique enhancement identifiers.

---

# Deliverables

- DynamoDB table created
- Enhancement history persisted
- GET /history endpoint implemented
- Multi-route Lambda
- IAM permissions configured
- End-to-end testing completed

---

# Next Phase

**Phase 8 – Static Frontend using Amazon S3**

The next phase introduces a browser-based user interface that communicates with the existing API Gateway endpoints.

---

# References

- AWS Lambda
- Amazon API Gateway
- Amazon Bedrock
- Amazon DynamoDB
- AWS IAM
- Amazon CloudWatch