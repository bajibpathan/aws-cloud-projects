# Serverless AI CV Enhancer

> A production-inspired serverless Generative AI application built on AWS that enhances resume bullet points for a target job description using Amazon Bedrock.

> **Project Inspiration:** This project is inspired by the *Serverless AI CV Enhancer* concept shared by **Lefteris Karageorgiou**. This repository is my own implementation and learning journey, built step by step to understand every architectural decision and AWS service involved.

---

## Project Overview

Users provide:

- A target job description
- Their current resume bullet points

The application validates the request, builds a carefully engineered prompt, sends it to Amazon Bedrock, and returns professionally rewritten resume bullets while preserving the truth of the original experience.

---

## Learning Objectives

- Build a real serverless GenAI application
- Learn Amazon Bedrock integration
- Practice prompt engineering
- Build production-style AWS Lambda functions
- Implement input validation
- Design a clean serverless architecture
- Store enhancement history in DynamoDB
- Apply observability and security best practices

---

# Architecture

## Core Architecture

![Core Architecture](architecture/diagrams/core-architecture.png)

## Solution Architecture

![Solution Architecture](architecture/diagrams/solution-architecture.png)

## Application Workflow

![Application Workflow](architecture/diagrams/application-workflow.png)

## Prompt Engineering Flow

![Prompt Flow](architecture/diagrams/prompt-flow.png)

---

# AWS Services

| Service | Purpose | Status |
|---------|---------|--------|
| AWS Lambda | Application logic | 🚧 In Progress |
| Amazon API Gateway | REST API | ⏳ Planned |
| Amazon Bedrock | Resume enhancement | 🚧 In Progress |
| Amazon DynamoDB | Enhancement history | ⏳ Planned |
| Amazon CloudWatch | Logging & monitoring | ⏳ Planned |
| AWS IAM | Secure access | 🚧 In Progress |
| Amazon S3 | Static website hosting | ⏳ Planned |

---

# Application Features

- AI-powered resume enhancement
- Prompt engineering with guardrails
- Honest resume rewriting (no hallucinated achievements)
- Request validation
- Serverless architecture
- Resume enhancement history
- Static web frontend
- Structured logging
- Production-ready error handling

---

# Repository Structure

```text
aws-serverless-ai-cv-enhancer/
├── architecture/
│   ├── decisions/
│   └── diagrams/
├── docs/
├── frontend/
├── lambda/
│   └── enhance_resume/
├── policies/
├── prompts/
├── sample-events/
├── screenshots/
└── README.md
```

---

# Example Request

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

# Example Response

```json
{
  "enhancedBullets": [
    "Developed Dynatrace dashboards to improve platform visibility and operational monitoring.",
    "Supported application teams in troubleshooting production incidents and identifying root causes.",
    "Automated Dynatrace OneAgent deployment and configuration using Ansible."
  ]
}
```

---

# Current Progress

| Phase | Status |
|------|--------|
| Phase 1 – Project Foundation | ✅ |
| Phase 2 – Basic Lambda Request Handling | ✅ |
| Phase 3 – Input Validation | ✅ |
| Phase 4 – Amazon Bedrock Prompt Engineering | ✅ |
| Phase 5 – Lambda + Amazon Bedrock Integration | 🚧 (Local integration complete) |
| Phase 6 – API Gateway Integration | ⏳ |
| Phase 7 – DynamoDB History | ⏳ |
| Phase 8 – Static Frontend + History | ⏳ |
| Phase 9 – Observability, Security & Final Testing | ⏳ |

> Do not mark Phase 5 as fully complete until the application is deployed to AWS Lambda and verified through API Gateway.


---

# Architecture Decision Records

| ADR | Description |
|-----|-------------|
| ADR-001 | Serverless Core Architecture |
| ADR-002 | Manual First Development |
| ADR-003 | Local-first Lambda Development |
| ADR-004 | Bedrock Model & Converse API |

---

# Security

- Validate every request before calling Amazon Bedrock
- Apply least-privilege IAM permissions
- Do not log sensitive resume content
- Never fabricate user achievements or metrics

---

# Cost-Conscious Decisions

- Use AWS Lambda (pay-per-use)
- Use the default API Gateway endpoint
- Host the frontend on Amazon S3
- Keep Bedrock testing small during development
- Remove AWS resources after testing

---

# Documentation

| Folder | Purpose |
|--------|---------|
| docs/ | Phase documentation |
| architecture/decisions | ADRs |
| prompts/ | Prompt versions and test cases |
| sample-events/ | Local test events |

---

# References

- Amazon Bedrock documentation
- AWS Lambda documentation
- Amazon API Gateway documentation
- Amazon DynamoDB documentation

---

## License

This project is intended for learning, portfolio development, and demonstrating modern AWS serverless and Generative AI architecture.
