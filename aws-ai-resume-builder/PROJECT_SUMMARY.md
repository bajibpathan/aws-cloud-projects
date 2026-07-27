# AWS AI Resume Builder — Project Summary

## Project Overview

The AWS AI Resume Builder is a serverless, event-driven application that transforms an uploaded resume into a professionally designed portfolio website.

Users securely upload a resume through a web interface. The application authenticates the user, stores the document in Amazon S3, extracts its content using Amazon Textract, processes the extracted data with generative AI, and generates a static portfolio website that can be securely delivered through Amazon CloudFront.

The project is being built incrementally to demonstrate practical AWS architecture, serverless development, security, automation, observability, and AI integration.

---

## Business Problem

Creating a professional portfolio website from a resume typically requires:

* Manual content extraction
* Website development knowledge
* Resume restructuring
* HTML and CSS experience
* Hosting and deployment configuration
* Ongoing maintenance

The AWS AI Resume Builder automates this process by converting resume content into structured data and generating a professional portfolio website.

---

## Solution

The application follows this workflow:

```text
User signs in
        ↓
Amazon Cognito
        ↓
Application requests a presigned URL
        ↓
Upload URL Lambda
        ↓
Amazon S3 Presigned URL
        ↓
Resume uploaded directly to Amazon S3
        ↓
S3 ObjectCreated Event
        ↓
Resume Processor Lambda
        ↓
Amazon Textract
        ↓
Structured Resume JSON
        ↓
Amazon Bedrock
        ↓
Portfolio Website Generator
        ↓
Website stored in Amazon S3
        ↓
Amazon CloudFront
```

---

# Project Roadmap

| Phase   | Description                  |     Status    |
| :------ | :--------------------------- | :-----------: |
| Phase 1 | Project Foundation & Storage |   ✅ Complete  |
| Phase 2 | Secure Resume Upload         |   ✅ Complete  |
| Phase 3 | Authentication               |   ✅ Complete  |
| Phase 4 | Resume Processing            |   ✅ Complete  |
| Phase 5 | AI Resume Analysis           |   🚧 Planned  |
| Phase 6 | Portfolio Website Generation | ⬜ Not Started |
| Phase 7 | Production Readiness         | ⬜ Not Started |

---

## Current Implementation

The application currently includes:

* Project foundation and repository structure
* Private Amazon S3 buckets for resume storage
* Secure browser uploads using Amazon S3 presigned URLs
* User authentication with Amazon Cognito
* JWT-protected API Gateway endpoints
* Upload URL generation using AWS Lambda
* Event-driven processing using Amazon S3 Event Notifications
* Resume text extraction using Amazon Textract
* Structured JSON generation
* Amazon CloudWatch logging
* Least-privilege IAM permissions

---

## Core AWS Services

| AWS Service        | Purpose                                   | Status |
| ------------------ | ----------------------------------------- | :----: |
| Amazon S3          | Store uploaded resumes and processed data |    ✅   |
| Amazon API Gateway | Expose secure APIs                        |    ✅   |
| AWS Lambda         | Execute serverless business logic         |    ✅   |
| Amazon Cognito     | Authenticate users                        |    ✅   |
| Amazon Textract    | Extract resume text                       |    ✅   |
| Amazon CloudWatch  | Logging and monitoring                    |    ✅   |
| AWS IAM            | Identity and access management            |    ✅   |
| Amazon Bedrock     | AI-powered resume analysis                |   🚧   |
| Amazon CloudFront  | Deliver generated portfolio websites      |    ⬜   |

---

## Key Architecture Characteristics

### Serverless

The application is built entirely using managed AWS services without requiring continuously running servers.

### Event-Driven

Resume processing begins automatically when a document is uploaded to Amazon S3.

### Secure File Uploads

Amazon S3 presigned URLs allow users to upload files directly to a private S3 bucket without exposing AWS credentials.

### Authentication

Amazon Cognito provides secure user registration, authentication, and JWT-based authorization.

### Separation of Concerns

Each Lambda function performs a single responsibility:

* Upload URL generation
* Resume processing
* AI processing
* Portfolio website generation

### AI-Ready Architecture

Resume data is converted into structured JSON before being processed by Amazon Bedrock, creating a modular workflow that is easy to extend.

### Static Website Delivery

Generated portfolio websites will be stored in Amazon S3 and distributed globally through Amazon CloudFront.

---

## Application Features

### Completed

* User authentication
* Secure resume uploads
* Browser-based uploads using presigned URLs
* PDF validation
* Event-driven processing
* Resume text extraction
* Structured JSON generation
* CloudWatch logging
* Least-privilege IAM implementation
* Private S3 storage

### Planned

* AI-powered resume analysis
* Portfolio website generation
* Static website hosting
* CloudFront distribution
* Infrastructure as Code
* CI/CD pipeline
* Production monitoring
* Security hardening
* Cost optimization

---

## Security Considerations

The project follows AWS security best practices, including:

* Private Amazon S3 buckets
* Block Public Access
* Least-privilege IAM permissions
* Short-lived S3 presigned URLs
* JWT-protected APIs
* Amazon Cognito authentication
* Encryption at rest
* HTTPS communication
* File type and file size validation
* CloudWatch logging

---

## Reliability Considerations

The production-ready architecture will incorporate:

* Event-driven processing
* Lambda retry behavior
* Error handling
* Duplicate event protection
* Dead-letter queue evaluation
* Bedrock response validation
* Idempotent processing
* CloudWatch alarms
* Operational dashboards

---

## Cost Considerations

The application is designed around usage-based AWS services.

Primary cost drivers include:

* Amazon S3 storage
* AWS Lambda invocations
* API Gateway requests
* Amazon Textract document processing
* Amazon Bedrock model inference
* Amazon CloudFront requests
* CloudWatch logs

Lifecycle policies and cleanup automation will be used to minimize storage and operational costs.

---

## Learning Objectives

This project provides hands-on experience with:

* AWS serverless architecture
* Event-driven application design
* Secure browser uploads
* Amazon Cognito authentication
* Amazon Textract integration
* Generative AI with Amazon Bedrock
* Prompt engineering
* JSON schema validation
* Python application development
* Static website hosting
* Content delivery with CloudFront
* IAM design
* Monitoring and observability
* Infrastructure as Code
* CI/CD automation
* Architecture Decision Records (ADRs)

---

## Portfolio Value

This project demonstrates the ability to:

* Translate a business requirement into a cloud-native solution
* Design secure AWS architectures
* Build serverless applications
* Implement event-driven workflows
* Integrate AWS managed AI services
* Design least-privilege IAM permissions
* Build scalable cloud-native applications
* Apply AWS Well-Architected Framework principles
* Document architectural decisions
* Explain design decisions and trade-offs during technical interviews

---

## Current Status

**Current Progress: Phase 4 Completed (Resume Processing)**

The project has successfully implemented the core serverless workflow, including secure uploads, authentication, and automated resume processing using Amazon Textract.

The next phase introduces Amazon Bedrock to analyze the extracted resume content and prepare structured data for portfolio website generation.

---

## Next Phase

### Phase 5 – AI Resume Analysis

The next phase integrates Amazon Bedrock to transform the extracted resume content into structured JSON suitable for portfolio website generation.

Planned work includes:

* Amazon Bedrock integration
* Prompt engineering
* JSON schema validation
* AI response validation
* Error handling
* Structured AI output
