# AWS AI Resume Builder — Project Summary

## Project Overview

The AWS AI Resume Builder is a serverless, event-driven application that transforms an uploaded resume into a structured and professionally formatted portfolio website.

Users upload a resume through a web interface. The application securely stores the document, extracts its content, processes the extracted text using generative AI, and creates a static portfolio website that can be delivered through Amazon CloudFront.

The project is being built incrementally to demonstrate practical AWS architecture, serverless development, security, automation, observability and AI integration.

---

## Business Problem

Creating a professional portfolio website from a resume can require:

* Manual content extraction
* Website development knowledge
* Resume restructuring
* HTML and CSS experience
* Hosting and deployment configuration
* Ongoing maintenance

The AWS AI Resume Builder automates this process by converting resume content into structured data and generating a static portfolio website.

---

## Solution

The application follows this workflow:

```text
User uploads a resume
        ↓
Application generates an S3 presigned URL
        ↓
Resume is uploaded directly to Amazon S3
        ↓
An S3 event starts the processing workflow
        ↓
Amazon Textract extracts resume content
        ↓
Amazon Bedrock converts the content into structured JSON
        ↓
A Python renderer generates the portfolio website
        ↓
The website is stored in Amazon S3
        ↓
Amazon CloudFront delivers the generated website
```

---

## Core AWS Services

| AWS Service        | Purpose                                            |
| ------------------ | -------------------------------------------------- |
| Amazon S3          | Store uploaded resumes and generated website files |
| Amazon API Gateway | Expose application APIs                            |
| AWS Lambda         | Execute serverless application logic               |
| Amazon Cognito     | Authenticate and authorize users                   |
| Amazon Textract    | Extract text and document structure from resumes   |
| Amazon SNS         | Support asynchronous event communication           |
| Amazon Bedrock     | Transform resume content into structured data      |
| Amazon CloudFront  | Deliver generated portfolio websites               |
| Amazon CloudWatch  | Collect logs, metrics and operational information  |
| AWS IAM            | Control access between users and AWS services      |

The final service list may evolve as the architecture is implemented and validated.

---

## Key Architecture Characteristics

### Serverless

The application uses managed AWS services and does not require continuously running servers.

### Event-Driven

Resume processing begins automatically when a document is uploaded to Amazon S3.

### Asynchronous Processing

Long-running document-processing tasks are separated from the initial upload request.

### Secure File Uploads

S3 presigned URLs allow the browser to upload files directly to a private bucket without exposing AWS credentials.

### Separation of Concerns

Different Lambda functions handle upload authorization, resume processing and website generation.

### Structured AI Output

Amazon Bedrock is expected to return validated JSON rather than directly generating the final HTML website.

### Static Website Delivery

Generated websites are stored in Amazon S3 and distributed through Amazon CloudFront.

---

## Planned Functional Capabilities

* User authentication
* Resume upload through presigned URLs
* PDF file validation
* Resume text extraction
* AI-assisted resume restructuring
* Structured JSON generation
* Static HTML portfolio generation
* Website publication
* Processing status tracking
* Error handling and retry mechanisms
* Logging and monitoring
* Automated infrastructure deployment

---

## Security Considerations

The project will apply the following security practices:

* Private S3 buckets
* Least-privilege IAM permissions
* Short-lived S3 presigned URLs
* File type and file size validation
* Encryption at rest
* HTTPS for application communication
* User authentication and authorization
* Sensitive-data protection
* CloudWatch logging
* Controlled access to generated websites
* Secure handling of application configuration and secrets

---

## Reliability Considerations

The architecture will evaluate:

* Lambda retry behavior
* Asynchronous failure handling
* Dead-letter queues
* Idempotent processing
* Duplicate event handling
* Textract job-status tracking
* Bedrock response validation
* Partial-processing recovery
* CloudWatch alarms
* Operational dashboards

---

## Cost Considerations

The application is designed around usage-based AWS services.

Primary cost drivers may include:

* Resume storage in Amazon S3
* Lambda invocations and execution duration
* API Gateway requests
* Amazon Textract document processing
* Amazon Bedrock model inference
* CloudFront requests and data transfer
* CloudWatch logs and metrics

Lifecycle policies and cleanup automation will be considered to control storage and operational costs.

---

## Learning Objectives

This project is intended to build practical knowledge in:

* AWS serverless architecture
* Event-driven application design
* Secure browser-based uploads
* Document-processing workflows
* Generative AI integration
* Prompt engineering
* JSON schema validation
* Python-based HTML generation
* Static website hosting
* CDN delivery
* IAM design
* Monitoring and observability
* Infrastructure as Code
* CI/CD automation
* Architecture Decision Records

---

## Portfolio Value

This project demonstrates the ability to:

* Translate a business problem into a cloud architecture
* Select appropriate AWS managed services
* Design secure and scalable workflows
* Build event-driven serverless applications
* Integrate AI into a practical application
* Evaluate architectural alternatives
* Document technical decisions
* Test and validate cloud components
* Explain design trade-offs during interviews

---

## Current Status

> **Phase 1 — Project Foundation**

Current activities include:

* Defining the project scope
* Designing the high-level architecture
* Creating the repository structure
* Establishing documentation standards
* Preparing Architecture Decision Records
* Protecting sensitive test data
* Preparing the project for incremental implementation

No production AWS resources have been deployed at this stage.

---

## Planned Next Phase

Phase 2 will focus on the storage and secure upload layer.

Planned activities include:

* Designing the resume S3 bucket
* Designing the generated website S3 bucket
* Defining bucket security settings
* Reviewing encryption and lifecycle policies
* Evaluating S3 presigned URL uploads
* Creating the first detailed Architecture Decision Records
* Implementing and validating the storage layer
