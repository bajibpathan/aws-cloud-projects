# AWS AI Resume Builder

> **Build Status:** ✅ Phase 6 – Web Client Integration Completed

The AWS AI Resume Builder is a serverless, event-driven application that transforms an uploaded resume into a professionally designed portfolio website.

The application now supports an end-to-end workflow where users authenticate through a browser, securely upload resumes directly to Amazon S3, extract resume content using Amazon Textract, analyze it with Amazon Bedrock, and prepare structured data for portfolio website generation.

The project is being built incrementally to demonstrate practical AWS architecture, serverless development, security, automation, observability, generative AI integration, and modern cloud-native application design.

---

# Project Overview

Recruiters and hiring managers often spend only a short time reviewing a resume. A well-designed portfolio website provides a more engaging way to showcase professional experience, technical skills, certifications, and projects.

However, building and maintaining a personal website typically requires:

* Web development knowledge
* Manual resume formatting
* HTML, CSS, and JavaScript experience
* Website hosting configuration
* Continuous content updates

The AWS AI Resume Builder automates this entire workflow using AWS managed services and generative AI.

Users securely sign in through a browser-based application, upload a resume, and automatically generate structured resume data that will be used to create a professional portfolio website.

---

# Problem Statement

Creating a professional portfolio website from a resume usually involves several manual steps:

* Organizing resume content
* Designing a website layout
* Writing HTML, CSS, and JavaScript
* Configuring website hosting
* Publishing the website
* Updating the website whenever the resume changes

These tasks can be time-consuming, particularly for users without web development experience.

This project automates the entire workflow using AWS managed services, event-driven architecture, and generative AI.

---

# Solution Overview

The application provides an automated serverless pipeline that:

* Authenticates users using Amazon Cognito
* Generates secure Amazon S3 Presigned Upload URLs
* Uploads resumes directly to a private Amazon S3 bucket
* Starts resume processing automatically through an Amazon S3 event
* Extracts resume text using Amazon Textract
* Converts extracted content into structured JSON
* Analyzes and restructures resume content using Amazon Bedrock
* Generates AI-ready structured resume data
* Produces a professional static portfolio website (upcoming)
* Stores generated website files in Amazon S3
* Delivers the website securely through Amazon CloudFront

The result is a scalable, secure, fully serverless cloud-native application.

---

# High-Level Architecture

```text
User
    │
    ▼
Browser Application
    │
    ▼
Amazon Cognito
    │
    ▼
API Gateway HTTP API
    │
    ▼
Upload URL Lambda
    │
    ▼
Amazon S3 Presigned URL
    │
    ▼
Direct Resume Upload
    │
    ▼
Amazon S3
    │
    ▼
Resume Processor Lambda
    │
    ▼
Amazon Textract
    │
    ▼
AI Resume Analyzer Lambda
    │
    ▼
Amazon Bedrock
    │
    ▼
Structured Resume JSON
    │
    ▼
Portfolio Website Generator
    │
    ▼
Amazon S3 Website Bucket
    │
    ▼
Amazon CloudFront
```

> **Architecture Diagram**

```text
architecture/images/01-ai-resume-builder-high-level-workflow.png
```

---

# Project Highlights

The solution demonstrates:

* Fully serverless architecture
* Event-driven document processing
* Browser-based frontend using HTML, CSS, and Vanilla JavaScript
* Secure authentication using Amazon Cognito
* JWT-protected API Gateway HTTP APIs
* Direct browser uploads using Amazon S3 Presigned URLs
* Private Amazon S3 storage
* Resume text extraction using Amazon Textract
* AI-powered resume analysis using Amazon Bedrock
* Structured JSON generation
* Automated portfolio website generation
* Static website delivery using Amazon CloudFront
* Logging and monitoring using Amazon CloudWatch
* Least-privilege IAM permissions
* AWS Well-Architected Framework principles

---

# AWS Services

| Category            | AWS Service                   | Purpose                                                              |     Status    |
| :------------------ | :---------------------------- | :------------------------------------------------------------------- | :-----------: |
| Compute             | AWS Lambda                    | Execute serverless business logic                                    | ✅ Implemented |
| Storage             | Amazon S3                     | Store uploaded resumes, processed data, AI output, and website files | ✅ Implemented |
| API                 | Amazon API Gateway (HTTP API) | Expose secure application APIs                                       | ✅ Implemented |
| Authentication      | Amazon Cognito                | Authenticate users and issue JWT access tokens                       | ✅ Implemented |
| Document Processing | Amazon Textract               | Extract text from uploaded resumes                                   | ✅ Implemented |
| Generative AI       | Amazon Bedrock                | Analyze resumes and generate structured JSON                         | ✅ Implemented |
| Monitoring          | Amazon CloudWatch             | Logging, monitoring, and troubleshooting                             | ✅ Implemented |
| Security            | AWS IAM                       | Identity and access management                                       | ✅ Implemented |
| Content Delivery    | Amazon CloudFront             | Deliver generated portfolio websites globally                        |   🚧 Planned  |

---

# Current Progress

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

# Completed So Far

## Phase 1 – Project Foundation & Storage

This phase established the project foundation and secure storage architecture.

### Completed Activities

* Created the GitHub repository structure
* Defined the initial project architecture
* Created project documentation
* Established the Architecture Decision Record (ADR) structure
* Created a private resume upload bucket
* Created a private processed-data bucket
* Created a private website bucket
* Enabled Amazon S3 Block Public Access
* Enabled Bucket Owner Enforced object ownership
* Enabled server-side encryption using SSE-S3
* Configured lifecycle policies
* Enabled versioning where appropriate
* Created sample resume datasets
* Documented storage architecture decisions

---

## Phase 2 – Secure Resume Upload

This phase implemented secure, direct-to-S3 resume uploads using Amazon S3 Presigned URLs.

### Completed Activities

* Created an Amazon API Gateway HTTP API
* Developed the Upload URL Generator Lambda function
* Configured Lambda proxy integration
* Generated short-lived Amazon S3 Presigned URLs
* Added PDF file validation
* Implemented a 5 MB file size limit
* Generated unique object keys using UUIDs
* Used Lambda environment variables for configuration
* Created a least-privilege Lambda execution role
* Configured API Gateway CORS
* Uploaded resumes directly to a private Amazon S3 bucket
* Completed end-to-end upload validation

### Key Outcome

Large resume files bypass Lambda and upload directly to Amazon S3, reducing latency, improving scalability, and preventing AWS credentials from being exposed to the browser.

---

## Phase 3 – Authentication

This phase secured the upload API using Amazon Cognito and JWT authorization.

### Completed Activities

* Created an Amazon Cognito User Pool
* Configured an application client
* Created and confirmed test users
* Enabled username and password authentication
* Generated JWT access tokens
* Created an API Gateway JWT Authorizer
* Protected the `POST /upload-url` endpoint
* Verified unauthorized requests return **401 Unauthorized**
* Verified invalid JWT tokens are rejected
* Verified authenticated users receive a Presigned Upload URL
* Successfully uploaded resumes after authentication

### Key Outcome

Only authenticated users can request upload URLs and access protected backend APIs.

---

## Phase 4 – Resume Processing

This phase implemented an event-driven document-processing pipeline.

### Completed Activities

* Configured Amazon S3 ObjectCreated events
* Automatically triggered the Resume Processor Lambda
* Retrieved uploaded resume metadata
* Downloaded resumes from Amazon S3
* Integrated with Amazon Textract
* Extracted resume text
* Converted extracted text into structured JSON
* Stored processed JSON in the processed-data bucket
* Added structured CloudWatch logging
* Implemented exception handling
* Applied least-privilege IAM permissions
* Validated the end-to-end processing workflow

### Processing Workflow

```text
Resume Upload
      ↓
Amazon S3
      ↓
ObjectCreated Event
      ↓
Resume Processor Lambda
      ↓
Amazon Textract
      ↓
Structured Resume JSON
      ↓
Processed Data Bucket
```

### Challenges Resolved

During implementation, several production-style issues were identified and resolved, including:

* Missing IAM permissions
* InvalidS3ObjectException
* UnsupportedDocumentException
* Amazon Textract access issues
* Invalid test documents

CloudWatch Logs, the AWS CLI, and the IAM Policy Simulator were used throughout the troubleshooting process.

---

## Phase 5 – AI Resume Analysis

This phase introduced generative AI into the application using Amazon Bedrock.

### Completed Activities

* Created a dedicated AI Resume Analyzer Lambda
* Integrated Claude Sonnet 4.6 using Amazon Bedrock
* Configured a Bedrock inference profile
* Designed controlled prompt templates
* Implemented prompt injection safeguards
* Added hallucination prevention techniques
* Parsed and validated AI-generated JSON
* Stored AI output under a dedicated S3 prefix
* Added operational logging
* Troubleshot Bedrock access and IAM issues

### Key Outcome

The application now converts raw resume text into structured, AI-generated resume data that can be consumed by the upcoming Portfolio Website Generator.

---

## Phase 6 – Web Client Integration

This phase transformed the backend services into a complete browser-based application.

### Completed Activities

* Built a responsive frontend using HTML, CSS, and Vanilla JavaScript
* Integrated Amazon Cognito authentication
* Implemented browser session management
* Protected APIs using JWT Authorizers
* Requested Presigned Upload URLs through API Gateway HTTP API
* Uploaded resumes directly to Amazon S3
* Added client-side PDF validation
* Added backend validation for uploaded files
* Configured CORS for API Gateway and Amazon S3
* Implemented secure sign-in and sign-out functionality
* Completed end-to-end browser workflow testing

### Upload Workflow

```text
User
      ↓
Browser
      ↓
Amazon Cognito
      ↓
HTTP API
      ↓
Upload URL Lambda
      ↓
Amazon S3 Presigned URL
      ↓
Direct Upload to Amazon S3
      ↓
Resume Processing Pipeline
```

### Key Outcome

The application now provides a complete user-facing experience where authenticated users can securely upload resumes through the browser while the backend automatically processes and analyzes the uploaded content.

---

# Current Application Flow

The application currently supports the following end-to-end workflow:

```text
User Authentication
        ↓
Amazon Cognito
        ↓
Browser Application
        ↓
Protected Upload API
        ↓
Presigned URL Generation
        ↓
Direct Resume Upload to Amazon S3
        ↓
Resume Processor Lambda
        ↓
Amazon Textract
        ↓
AI Resume Analyzer Lambda
        ↓
Amazon Bedrock
        ↓
Structured Resume JSON
        ↓
Processed Data Bucket
```

The next phase will consume the structured AI-generated resume data to create a professional portfolio website.

---

# Repository Structure

```text
aws-ai-resume-builder/
│
├── architecture/
│   ├── decisions/
│   └── images/
│
├── docs/
│   
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── app.js
│
├── lambda/
│   ├── upload-url-generator/
│   ├── resume-processor/
│   ├── ai-resume-analyzer/
│   └── portfolio-generator/      (Upcoming)
│
├── policies/
├── prompts/
├── sample-resumes/
├── screenshots/
│
├── README.md
├── PROJECT_SUMMARY.md
└── INTERVIEW_GUIDE.md
```

The repository is intentionally organized to separate application code, infrastructure documentation, architectural decisions, and supporting assets, making it easier to navigate and maintain.

---
# Architecture Decision Records

Major architectural decisions are documented as Architecture Decision Records (ADRs).

Current ADRs include:

- ADR-001 – Use Separate Amazon S3 Buckets
- ADR-002 – Use Different Versioning Strategies
- ADR-003 – Use Amazon S3 Presigned URLs for Secure Resume Uploads
- ADR-004 – Use Amazon Cognito and API Gateway JWT Authorization
- ADR-005 – Use Amazon Textract for Resume Text Extraction
- ADR-006 – Use Amazon Bedrock for Resume Analysis
- ADR-007 – Browser-Based Web Client Integration

Future ADRs will be added as new architectural decisions and trade-offs are introduced throughout the project.

---

# Security Design

The project follows AWS security best practices and implements multiple layers of protection across authentication, authorization, storage, and application access.

## Authentication & Authorization

* Amazon Cognito User Pool authentication
* JWT-based authorization using API Gateway HTTP API
* Protected API endpoints using JWT Authorizers
* Browser session management
* Access Token authentication for backend APIs

## Storage Security

* Private Amazon S3 buckets
* Amazon S3 Block Public Access
* Bucket Owner Enforced object ownership
* Server-side encryption using SSE-S3
* Versioning enabled where appropriate

## Secure File Uploads

* Short-lived Amazon S3 Presigned URLs
* Direct browser uploads to Amazon S3
* No AWS credentials exposed to the browser
* Client-side PDF validation
* Backend validation of filename, file type, and file size
* Filename sanitization before generating object keys

## Identity & Access Management

* Least-privilege IAM roles
* Service-specific IAM permissions
* Lambda execution roles with minimal required access
* Principle of Least Privilege applied throughout the application

## Application Security

* HTTPS communication for all AWS services
* Request validation before upload
* Event-driven processing with private resources
* Structured CloudWatch logging for auditing and troubleshooting
* Sample resumes sanitized to remove personal information

---

# Reliability Design

The application is designed around managed AWS services that provide high availability, scalability, and fault tolerance.

## Current Reliability Features

* Event-driven architecture using Amazon S3 events
* Automatic Lambda invocation
* Exception handling within Lambda functions
* CloudWatch logging for operational visibility
* Unique object keys using UUIDs
* Backend validation before processing
* Structured JSON validation
* Modular Lambda functions with single responsibilities

## Planned Production Enhancements

The Production Readiness phase will include:

* Lambda retry strategy review
* Dead-letter queue (DLQ) implementation
* Idempotent processing
* Duplicate event handling
* CloudWatch alarms
* Operational dashboards
* Automated health monitoring
* Performance optimization
* Disaster recovery considerations

The goal is to ensure the application remains resilient while minimizing operational overhead.

---

# Cost Considerations

The application is designed using fully managed, pay-as-you-go AWS services to minimize operational costs.

## Primary Cost Drivers

* Amazon S3 storage
* AWS Lambda invocations and execution time
* Amazon API Gateway requests
* Amazon Textract document processing
* Amazon Bedrock model inference
* Amazon CloudFront requests and data transfer
* Amazon CloudWatch logs and metrics

## Current Cost Optimization Measures

* Fully serverless architecture
* No continuously running compute resources
* Direct browser uploads to Amazon S3 using Presigned URLs
* Short Lambda execution durations
* Lifecycle policies for uploaded resumes
* Small test datasets during development
* Cleanup of unused AWS resources
* Separation of storage buckets to simplify lifecycle management

## Planned Cost Improvements

During the Production Readiness phase, additional optimization will include:

* CloudWatch log retention policies
* Storage lifecycle optimization
* Cost monitoring dashboards
* Lambda memory tuning
* Bedrock prompt optimization
* Infrastructure cost analysis
* AWS Cost Explorer reporting

The objective is to maintain a cost-efficient architecture while supporting future scalability.

---

# Learning Journey

This repository is intentionally being built as a practical cloud engineering portfolio project rather than by following a complete tutorial.

Each phase is designed to simulate how production cloud applications are planned, implemented, tested, documented, and continuously improved.

## Engineering Workflow

Every major feature follows the same structured process:

1. Understand the business problem.
2. Design the architecture.
3. Evaluate implementation options and trade-offs.
4. Implement the solution.
5. Validate functionality through end-to-end testing.
6. Troubleshoot real-world issues.
7. Capture supporting screenshots.
8. Document architectural decisions using ADRs.
9. Update project documentation.
10. Commit changes using meaningful Git history.

This workflow emphasizes understanding **why** architectural decisions are made, not just **how** they are implemented.

## Skills Demonstrated

Through this project, the following cloud engineering skills are being developed:

* AWS serverless application development
* Event-driven architecture
* Browser-based application integration
* Secure authentication and authorization
* Direct Amazon S3 uploads using Presigned URLs
* Document processing with Amazon Textract
* Generative AI integration using Amazon Bedrock
* Secure API design
* IAM and least-privilege security
* Cloud-native application design
* Monitoring and observability
* Technical documentation
* Architecture decision documentation
* Troubleshooting distributed systems

## Project Goal

The objective of this project is not only to build a working application, but also to create a production-style portfolio that demonstrates practical cloud engineering skills, architectural thinking, and the ability to explain design decisions during technical interviews.

Each completed phase builds upon the previous one, resulting in an end-to-end cloud-native application that showcases real-world AWS implementation patterns and best practices.

---

# Upcoming Milestones

## Phase 7 – Portfolio Website Generation

The next phase will transform the AI-generated resume data into a professional static portfolio website.

### Planned Activities

* Develop a reusable HTML portfolio template
* Generate portfolio content from AI-generated resume JSON
* Build responsive CSS styling
* Generate project, certification, and skills sections
* Create downloadable resume functionality
* Generate website assets
* Upload generated website files to the website S3 bucket
* Prepare the application for Amazon CloudFront distribution
* Validate the complete website generation workflow

### Expected Outcome

Users will automatically receive a professional portfolio website generated from their uploaded resume without requiring any web development knowledge.

---

## Phase 8 – Production Readiness

The final phase will focus on preparing the application for production deployment by improving automation, operational visibility, security, and maintainability.

### Planned Activities

* Provision infrastructure using Infrastructure as Code (Terraform)
* Build a CI/CD pipeline using GitHub Actions
* Configure CloudWatch dashboards and alarms
* Implement retry strategies and failure handling
* Evaluate Dead Letter Queue (DLQ) implementation
* Improve security hardening
* Perform cost optimization
* Optimize Lambda performance
* Conduct end-to-end testing
* Finalize project documentation

### Expected Outcome

The application will follow production-ready cloud engineering practices and demonstrate a complete serverless application lifecycle.

---

# Portfolio Value

This project demonstrates the ability to:

## Cloud Architecture

* Design secure AWS cloud architectures
* Apply AWS Well-Architected Framework principles
* Build scalable serverless applications
* Design event-driven workflows
* Architect secure browser-based applications

## AWS Services

* Amazon S3
* AWS Lambda
* Amazon API Gateway
* Amazon Cognito
* Amazon Textract
* Amazon Bedrock
* Amazon CloudWatch
* AWS IAM
* Amazon CloudFront

## Security

* Implement least-privilege IAM permissions
* Protect APIs using JWT authorization
* Secure browser uploads using Amazon S3 Presigned URLs
* Design private Amazon S3 architectures
* Apply authentication and authorization best practices

## Serverless Development

* Develop Python-based AWS Lambda functions
* Build event-driven workflows
* Integrate managed AWS services
* Design modular cloud-native applications
* Implement secure API integrations

## AI Integration

* Process documents using Amazon Textract
* Build prompt-driven AI workflows
* Integrate Amazon Bedrock foundation models
* Validate structured AI-generated output
* Build AI-powered cloud applications

## Engineering Practices

* Troubleshoot distributed cloud applications
* Document architectural decisions using ADRs
* Produce production-style technical documentation
* Design modular application architectures
* Explain technical trade-offs during interviews

---

# Repository Documentation

The repository includes comprehensive documentation for every major phase of the project.

| Document                                 | Purpose                                             |
| :--------------------------------------- | :-------------------------------------------------- |
| **README.md**                            | Project overview and implementation progress        |
| **PROJECT_SUMMARY.md**                   | Executive summary of the project                    |
| **INTERVIEW_GUIDE.md**                   | Architecture explanations and interview preparation |
| **Architecture Decision Records (ADRs)** | Design decisions and technical trade-offs           |
| **Phase Documentation**                  | Implementation details for each completed phase     |

Each phase includes architecture diagrams, implementation notes, testing evidence, lessons learned, and supporting screenshots.

---

# Learning Outcomes

By completing this project, I have gained practical experience in:

* Designing secure serverless architectures
* Building browser-based cloud applications
* Implementing authentication using Amazon Cognito
* Protecting APIs with JWT authorization
* Building event-driven workflows
* Processing documents using Amazon Textract
* Integrating Generative AI using Amazon Bedrock
* Developing scalable cloud-native applications
* Applying AWS security best practices
* Troubleshooting production-style cloud issues
* Documenting architectural decisions
* Communicating technical solutions effectively

---

# Future Enhancements

Potential future improvements include:

* Multi-template portfolio generation
* Custom themes and branding
* Resume version management
* AI-powered resume recommendations
* Portfolio sharing with custom domains
* Analytics dashboard
* Multi-language support
* Email notifications
* Resume scoring and benchmarking
* Integration with LinkedIn and GitHub APIs

---

# Contributing

This repository is primarily a personal learning and portfolio project.

Suggestions, feedback, and discussions about cloud architecture, AWS services, serverless development, and AI integration are always welcome.

If you discover an issue or have an improvement suggestion, feel free to open an issue or submit a pull request.

---
## Acknowledgements

This project was inspired by and initially developed as part of the **AWS Accelerator** program by **Rajesh Daswani (IaaS Academy)**.

The live sessions and the original project provided the foundation for learning the overall architecture and implementation approach.

Repository reference:

* https://github.com/iaasacademy/ai-resume-builder-aws

Beyond the original implementation, this repository has been significantly extended as part of my personal cloud engineering learning journey. Additional work includes:

* Comprehensive project documentation
* Architecture Decision Records (ADRs)
* Detailed phase-by-phase implementation guides
* Interview preparation guide
* Enhanced project summary
* Browser-based frontend integration using HTML, CSS, and Vanilla JavaScript
* Improved architecture documentation and diagrams
* End-to-end testing documentation
* Troubleshooting notes and lessons learned
* GitHub portfolio optimization

The goal of this repository is not only to recreate the original project, but also to deepen my understanding of AWS services, serverless architecture, event-driven design, security best practices, and AI integration through hands-on implementation and documentation.


---

# Next Phase

## Phase 7 – Portfolio Website Generation

The next milestone is to generate a professional portfolio website from the AI-generated resume data.

This phase will complete the core business objective of the project by transforming structured resume information into a responsive static website hosted in Amazon S3 and delivered securely through Amazon CloudFront.

---

⭐ **If you found this project helpful or interesting, consider giving the repository a star. Feedback and suggestions are always appreciated!**
