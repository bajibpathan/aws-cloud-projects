# Serverless AI CV Enhancer

> A production-inspired serverless Generative AI application built on AWS that enhances resume bullet points for a target job description using Amazon Bedrock.

> **Project Inspiration:** This project is inspired by the *Serverless AI CV Enhancer* concept shared by **Lefteris Karageorgiou**. This repository is my own implementation and learning journey, built step by step to understand every architectural decision and AWS service involved.

---

## Project Overview

Users provide:

* A target job description
* Their current resume bullet points

The application validates the request, builds a carefully engineered prompt, sends it to Amazon Bedrock, and returns professionally rewritten resume bullets while preserving the truth of the original experience.

Successful enhancements are stored in Amazon DynamoDB so they can be retrieved later through the enhancement history API.

---

## Learning Objectives

* Build a real serverless GenAI application
* Learn Amazon Bedrock integration
* Practice prompt engineering
* Build production-style AWS Lambda functions
* Implement input validation
* Design a clean serverless architecture
* Build HTTP APIs using Amazon API Gateway
* Store enhancement history in Amazon DynamoDB
* Apply access-pattern-first DynamoDB data modeling
* Apply observability and security best practices

---

# Architecture

## Core Architecture

![Core Architecture](architecture/diagrams/01-core-architecture.png)

## Solution Architecture

![Solution Architecture](architecture/diagrams/04-solution-architecture.png)

## Application Workflow

![Application Workflow](architecture/diagrams/02-application-workflow.png)

## Prompt Engineering Flow

![Prompt Flow](architecture/diagrams/03-prompt-engineering-flow.png)
---

# Current Architecture

```text
Client
   │
   ▼
Amazon API Gateway
   │
   ├──────── POST /enhance
   │
   └──────── GET /history
   │
   ▼
AWS Lambda
   │
   ├──────── Amazon Bedrock
   │             │
   │             ▼
   │      Enhanced Resume Bullets
   │
   └──────── Amazon DynamoDB
                 │
                 ▼
          Enhancement History
```

---

# AWS Services

| Service            | Purpose                                    | Status         |
| ------------------ | ------------------------------------------ | -------------- |
| AWS Lambda         | Backend application logic                  | ✅ Implemented  |
| Amazon API Gateway | HTTP API endpoints                         | ✅ Implemented  |
| Amazon Bedrock     | Resume enhancement using foundation models | ✅ Implemented  |
| Amazon DynamoDB    | Enhancement history                        | ✅ Implemented  |
| Amazon CloudWatch  | Logging and troubleshooting                | 🚧 In Progress |
| AWS IAM            | Secure service access                      | ✅ Implemented  |
| Amazon S3          | Static website hosting                     | ⏳ Planned      |

---

# Application Features

## Implemented

* AI-powered resume enhancement
* Prompt engineering with guardrails
* Honest resume rewriting without invented achievements or metrics
* Request validation
* Amazon Bedrock Converse API integration
* Amazon Bedrock inference profile
* Structured AI response parsing
* Serverless backend architecture
* HTTP API using Amazon API Gateway
* Persistent enhancement history
* DynamoDB access-pattern-first data model
* Unique enhancement IDs
* Enhancement timestamps
* Prompt version tracking
* Model ID tracking
* `POST /enhance` API
* `GET /history` API
* Local Lambda testing
* Production-style error handling

## Planned

* Static web frontend
* Enhancement history UI
* Structured CloudWatch logging
* AWS X-Ray tracing
* Final security hardening
* Final end-to-end testing

---

# API Endpoints

## POST /enhance

Enhances resume bullet points based on the supplied target job description.

### Example Request

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

### Example Response

```json
{
  "enhancementId": "8d9fa874-750a-41dd-aedf-4ef3307fd17a",
  "message": "Resume enhanced successfully.",
  "enhancedBullets": [
    "Developed and maintained Dynatrace dashboards to monitor application performance and system health.",
    "Supported application teams in troubleshooting and resolving production incidents.",
    "Utilized Ansible to automate the deployment and configuration of Dynatrace OneAgent."
  ],
  "promptVersion": "v1"
}
```

---

## GET /history

Returns recent resume enhancements stored in Amazon DynamoDB.

### Example Response

```json
{
  "history": [
    {
      "userId": "USER#demo",
      "createdAt": "2026-08-09T20:30:42.123456+00:00#8d9fa874-750a-41dd-aedf-4ef3307fd17a",
      "enhancementId": "8d9fa874-750a-41dd-aedf-4ef3307fd17a",
      "jobDescription": "Cloud Engineer with AWS and observability experience",
      "resumeBullets": [
        "Worked on Dynatrace dashboards"
      ],
      "enhancedBullets": [
        "Developed and maintained Dynatrace dashboards to monitor application performance and system health."
      ],
      "promptVersion": "v1",
      "modelId": "Amazon Bedrock inference profile"
    }
  ]
}
```

---

# DynamoDB Data Model

## Table

```text
ResumeEnhancementHistory
```

## Primary Key

```text
Partition Key:
userId

Sort Key:
createdAt
```

Current demo user:

```text
USER#demo
```

The `createdAt` value includes both the UTC timestamp and the enhancement ID.

Example:

```text
2026-08-09T20:30:42.123456+00:00#8d9fa874-750a-41dd-aedf-4ef3307fd17a
```

This allows enhancement history to be queried efficiently and returned newest first.

Each item also stores:

* `enhancementId`
* `jobDescription`
* `resumeBullets`
* `enhancedBullets`
* `promptVersion`
* `modelId`

---

# Repository Structure

```text
aws-serverless-ai-cv-enhancer/
├── architecture/
│   ├── decisions/
│   │   ├── ADR-001-serverless-core-architecture.md
│   │   ├── ADR-002-manual-first-before-terraform.md
│   │   ├── ADR-003-local-first-lambda-development-and-validation.md
│   │   ├── ADR-004-amazon-bedrock-integration-strategy.md
│   │   ├── ADR-005-lambda-service-layer-architecture.md
│   │   ├── ADR-006-api-gateway-http-api-strategy.md
│   │   └── ADR-007-dynamodb-history-data-model.md
│   │
│   └── diagrams/
│       ├── core-architecture.png
│       ├── solution-architecture.png
│       ├── application-workflow.png
│       └── prompt-flow.png
│
├── docs/
│   ├── phase-01-project-foundation.md
│   ├── phase-02-basic-lambda-request-handling.md
│   ├── phase-03-input-validation.md
│   ├── phase-04-amazon-bedrock-prompt-testing.md
│   ├── phase-05-lambda-bedrock-integration.md
│   ├── phase-06-api-gateway-integration.md
│   └── phase-07-dynamodb-enhancement-history.md
│
├── frontend/
│
├── lambda/
│   └── enhance_resume/
│       ├── config.py
│       ├── lambda_function.py
│       ├── validator.py
│       ├── response.py
│       ├── local_test.py
│       │
│       ├── prompts/
│       │   ├── prompt_builder.py
│       │   ├── output_parser.py
│       │   └── resume-enhancer-v1.txt
│       │
│       ├── services/
│       │   ├── bedrock_service.py
│       │   └── history_service.py
│       │
│       └── README.md
│
├── policies/
├── prompts/
│   └── prompt-test-cases.md
├── sample-events/
├── screenshots/
└── README.md
```

---

# Local Testing

Run the Lambda test suite from the project root:

```bash
python3 lambda/enhance_resume/local_test.py
```

The test suite validates:

* Valid enhancement request
* Missing request body
* Invalid JSON
* Missing job description
* Empty job description
* Invalid resume bullet structure
* Empty resume bullet list

The valid request performs a real Amazon Bedrock invocation and stores the successful enhancement in DynamoDB.

---

# Current Progress

| Phase                                             | Status  |
| ------------------------------------------------- | ------- |
| Phase 1 – Project Foundation                      | ✅       |
| Phase 2 – Basic Lambda Request Handling           | ✅       |
| Phase 3 – Input Validation                        | ✅       |
| Phase 4 – Amazon Bedrock Prompt Engineering       | ✅       |
| Phase 5 – Lambda + Amazon Bedrock Integration     | ✅       |
| Phase 6 – API Gateway Integration                 | ✅       |
| Phase 7 – DynamoDB Enhancement History            | ✅       |
| Phase 8 – Static Frontend + History               | 🚧 Next |
| Phase 9 – Observability, Security & Final Testing | ⏳       |

---

# Architecture Decision Records

| ADR     | Description                                   |
| ------- | --------------------------------------------- |
| ADR-001 | Serverless Core Architecture                  |
| ADR-002 | Manual-First Development                      |
| ADR-003 | Local-First Lambda Development and Validation |
| ADR-004 | Amazon Bedrock Integration Strategy           |
| ADR-005 | Lambda Service Layer Architecture             |
| ADR-006 | API Gateway HTTP API Strategy                 |
| ADR-007 | DynamoDB History Data Model                   |

---

# Security

* Validate every request before calling Amazon Bedrock
* Apply least-privilege IAM permissions
* Use Lambda execution roles instead of embedded AWS credentials
* Restrict API Gateway Lambda invoke permissions
* Do not log complete resumes or job descriptions
* Never fabricate user achievements, metrics, technologies, or responsibilities
* Use environment variables for runtime configuration
* Avoid using the AWS root user for application development

---

# Cost-Conscious Decisions

* Use AWS Lambda with pay-per-use execution
* Use Amazon API Gateway HTTP API
* Use DynamoDB on-demand capacity
* Use the default API Gateway endpoint
* Host the frontend using Amazon S3
* Avoid Route 53 and custom domains
* Keep Amazon Bedrock testing small
* Remove unused AWS resources after testing

---

# Screenshots

Project implementation screenshots are stored by phase.

```text
screenshots/
├── phase-04/
├── phase-05/
├── phase-06/
└── phase-07/
```

Phase 7 includes:

```text
phase-07-dynamodb-table-created.png
phase-07-dynamodb-item.png
phase-07-post-enhance-success.png
phase-07-get-history-success.png
phase-07-cloudwatch-history.png
```

---

# Documentation

| Folder                           | Purpose                                            |
| -------------------------------- | -------------------------------------------------- |
| `docs/`                          | Step-by-step phase documentation                   |
| `architecture/decisions/`        | Architecture Decision Records                      |
| `architecture/diagrams/`         | Architecture and workflow diagrams                 |
| `prompts/`                       | Prompt test cases                                  |
| `lambda/enhance_resume/prompts/` | Runtime prompt template and prompt-processing code |
| `sample-events/`                 | Local API Gateway test events                      |
| `screenshots/`                   | Implementation evidence by project phase           |

---

# Next Phase

## Phase 8 – Static Frontend + Enhancement History

The next phase will build a browser-based user interface that allows users to:

* Paste a target job description
* Enter existing resume bullets
* Submit the request to `POST /enhance`
* Display enhanced resume bullets
* Copy enhanced bullets
* Retrieve previous enhancements from `GET /history`

The frontend will be hosted using Amazon S3.

---

# References

* Amazon Bedrock documentation
* AWS Lambda documentation
* Amazon API Gateway documentation
* Amazon DynamoDB documentation
* AWS IAM documentation
* Amazon CloudWatch documentation

---

## License

This project is intended for learning, portfolio development, and demonstrating modern AWS serverless and Generative AI architecture.
