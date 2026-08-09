# Technical Overview

## Project Overview

The **Serverless AI CV Enhancer** is a production-inspired serverless Generative AI application built on AWS. It enhances resume bullet points based on a target job description while preserving the accuracy of the candidate's experience.

The application combines modern AWS serverless services with prompt engineering techniques to demonstrate how Generative AI can be integrated into a real-world cloud application.

---

# Solution Architecture

The application follows a fully managed serverless architecture.

<p align="center">
    <img
        src="architecture/diagrams/00-high-level-architecture.png"
        alt="High-Level Architecture"
        width="900">
</p>

The architecture consists of:

- Amazon S3 for static website hosting
- Amazon API Gateway for REST endpoints
- AWS Lambda for application logic
- Amazon Bedrock for AI-powered resume enhancement
- Amazon DynamoDB for storing enhancement history
- Amazon CloudWatch for logging
- AWS X-Ray for distributed tracing

---

# Application Workflow

The application follows the workflow below:

1. User enters a job description and resume bullet points.
2. The frontend sends a request to Amazon API Gateway.
3. API Gateway invokes the Lambda function.
4. Lambda validates the request payload.
5. A structured prompt is generated using the prompt template.
6. Lambda invokes Amazon Bedrock.
7. Amazon Bedrock returns enhanced resume bullet points.
8. Lambda stores the enhancement history in DynamoDB.
9. The enhanced content is returned to the frontend.
10. Users can retrieve previous enhancements using the history endpoint.

---

# AWS Services Used

| Service | Purpose |
|----------|---------|
| AWS Lambda | Backend business logic |
| Amazon API Gateway | HTTP API |
| Amazon Bedrock | Resume enhancement |
| Amazon DynamoDB | Enhancement history |
| Amazon S3 | Static website hosting |
| Amazon CloudWatch | Logging |
| AWS X-Ray | Distributed tracing |
| AWS IAM | Authentication and authorization |

---

# Key Components

## Frontend

The browser-based frontend provides a simple interface for users to:

- Enter a target job description
- Add resume bullet points
- Submit enhancement requests
- View enhanced results
- Review previous enhancement history

---

## API Layer

Amazon API Gateway exposes two endpoints:

| Endpoint | Purpose |
|----------|---------|
| POST /enhance | Enhance resume bullet points |
| GET /history | Retrieve enhancement history |

---

## Lambda Function

The Lambda function is responsible for:

- Request validation
- Prompt generation
- Amazon Bedrock invocation
- Response parsing
- Saving enhancement history
- Returning API responses

The implementation follows a modular structure with dedicated components for validation, response handling, prompt generation, configuration, and service integrations.

---

## Prompt Engineering

Prompt engineering is separated from application logic by using reusable prompt templates.

This provides several benefits:

- Easier prompt updates
- Better maintainability
- Consistent AI responses
- Version tracking

The application currently uses **Prompt Version v1**.

---

## Amazon Bedrock Integration

Amazon Bedrock generates improved resume bullet points based on:

- Target job description
- Existing resume bullets
- Prompt instructions

The application is designed to improve wording while preserving factual accuracy and avoiding fabricated achievements.

---

## DynamoDB

Each successful enhancement stores:

- Enhancement ID
- Timestamp
- Job description
- Original resume bullets
- Enhanced resume bullets
- Prompt version
- Model identifier

This allows users to review previous enhancements through the frontend.

---

# Security

Security considerations include:

- Request validation before AI invocation
- Least-privilege IAM permissions
- No hardcoded AWS credentials
- Configuration through environment variables
- Restricted CORS configuration
- Sensitive data excluded from logs

---

# Observability

The application uses native AWS observability services.

## Amazon CloudWatch

CloudWatch provides:

- Application logs
- Runtime errors
- Execution metrics

---

## AWS X-Ray

AWS X-Ray provides:

- End-to-end request tracing
- Performance insights
- Service dependency visualization

---

# Testing

The project includes testing at multiple levels.

## Local Testing

- Lambda handler
- Request validation
- Amazon Bedrock integration
- DynamoDB integration

## Browser Testing

- Resume enhancement
- Enhancement history
- Error handling
- API connectivity

## AWS Testing

- Lambda execution
- API Gateway integration
- DynamoDB persistence
- CloudWatch logs
- X-Ray traces

---

# Skills Demonstrated

This project demonstrates practical experience with:

## AWS

- AWS Lambda
- Amazon API Gateway
- Amazon Bedrock
- Amazon DynamoDB
- Amazon S3
- AWS IAM
- Amazon CloudWatch
- AWS X-Ray

## Software Engineering

- Serverless architecture
- REST API development
- Prompt engineering
- Input validation
- Error handling
- Modular application design
- Technical documentation

## DevOps

- Git and GitHub
- Feature branch workflow
- Architecture Decision Records (ADRs)
- Local-first development
- Cloud deployment

---

# Lessons Learned

Building this project provided practical experience in designing, implementing, and documenting a serverless Generative AI application on AWS.

Key takeaways include:

- Designing event-driven serverless applications
- Integrating Amazon Bedrock into production-inspired workflows
- Separating prompt engineering from business logic
- Applying least-privilege security principles
- Using CloudWatch and X-Ray for observability
- Building maintainable applications through modular design
- Documenting architectural decisions using ADRs

---

# Documentation Structure

| Document | Purpose |
|----------|---------|
| README.md | Project overview |
| TECHNICAL_OVERVIEW.md | Executive technical summary |
| INTERVIEW_GUIDE.md | Project interview preparation |
| docs/ | Phase-by-phase implementation |
| architecture/decisions/ | Architecture Decision Records |
| lambda/enhance_resume/README.md | Lambda implementation details |

---

# Conclusion

The Serverless AI CV Enhancer demonstrates how AWS serverless services and Generative AI can be combined to build a practical cloud-native application.

Although developed as a learning project, it follows production-inspired design principles, including modular architecture, reusable prompt engineering, structured observability, security best practices, and comprehensive documentation.