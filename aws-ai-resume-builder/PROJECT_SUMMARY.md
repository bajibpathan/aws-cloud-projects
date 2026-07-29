# AWS AI Resume Builder

> A serverless, event-driven application that converts a resume into a professional portfolio website using AWS managed services and Generative AI.

---

# Executive Summary

The AWS AI Resume Builder automates the process of transforming a resume into a responsive portfolio website.

Users securely authenticate using Amazon Cognito, upload their resume through a browser, and the application automatically extracts the content, enhances it using Amazon Bedrock, generates a portfolio website, and publishes it through Amazon CloudFront.

The solution demonstrates modern AWS cloud architecture using a fully serverless, event-driven design.

---

# Solution at a Glance

| Category | Details |
|----------|---------|
| **Architecture** | Serverless, Event-Driven |
| **Frontend** | HTML, CSS, JavaScript |
| **Authentication** | Amazon Cognito |
| **API** | Amazon API Gateway |
| **Compute** | AWS Lambda |
| **Storage** | Amazon S3 |
| **AI Service** | Amazon Bedrock |
| **Document Processing** | Amazon Textract |
| **Content Delivery** | Amazon CloudFront |
| **Monitoring** | Amazon CloudWatch |

---

# End-to-End Workflow

```text
User Login
      │
      ▼
Amazon Cognito
      │
      ▼
Upload Resume
      │
      ▼
Amazon S3
      │
      ▼
Amazon Textract
      │
      ▼
Amazon Bedrock
      │
      ▼
Portfolio Generator
      │
      ▼
Amazon S3 Website
      │
      ▼
Amazon CloudFront
```

---

# Implementation Summary

| Phase | Outcome |
|--------|---------|
| **Phase 1** | Project foundation and Amazon S3 storage |
| **Phase 2** | Secure resume uploads using Presigned URLs |
| **Phase 3** | User authentication with Amazon Cognito |
| **Phase 4** | Resume processing using Amazon Textract |
| **Phase 5** | AI-powered resume enhancement with Amazon Bedrock |
| **Phase 6** | Browser-based frontend integration |
| **Phase 7** | Portfolio website generation and CloudFront delivery |

---

# AWS Services Used

- Amazon Cognito
- Amazon API Gateway
- AWS Lambda
- Amazon S3
- Amazon Textract
- Amazon Bedrock
- Amazon CloudFront
- Amazon CloudWatch
- AWS IAM

---

# Key Capabilities

- Secure user authentication
- Direct browser uploads using Presigned URLs
- Event-driven processing
- AI-powered resume enhancement
- Automatic portfolio website generation
- Static website hosting
- Global content delivery
- Centralized logging and monitoring

---

# Skills Demonstrated

### Cloud Engineering

- Serverless Architecture
- Event-Driven Design
- REST API Development
- Identity & Access Management
- Secure File Upload

### AI Integration

- Amazon Bedrock
- Prompt Engineering
- JSON Processing

### AWS Services

- Lambda
- S3
- Cognito
- Textract
- CloudFront
- CloudWatch
- IAM

---

# Repository Structure

```text
README.md
PROJECT_SUMMARY.md
architecture/
docs/
frontend/
lambda/
templates/
```

---

# Documentation

| Document | Purpose |
|----------|---------|
| README.md | Complete project documentation |
| PROJECT_SUMMARY.md | Executive project overview |
| architecture/ | Architecture diagrams and ADRs |
| docs/ | Phase-by-phase implementation guides |

---

# Project Status

**Status:** ✅ Completed

This project demonstrates how AWS managed services and Generative AI can be combined to build a secure, scalable, and fully automated serverless application.

---
