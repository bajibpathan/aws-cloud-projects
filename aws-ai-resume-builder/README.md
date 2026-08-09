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

## 🎯 Learning Objectives

This project demonstrates how to:

- Build a complete event-driven serverless application
- Secure applications using Amazon Cognito and IAM
- Upload files securely using Amazon S3 Presigned URLs
- Process documents using Amazon Textract
- Integrate Generative AI using Amazon Bedrock
- Generate static portfolio websites automatically
- Apply AWS Well-Architected Framework principles
- Document architecture using Architecture Decision Records (ADRs)

---

# ✨ Key Features

### User Features

- Secure user authentication
- Resume upload through a web interface
- Direct S3 uploads using Presigned URLs
- Automatic resume processing
- AI-powered resume enhancement
- Responsive portfolio website generation
- Global website delivery using CloudFront

### Cloud Engineering Features

- Event-driven architecture
- Fully serverless design
- Modular Lambda functions
- Least-privilege IAM permissions
- Private S3 buckets
- Structured CloudWatch logging
- Jinja2 template engine
- Production-style documentation
- Architecture Decision Records (ADRs)

---

# 🏗️ Solution Architecture

<p align="center">
  <img src="architecture/images/aws-ai-resume-builder-architecture.png"
       alt="AWS AI Resume Builder Architecture"
       width="100%">
</p>

The application follows an event-driven serverless architecture. Resume uploads trigger independent processing stages through Amazon S3 events, allowing components to remain loosely coupled, scalable, and independently maintainable.

---

# 🔄 Application Workflow

<p align="center">
  <img src="architecture/images/aws-ai-resume-builder-high-level-workflow.png"
       alt="AWS AI Resume Builder Application Workflow"
       width="100%">
</p>

The workflow illustrates the end-to-end resume processing pipeline, from secure user authentication and resume upload through document extraction, AI analysis, and portfolio generation.

---

# ☁️ AWS Services Used

| AWS Service | Purpose |
|-------------|---------|
| AWS Lambda | Serverless compute for business logic |
| Amazon API Gateway | Secure REST API endpoints |
| Amazon S3 | Resume storage, processed data, and portfolio hosting |
| Amazon Cognito | User authentication and authorization |
| Amazon Textract | Extract structured text from PDF resumes |
| Amazon Bedrock | AI-powered resume analysis and content generation |
| Amazon CloudFront | Global delivery of generated portfolio websites |
| Amazon CloudWatch | Logging and operational monitoring |
| AWS IAM | Identity and access management |

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


# 🎯 What This Project Demonstrates

This project showcases practical experience with modern AWS cloud engineering and AI services through a production-style implementation.

### AWS Services

- Amazon S3
- AWS Lambda
- Amazon API Gateway
- Amazon Cognito
- Amazon Textract
- Amazon Bedrock
- Amazon CloudFront
- AWS IAM
- Amazon CloudWatch

### Cloud Engineering Skills

- Serverless Architecture
- Event-Driven Design
- REST API Development
- Authentication & Authorization
- AI Integration
- Static Website Hosting
- Secure File Upload
- IAM Security
- Monitoring & Logging
- Production Documentation

# 🔒 Security Architecture

Security was a core consideration throughout the project. The application follows AWS security best practices to protect user data, control access, and minimize the attack surface.

## Security Controls

| Area | Implementation |
|------|----------------|
| Authentication | Amazon Cognito User Pools |
| Authorization | JWT validation using API Gateway |
| Identity & Access | Least-Privilege IAM Roles |
| File Upload | Amazon S3 Presigned URLs |
| Data Storage | Private Amazon S3 Buckets |
| Transport Security | HTTPS/TLS |
| Public Access | Blocked on all S3 buckets |
| Secrets | No hardcoded credentials |

### Security Highlights

- User authentication managed by Amazon Cognito
- Direct browser-to-S3 uploads using temporary presigned URLs
- IAM roles grant only the minimum required permissions
- Private S3 buckets with Block Public Access enabled
- API endpoints protected using JWT authentication
- Server-side encryption supported for stored data

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

# 📚 Repository Documentation

| Document | Description |
|----------|-------------|
| README.md | Project overview |
| PROJECT_SUMMARY.md | Executive summary |
| INTERVIEW_GUIDE.md | Interview preparation |
| docs/ | Detailed implementation guide |
| architecture/ | Architecture diagrams and ADRs |
| troubleshooting.md | Common issues and resolutions |
| cleanup-guide.md | Resource cleanup instructions |

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

# 🏆 Skills Demonstrated

## AWS Services

- Amazon S3
- AWS Lambda
- Amazon API Gateway
- Amazon Cognito
- Amazon Textract
- Amazon Bedrock
- Amazon CloudFront
- AWS IAM
- Amazon CloudWatch

## Cloud Engineering

- Serverless Architecture
- Event-Driven Design
- REST APIs
- Authentication & Authorization
- Secure File Upload
- AI Integration
- Static Website Hosting
- Logging & Monitoring
- Cost Optimization
- Documentation

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