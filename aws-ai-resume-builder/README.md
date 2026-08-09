# 🚀 AWS AI Resume Builder

<p align="center">

![AWS](https://img.shields.io/badge/AWS-Serverless-orange?logo=amazonaws)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Amazon S3](https://img.shields.io/badge/Amazon-S3-red?logo=amazons3)
![AWS Lambda](https://img.shields.io/badge/AWS-Lambda-orange?logo=awslambda)
![Amazon Textract](https://img.shields.io/badge/Amazon-Textract-green)
![Amazon Bedrock](https://img.shields.io/badge/Amazon-Bedrock-purple)
![Amazon Cognito](https://img.shields.io/badge/Amazon-Cognito-blue)
![Amazon CloudFront](https://img.shields.io/badge/Amazon-CloudFront-blue)
![Project Status](https://img.shields.io/badge/Status-Completed-success)
![Documentation](https://img.shields.io/badge/Documentation-Complete-success)
![License](https://img.shields.io/badge/License-MIT-brightgreen)

</p>

---

## 📌 Project Overview

AWS AI Resume Builder is a production-style, serverless application that transforms a PDF resume into a professional portfolio website using AWS AI and serverless technologies.

The application securely accepts resume uploads, extracts content using Amazon Textract, enhances and restructures the information with Amazon Bedrock, and automatically generates a responsive portfolio website that is hosted on Amazon S3 and delivered globally through Amazon CloudFront.

This project demonstrates real-world cloud engineering practices including event-driven architecture, serverless development, secure authentication, infrastructure security, AI integration, and static website hosting.

---

# 🏢 Business Problem

Recruiters and hiring managers often receive resumes in a variety of formats, making manual screening time-consuming and inconsistent. Candidates also struggle to understand how effectively their resumes communicate their skills and experience or how to transform them into a professional online portfolio.

Traditional resume reviews are largely manual, making it difficult to provide personalized feedback, structured insights, or an engaging digital representation of a candidate's profile.

---

# 💡 Solution

AWS AI Resume Builder demonstrates a production-inspired serverless application that automates resume processing using managed AWS services.

The solution enables users to securely upload resumes, extract structured information, leverage Generative AI to enhance and analyze resume content, and automatically generate a professional portfolio website.

The application is designed around modern cloud engineering principles including event-driven architecture, serverless computing, least-privilege security, Infrastructure as Code readiness, and operational observability.

---

# 🎯 Engineering Goals

This project was designed to demonstrate the following cloud engineering capabilities:

- Design an end-to-end event-driven serverless architecture
- Build secure APIs using Amazon API Gateway and Amazon Cognito
- Process documents automatically using Amazon Textract
- Integrate Generative AI using Amazon Bedrock
- Generate static portfolio websites using Amazon S3 and Amazon CloudFront
- Apply AWS security and Well-Architected best practices
- Build scalable and loosely coupled cloud-native applications
- Produce comprehensive engineering documentation for maintainability and knowledge sharing

---

# ✨ Key Features

### 🔐 Security

- Amazon Cognito authentication
- JWT-secured REST APIs
- Amazon S3 presigned uploads
- Least-privilege IAM permissions

### 🤖 AI & Document Processing

- Resume text extraction with Amazon Textract
- AI-powered resume analysis using Amazon Bedrock
- Structured JSON generation
- Automated portfolio content generation

### ☁️ Cloud Architecture

- Event-driven serverless design
- RESTful APIs with Amazon API Gateway
- Static website hosting with Amazon CloudFront
- CloudWatch monitoring and logging

---

# 🏗️ Solution Architecture

<p align="center">
  <img src="architecture/images/aws-ai-resume-builder-architecture.png"
       alt="AWS AI Resume Builder Architecture"
       width="100%">
</p>

The application follows an event-driven serverless architecture. Each AWS service performs a dedicated responsibility, allowing the solution to remain loosely coupled, scalable, secure, and independently maintainable.

---

# 🔄 Application Workflow

<p align="center">
  <img src="architecture/images/aws-ai-resume-builder-high-level-workflow.png"
       alt="AWS AI Resume Builder High-Levellication Workflow"
       width="100%">
</p>

The workflow shows the end-to-end processing path from secure resume upload through document extraction, AI-powered analysis, portfolio generation, and global delivery through Amazon CloudFront.

---

# ☁️ AWS Services Used

| AWS Service | Purpose |
|-------------|---------|
| Amazon Cognito | Authenticate users and issue JWT tokens |
| Amazon API Gateway | Expose secure REST APIs |
| AWS Lambda | Execute application logic |
| Amazon S3 | Store resumes, generated content, and static websites |
| Amazon Textract | Extract structured text from uploaded resumes |
| Amazon Bedrock | Analyze and enhance resume content using Generative AI |
| Amazon DynamoDB | Store application metadata and structured resume information |
| Amazon CloudFront | Deliver generated portfolio websites globally |
| Amazon CloudWatch | Collect logs, metrics, and operational insights |
| AWS IAM | Secure access using least-privilege permissions |

---

# 🏛️ Architecture Decisions at a Glance

The following table summarizes the key architectural decisions made during the design of this application. Detailed Architecture Decision Records (ADRs) are available in the [`architecture/decisions`](architecture/decisions/) directory.

| Area | Decision | Why This Approach? |
|------|----------|--------------------|
| Compute | AWS Lambda | Fully managed compute with automatic scaling and no server management |
| API | Amazon API Gateway | Secure, scalable REST APIs with built-in authorization and throttling |
| Authentication | Amazon Cognito | Managed user authentication without maintaining custom identity infrastructure |
| Storage | Amazon S3 | Highly durable object storage for resumes, generated content, and static websites |
| Document Processing | Amazon Textract | Extract structured text from resumes without building custom OCR logic |
| AI Processing | Amazon Bedrock | Integrate Generative AI using managed foundation models |
| Database | Amazon DynamoDB | Serverless NoSQL database with low operational overhead |
| CDN | Amazon CloudFront | Low-latency global delivery for generated portfolio websites |
| Monitoring | Amazon CloudWatch | Centralized logging, metrics, and operational visibility |
| Security | IAM Least Privilege | Restrict permissions to only the resources required by each component |

---

# 📂 Repository Structure

```text
aws-ai-resume-builder/
│
├── architecture/
│   ├── decisions/
│   └── images/
│
├── docs/
│   ├── phase-01-project-foundation.md
│   ├── phase-02-secure-upload.md
│   ├── phase-03-authentication.md
│   ├── phase-04-resume-processing.md
│   ├── phase-05-ai-resume-analysis.md
│   ├── phase-06-web-client-integration.md
│   ├── phase-07-portfolio-generation.md
│   ├── troubleshooting.md
│   └── cleanup-guide.md
│
├── frontend/
├── lambda/
├── prompts/
├── policies/
├── screenshots/
├── README.md
├── PROJECT_SUMMARY.md
├── INTERVIEW_GUIDE.md
└── LICENSE
```

---

# 📚 Project Documentation

| Document | Description |
|----------|-------------|
| README.md | Project overview and architecture |
| PROJECT_SUMMARY.md | Executive summary |
| INTERVIEW_GUIDE.md | Interview questions and architecture discussion |
| docs/ | Detailed implementation of all project phases |
| architecture/decisions/ | Architecture Decision Records (ADRs) |
| troubleshooting.md | Common issues and resolutions |
| cleanup-guide.md | AWS resource cleanup steps |

---

## 🚀 Project Status

✅ **Completed**

- Phase 1 – Project Foundation & Storage
- Phase 2 – Secure Resume Upload
- Phase 3 – Authentication
- Phase 4 – Resume Processing
- Phase 5 – AI Resume Analysis
- Phase 6 – Web Client Integration
- Phase 7 – Portfolio Website Generation

The project is fully functional and demonstrates a complete end-to-end serverless workflow using AWS managed services.

# 🚀 Implementation Journey

The application was built incrementally across seven implementation phases, with each phase introducing a new cloud capability while maintaining a modular, secure, and event-driven architecture.

| Phase | Focus | Documentation |
|------|-------|---------------|
| 1 | Project Foundation & Storage | [View Guide](docs/phase-01-project-foundation.md) |
| 2 | Secure Resume Upload | [View Guide](docs/phase-02-secure-upload.md) |
| 3 | User Authentication | [View Guide](docs/phase-03-authentication.md) |
| 4 | Resume Processing | [View Guide](docs/phase-04-resume-processing.md) |
| 5 | AI Resume Analysis | [View Guide](docs/phase-05-ai-resume-analysis.md) |
| 6 | Web Client Integration | [View Guide](docs/phase-06-web-client-integration.md) |
| 7 | Portfolio Website Generation | [View Guide](docs/phase-07-portfolio-generation.md) |

➡️ See the [`docs/`](docs/) directory for the complete implementation journey.

---

# 📊 Monitoring & Logging

The application uses Amazon CloudWatch for centralized monitoring and troubleshooting.

## Logging Strategy

| Service | Logs |
|----------|------|
| Upload URL Lambda | Upload URL generation |
| Resume Processor Lambda | Resume processing |
| AI Resume Analyzer Lambda | AI requests and responses |
| Portfolio Generator Lambda | Website generation |
| API Gateway | Request logs |
| CloudFront | Access logs (optional) |

### Operational Benefits

- Centralized logging
- Easier troubleshooting
- Faster root cause analysis
- Improved operational visibility

---

# 💰 Cost Optimization

The solution was designed using managed, serverless AWS services to minimize operational costs.

## Cost Optimization Techniques

- AWS Lambda scales automatically with demand
- Amazon S3 charges only for stored data
- CloudFront caches static content globally
- No EC2 instances to manage
- No always-on infrastructure
- Event-driven processing eliminates idle resources

### Why Serverless?

- Pay only when functions execute
- Automatic scaling
- Reduced operational overhead
- High availability by default

---

# 🏛️ AWS Well-Architected Framework

This project aligns with the six pillars of the AWS Well-Architected Framework.

| Pillar | Implementation |
|----------|----------------|
| Operational Excellence | Modular Lambda functions, documentation, CloudWatch logging |
| Security | Amazon Cognito, IAM, JWT authentication, private S3 buckets |
| Reliability | Event-driven processing with Amazon S3 triggers |
| Performance Efficiency | Serverless architecture with CloudFront caching |
| Cost Optimization | Pay-per-use services with no idle infrastructure |
| Sustainability | Fully managed AWS services with automatic scaling |

---

# 🎓 Lessons Learned

Building this project provided hands-on experience with designing and operating cloud-native applications.

### Key Takeaways

- Event-driven architectures simplify application workflows.
- Amazon S3 integrates seamlessly with serverless services.
- Presigned URLs provide a secure method for browser-based uploads.
- Amazon Textract significantly reduces document processing effort.
- Amazon Bedrock enables rapid AI integration without managing ML infrastructure.
- Separating AI processing from presentation logic improves maintainability.
- CloudFront enhances website performance through global edge caching.
- Good documentation is just as important as good code.

---

# ⚠️ Challenges & Solutions

| Challenge | Solution |
|-----------|----------|
| Secure file uploads | Implemented Amazon S3 Presigned URLs |
| PDF text extraction | Integrated Amazon Textract |
| AI output consistency | Improved prompts and standardized JSON structure |
| Portfolio generation | Used reusable Jinja2 templates |
| Secure API access | Protected endpoints with Amazon Cognito and JWT |
| Static website delivery | Hosted on Amazon S3 with Amazon CloudFront |

---

# 🧹 Resource Cleanup

To avoid unnecessary AWS charges, resources should be removed after completing the project.

### Recommended Cleanup Order

```text
Disable CloudFront Distribution
        │
        ▼
Remove Amazon S3 Event Notifications
        │
        ▼
Delete Lambda Functions
        │
        ▼
Delete Lambda Layers
        │
        ▼
Empty Amazon S3 Buckets
        │
        ▼
Delete Amazon S3 Buckets
        │
        ▼
Delete API Gateway
        │
        ▼
Delete Amazon Cognito User Pool
        │
        ▼
Delete IAM Roles and Policies
        │
        ▼
Delete CloudWatch Log Groups
```

> 📌 Capture screenshots before deleting AWS resources if you plan to use them in your portfolio.

---

# 🚀 Future Enhancements

Potential enhancements for future iterations include:

- Infrastructure as Code using Terraform
- CI/CD pipeline with GitHub Actions
- Custom domain using Amazon Route 53
- HTTPS certificates with AWS Certificate Manager
- Multiple portfolio themes
- Contact form integration
- DynamoDB for user metadata
- Analytics dashboard for portfolio visits

---

# 🙏 Acknowledgements

This project was inspired by the **AI Resume Builder** project shared by **Rajesh** from **IaaS Academy**.

Thank you to Rajesh and the IaaS Academy team for creating and sharing this valuable learning project with the community. This repository represents my personal implementation, enhancements, and learning journey while exploring AWS serverless services and Generative AI.

Original project:
https://github.com/iaasacademy/ai-resume-builder-aws

---


# ⭐ Support

If you found this repository helpful, consider giving it a ⭐ on GitHub.

Feedback, suggestions, and contributions are always welcome.

Happy Cloud Learning! ☁️

---


## 🔗 Continue Exploring

🏠 [AWS Cloud Engineering Portfolio](../README.md)

✨ [Serverless AI CV Enhancer](../serverless-ai-cv-enhancer)

📸 [Event-Driven Image Processing](../aws-event-driven-image-processing)

🔄 [Serverless CRUD API](../serverless-dynamodb-crud-api)