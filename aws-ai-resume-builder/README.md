# AWS AI Resume Builder

> **Build Status:** ✅ Phase 3 – Secure Resume Upload (Completed)

An end-to-end serverless AWS application that transforms a resume into a professional portfolio website using Amazon Textract, Amazon Bedrock and modern AWS serverless services.

The project is being designed, implemented, tested and documented incrementally. Each phase is completed, validated and committed to GitHub before moving to the next stage.

---

# Project Overview

Recruiters and hiring managers often spend only a few seconds reviewing a resume. A well-designed personal website provides a more engaging way to present professional experience, technical skills and projects.

However, building a personal website typically requires web development knowledge, manual formatting and ongoing maintenance.

This project automates that entire process.

Users upload a resume through a secure web application. The application extracts the resume content, understands the information using Generative AI, and automatically generates a professional static portfolio website.

The solution follows a serverless, event-driven architecture designed using AWS best practices for security, scalability, reliability and cost optimization.

---

# Problem Statement

Creating a professional portfolio website usually involves multiple manual steps:

* Writing HTML, CSS and JavaScript
* Organizing resume content
* Choosing a website layout
* Hosting the website
* Updating the website whenever the resume changes

These tasks can be time-consuming, especially for users without web development experience.

This project automates the entire workflow using managed AWS services and Generative AI.

---

# Solution Overview

The application provides an automated pipeline that:

* Securely uploads resume files using Amazon S3 presigned URLs
* Stores uploaded resumes in a private Amazon S3 bucket
* Extracts document text using Amazon Textract
* Understands resume content using Amazon Bedrock
* Converts extracted information into structured JSON
* Generates a professional portfolio website
* Stores the generated website in Amazon S3
* Delivers the website globally through Amazon CloudFront

The result is a scalable, secure and fully serverless architecture.

---

# High-Level Architecture

```text
                    User
                      │
                      ▼
              Frontend Application
                      │
                      ▼
             Amazon API Gateway
                      │
                      ▼
                AWS Lambda
                      │
          Generate Presigned URL
                      │
                      ▼
         Amazon S3 (Resume Upload)
                      │
                      ▼
             Amazon Textract
                      │
                      ▼
                Amazon SNS
                      │
                      ▼
                AWS Lambda
                      │
                      ▼
             Amazon Bedrock
                      │
                      ▼
          Python HTML Generator
                      │
                      ▼
        Amazon S3 (Website Bucket)
                      │
                      ▼
          Amazon CloudFront
                      │
                      ▼
        Generated Portfolio Website
```

A detailed AWS architecture diagram is available in the `architecture/images` directory.

---

# Project Highlights

The completed solution is designed to provide:

* Fully serverless architecture
* Event-driven processing
* Secure resume uploads using Amazon S3 Presigned URLs
* Private Amazon S3 storage
* Authentication with Amazon Cognito
* Document text extraction using Amazon Textract
* AI-powered resume understanding using Amazon Bedrock
* Structured JSON generation
* Automated HTML portfolio generation
* Global content delivery through Amazon CloudFront
* Monitoring using Amazon CloudWatch
* IAM least-privilege security model
* AWS Well-Architected Framework best practices

---

# AWS Services

| Category            | Services           |
| ------------------- | ------------------ |
| Compute             | AWS Lambda         |
| Storage             | Amazon S3          |
| AI                  | Amazon Bedrock     |
| Document Processing | Amazon Textract    |
| API                 | Amazon API Gateway |
| Messaging           | Amazon SNS         |
| Authentication      | Amazon Cognito     |
| CDN                 | Amazon CloudFront  |
| Monitoring          | Amazon CloudWatch  |
| Security            | AWS IAM            |

---

# Current Progress

| Phase    | Description                                 |     Status     |
| :------- | :------------------------------------------ | :------------: |
| Phase 1  | Project Foundation                          |   ✅ Complete   |
| Phase 2  | Storage Layer (Amazon S3)                   |   ✅ Complete   |
| Phase 3  | Secure Resume Upload (API Gateway & Lambda) |   ✅ Complete   |
| Phase 4  | Authentication (Amazon Cognito)             |   ✅ Complete   |
| Phase 5  | Document Processing (Textract & SNS)        |  ⬜ Not Started |
| Phase 6  | AI Processing (Amazon Bedrock)              |  ⬜ Not Started |
| Phase 7  | Portfolio Website Generation                |  ⬜ Not Started |
| Phase 8  | Frontend Integration                        |  ⬜ Not Started |
| Phase 9  | Observability (CloudWatch)                  |  ⬜ Not Started |
| Phase 10 | Reliability & Security                      |  ⬜ Not Started |
| Phase 11 | Cost Optimization                           |  ⬜ Not Started |
| Phase 12 | Final Testing & Documentation               |  ⬜ Not Started |

---

# Completed So Far

## Phase 1 – Project Foundation

* Repository structure
* Initial architecture
* Project documentation
* Architecture Decision Record (ADR) structure

## Phase 2 – Storage Layer

* Private Resume Upload Bucket
* Private Website Bucket
* Server-side encryption (SSE-S3)
* Lifecycle policy for uploaded resumes
* Versioning for generated websites
* Block Public Access
* Bucket Owner Enforced
* Sample resume dataset
* Architecture Decision Records for storage design

## Phase 3 – Secure Resume Upload

- HTTP API using Amazon API Gateway
- Lambda proxy integration
- Lambda execution role with least-privilege IAM permissions
- Presigned URL generation
- File validation (type and size)
- Secure direct uploads to a private Amazon S3 bucket
- API-level CORS configuration
- End-to-end upload testing

## Phase 4 – Authentication and API Security

- Created an Amazon Cognito User Pool
- Created a public application client without a client secret
- Created and confirmed a test user
- Enabled username and password authentication for testing
- Created an API Gateway JWT authorizer
- Protected the `POST /upload-url` route
- Verified unauthenticated requests return `401 Unauthorized`
- Generated an Amazon Cognito access token
- Verified authenticated requests return a presigned upload URL
- Successfully uploaded a resume to the private S3 bucket

---

# Repository Structure

```text
aws-ai-resume-builder/
│
├── architecture/
│   ├── images/
│   └── decisions/
│
├── docs/
├── frontend/
├── lambda/
├── policies/
├── prompts/
├── sample-resumes/
├── screenshots/
├── tests/
│
├── README.md
├── PROJECT_SUMMARY.md
└── INTERVIEW_GUIDE.md
```

---

# Architecture Decision Records (ADRs)

Important design decisions are documented as Architecture Decision Records.

Current ADRs include:

* ADR-001 – Use Separate S3 Buckets
* ADR-002 – Use Different Versioning Strategies
* ADR-003 - Use Amazon S3 Presigned URLs for Secure Resume Uploads
* ADR-004 - Use Amazon Cognito and API Gateway JWT Authorization 

Additional ADRs will be added as new architectural decisions are made.

---

# Learning Journey

This repository is intentionally being built as a hands-on engineering project rather than by following a tutorial.

For every feature, the same engineering workflow is followed:

1. Understand the business requirement
2. Design the solution
3. Implement the feature
4. Test the implementation
5. Capture screenshots
6. Document architectural decisions (ADR)
7. Commit and push to GitHub
8. Update project documentation at the end of each phase

The objective is not only to build a working application, but also to understand the reasoning behind every architectural decision and create a portfolio project that demonstrates real-world cloud engineering practices.

---

# Upcoming Milestones

* Complete API Gateway integration
* Build secure browser uploads
* Process resumes using Amazon Textract
* Generate structured resume JSON with Amazon Bedrock
* Render portfolio websites automatically
* Deliver websites securely using Amazon CloudFront
* Add observability, security hardening and cost optimization
