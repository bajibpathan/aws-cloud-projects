# AWS AI Resume Builder — Project Summary

## Project Overview

The AWS AI Resume Builder is a serverless, event-driven application that transforms an uploaded resume into a professionally designed portfolio website.

Users securely sign in through a browser-based web application, upload a resume directly to Amazon S3, extract its content using Amazon Textract, process the extracted data with Amazon Bedrock, and generate a professional portfolio website that can be securely delivered through Amazon CloudFront.

The project is being built incrementally to demonstrate practical AWS architecture, serverless development, security, automation, observability, AI integration, and modern cloud-native application design.

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
Browser Application
        ↓
Request Presigned Upload URL
        ↓
API Gateway HTTP API
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
AI Resume JSON
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
| Phase 5 | AI Resume Analysis           |   ✅ Complete  |
| Phase 6 | Web Client Integration       |   ✅ Complete  |
| Phase 7 | Portfolio Website Generation |   🚧 Planned  |
| Phase 8 | Production Readiness         | ⬜ Not Started |

---

## Current Implementation

The application currently includes:

* Project foundation and organized GitHub repository structure
* Browser-based frontend built with HTML, CSS, and Vanilla JavaScript
* Secure user authentication using Amazon Cognito
* JWT-protected Amazon API Gateway HTTP APIs
* Three private Amazon S3 buckets for resume uploads, processed data, and generated website files
* Secure browser uploads using Amazon S3 Presigned URLs
* Client-side and server-side file validation
* Presigned upload URL generation using AWS Lambda
* Event-driven resume processing using Amazon S3 Event Notifications
* Resume text extraction using Amazon Textract
* Structured Textract output stored in the processed-data bucket
* AI resume analysis using Amazon Bedrock
* Claude Sonnet 4.6 integration through a Bedrock inference profile
* Structured and validated AI resume JSON generation
* Separate `processed/` and `ai-output/` prefixes in the processed-data bucket
* Amazon CloudWatch logging and troubleshooting
* Dedicated IAM roles following the principle of least privilege
* Complete end-to-end workflow from browser login through AI-generated resume data

The project now provides a complete user-facing workflow, allowing authenticated users to securely upload resumes through the browser while maintaining a fully serverless backend architecture.

---

## Core AWS Services

| AWS Service        | Purpose                                   | Status |
| ------------------ | ----------------------------------------- | :----: |
| Amazon S3          | Store uploaded resumes and processed data |    ✅   |
| Amazon API Gateway | Expose secure APIs                        |    ✅   |
| AWS Lambda         | Execute serverless business logic         |    ✅   |
| Amazon Cognito     | Authenticate users                        |    ✅   |
| Amazon Textract    | Extract resume text                       |    ✅   |
| Amazon Bedrock     | AI-powered resume analysis                |    ✅   |
| Amazon CloudWatch  | Logging and monitoring                    |    ✅   |
| AWS IAM            | Identity and access management            |    ✅   |
| Amazon CloudFront  | Deliver generated portfolio websites      |   🚧   |

---

## Key Architecture Characteristics

### Serverless

The application is built entirely using managed AWS services without requiring continuously running servers.

### Event-Driven

Resume processing begins automatically when a document is uploaded to Amazon S3.

### Secure Browser Uploads

Amazon S3 Presigned URLs allow authenticated users to upload resumes directly to a private Amazon S3 bucket without exposing AWS credentials.

### Authentication

Amazon Cognito provides secure user registration, authentication, and JWT-based authorization for all protected APIs.

### Separation of Concerns

Each Lambda function performs a single responsibility:

* Upload URL generation
* Resume processing
* AI resume analysis
* Portfolio website generation

### AI-Ready Architecture

Resume data is converted into structured JSON before being processed by Amazon Bedrock, creating a modular workflow that is easy to extend.

### Static Website Delivery

Generated portfolio websites will be stored in Amazon S3 and distributed globally through Amazon CloudFront.

---

## Application Features

### Completed

* Browser-based authentication
* Secure resume uploads
* Amazon Cognito integration
* JWT-protected APIs
* Browser uploads using Presigned URLs
* PDF validation
* Event-driven processing
* Resume text extraction
* AI-powered resume analysis
* Structured JSON generation
* CloudWatch logging
* Least-privilege IAM implementation
* Private Amazon S3 storage

### Planned

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
* Amazon Cognito authentication
* JWT-protected APIs
* Short-lived Amazon S3 Presigned URLs
* Client-side and server-side validation
* Encryption at rest
* HTTPS communication
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
* JWT authorization
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
* Build end-to-end serverless applications
* Implement event-driven workflows
* Integrate AWS managed AI services
* Build secure browser applications
* Design least-privilege IAM permissions
* Apply AWS Well-Architected Framework principles
* Document architectural decisions
* Explain design decisions and trade-offs during technical interviews

---

## Current Status

**Current Phase: Phase 6 – Web Client Integration (Completed)**

### Completed

* Project foundation and S3 storage
* Secure resume uploads
* Browser-based frontend
* Amazon Cognito authentication
* JWT authorization
* Direct browser uploads using Amazon S3 Presigned URLs
* Resume processing with Amazon Textract
* AI resume analysis using Amazon Bedrock
* Structured AI resume JSON generation
* Event-driven processing
* CloudWatch logging
* End-to-end browser workflow validation

### Next

**Phase 7 – Portfolio Website Generation**

The next phase will generate a professional static portfolio website from the AI-generated resume data and prepare it for secure hosting through Amazon S3 and Amazon CloudFront.
