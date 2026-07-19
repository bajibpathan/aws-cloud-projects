# AWS AI Resume Builder

> **Build Status:** 🚧 Phase 1 – Project Foundation (In Progress)

This project is being designed, implemented, tested and documented incrementally. Each phase is completed, validated and committed to GitHub before moving to the next stage.


---

# Project Overview

Recruiters and hiring managers often spend only a few seconds reviewing a resume. A well-designed personal website provides a more engaging way to present professional experience, technical skills and projects.

However, building a personal website typically requires web development knowledge, manual formatting and ongoing maintenance.

This project automates that entire process.

Users upload a PDF resume through a secure web application. The application extracts the resume content, understands the information using Generative AI, and automatically generates a professional static website.

The solution follows an event-driven serverless architecture that scales automatically without requiring server management.

The project is being built from scratch as a learning and portfolio project while following AWS best practices for security, scalability, reliability and cost optimization.

---

# Problem Statement

Creating a professional personal website usually involves multiple manual steps:

- Writing HTML and CSS
- Organizing resume content
- Choosing a website layout
- Hosting the website
- Keeping the website updated whenever the resume changes

These tasks can be time-consuming, especially for users without web development experience.

The goal of this project is to automate the entire workflow using managed AWS services and Generative AI.

---

# Solution Overview

The application provides an automated pipeline that:

- Accepts secure PDF uploads
- Extracts text using Amazon Textract
- Understands resume content using Amazon Bedrock
- Converts the extracted information into structured JSON
- Generates a professional HTML website using Python
- Stores the website in Amazon S3
- Delivers the website globally through Amazon CloudFront

The result is a scalable, secure and fully serverless solution that demonstrates modern cloud architecture patterns.


# Project Highlights

The completed solution is designed to provide:

- A fully serverless and event-driven architecture
- Secure PDF resume uploads using Amazon S3 presigned URLs
- Authentication and authorization with Amazon Cognito
- Automated document text extraction using Amazon Textract
- Asynchronous document processing using Amazon SNS
- AI-powered resume understanding using Amazon Bedrock
- Structured JSON generation for deterministic website rendering
- Professional HTML website generation using reusable Python templates
- Secure static website hosting using Amazon S3 and Amazon CloudFront
- Logging, monitoring and troubleshooting using Amazon CloudWatch
- Security based on IAM least-privilege principles
- Architecture aligned with the AWS Well-Architected Framework

### Key Design Principles

This project follows several cloud architecture best practices:

- **Event-Driven Architecture** – Components communicate through events instead of continuous polling.
- **Serverless Design** – Managed AWS services automatically scale without server management.
- **Separation of Concerns** – Each AWS service is responsible for a single business function.
- **AI-Assisted Processing** – Amazon Bedrock extracts structured information, while Python generates the final website.
- **Security by Design** – Authentication, authorization and least-privilege access are applied throughout the solution.


# Project Progress

The project is being developed iteratively. Each phase is designed, implemented, tested, documented and committed before moving to the next stage.

| Phase | Description | Status |
|:------|:------------|:------:|
| Phase 1 | Project Foundation | 🚧 In Progress |
| Phase 2 | Storage Layer (Amazon S3) | ⬜ Not Started |
| Phase 3 | API Layer (API Gateway & Presigned Uploads) | ⬜ Not Started |
| Phase 4 | Authentication Layer (Amazon Cognito) | ⬜ Not Started |
| Phase 5 | Document Processing (Lambda, Amazon Textract & Amazon SNS) | ⬜ Not Started |
| Phase 6 | AI Processing (Amazon Bedrock) | ⬜ Not Started |
| Phase 7 | Presentation Layer (Python HTML Renderer & CloudFront) | ⬜ Not Started |
| Phase 8 | Frontend Integration | ⬜ Not Started |
| Phase 9 | Observability (Amazon CloudWatch) | ⬜ Not Started |
| Phase 10 | Reliability & Security | ⬜ Not Started |
| Phase 11 | Cost Optimization | ⬜ Not Started |
| Phase 12 | Final Testing & Documentation | ⬜ Not Started |



# Learning Journey

This repository is being built as a hands-on learning and portfolio project rather than simply following a tutorial.

For every phase, the same engineering workflow is followed:

1. Understand the AWS concept
2. Design the architecture
3. Implement the solution
4. Validate the functionality
5. Document the implementation
6. Commit and push the changes to GitHub
7. Capture key learnings and interview notes

The goal is not only to build a working application, but also to understand the architectural decisions behind every AWS service used. This approach helps reinforce cloud engineering best practices and prepares the project for technical discussions and interviews.



