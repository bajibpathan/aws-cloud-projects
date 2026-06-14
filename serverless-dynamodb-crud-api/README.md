# 🚀 Serverless CRUD API — AWS Lambda, API Gateway & DynamoDB

A beginner‑friendly, fully serverless CRUD API built using AWS Lambda, API Gateway, and DynamoDB.
This project is designed to help cloud learners understand how serverless applications work end‑to‑end — from architecture to deployment, testing, validation, and cleanup.

---

## 🚀 Project Overview

This project demonstrates how to build a simple, scalable, cost‑efficient CRUD API using AWS serverless services.
It walks through:

- Designing the architecture
- Creating IAM roles and policies
- Deploying Lambda, API Gateway, and DynamoDB
- Testing and validating the API
- Cleaning up resources
- Documenting architectural decisions (ADRs)
- Aligning with the AWS Well‑Architected Framework

It is ideal for beginners, students, and professionals building their first AWS serverless project.

---

## 🏗 Architecture

The system uses a lightweight serverless architecture:

- **API Gateway** exposes a REST endpoint
- **Lambda** handles CRUD logic
- **DynamoDB** stores items
- **IAM** secures access

![Architecture Diagram](./docs/diagrams/high-level-architecture.png)

---

## 🧩 Architecture Decision Records (ADRs)

ADRs help document *why* certain choices were made.

| ADR Number | Title                               | Description                                                   |
|------------|---------------------------------------|---------------------------------------------------------------|
| [0001](./docs/adr/0001-use-lambda-for-compute.md0001-use-lambda-for-compute.md)       | Use AWS Lambda for Compute            | Decision to use Lambda as the serverless compute layer.       |
| [0002](./docs/adr/0002-use-api-gateway-as-entrypoint.md)       | Use API Gateway as API Entry Point    | Decision to expose the API using Amazon API Gateway.          |
| [0003](./docs/adr/0003-use-dynamodb-as-database.md)       | Use DynamoDB as the Database          | Decision to store CRUD items in DynamoDB.                     |
| [0004](./docs/adr/0004-use-single-lambda-handler-pattern.md)       | Use Single Lambda Handler Pattern     | Decision to route all operations through one Lambda function. |
| [0005](./docs/adr/0005-use-least-privilege-iam-policy.md)       | Use Least‑Privilege IAM Policy        | Decision to create a custom IAM policy with minimal permissions. |

All ADRs are stored in:

👉 [ADR](docs/adr/README.md)

---

## 🧭 Alignment with the AWS Well‑Architected Framework

This project aligns with all six pillars:

- **Operational Excellence** → clear documentation, structured folder layout
- **Security** → least‑privilege IAM, controlled access
- **Reliability** → DynamoDB durability, Lambda availability
- **Performance Efficiency** → serverless, auto‑scaling
- **Cost Optimization** → pay‑per‑use model
- **Sustainability** → fully managed, energy‑efficient services

---

## 📦 Folder Structure

```text
.
├── docs/
│   ├── architecture/      # Simple architecture explanation + diagram
│   ├── deployment/        # Step-by-step deployment guide
│   ├── diagrams/          # Visual diagrams (architecture, flow, structure)
│   ├── adr/               # Architecture Decision Records
│   └── references/        # Learning resources used for this project
│
├── src/                   # Placeholder; source code lives in separate repo
│
├── scripts/               # Placeholder for future automation scripts
│
├── tests/                 # Placeholder for future tests
│
└── README.md              # Main project documentation

```

---

## 📄 Deployment Guide

A complete, beginner‑friendly deployment guide is available here:

👉 [Deployment Guide](docs/deployment/deployment-guide.md)


It includes:

- IAM policy creation
- IAM role setup
- Lambda deployment
- DynamoDB table creation
- API Gateway setup
- Testing Lambda & API

---
## 🧼 Clean‑up Instructions

To avoid unnecessary AWS charges, the cleanup guide explains how to delete:

- DynamoDB table
- Lambda function
- API Gateway API
- IAM role & policy

A full clean‑up guide is available here:

👉 [Clean‑up Instructions](docs/deployment/cleanup-guide.md)

---

## 📚 References

A list of AWS docs, tutorials, and tools that helped me learn is available in:

👉 [References](docs/references/README.md)

---

## 🎯 Why This Project Matters

This project helps to understand:

- How serverless applications work
- How AWS services integrate
- How to design and document cloud architectures
- How to deploy and test real AWS workloads
---

## 📊 Project Impact

This project demonstrates my ability to design, document, and deploy a simple AWS‑hosted website using professional engineering practices. It shows clear understanding of cloud fundamentals and structured project organization.

- Demonstrates real AWS service integration
- Provides hands‑on experience with serverless design
- Builds confidence in cloud fundamentals
- Helps learners understand IAM, API Gateway, Lambda, and DynamoDB

---

### 🛠 Technical Outcomes

- Built a fully serverless CRUD API
- Implemented least‑privilege IAM
- Deployed Lambda with API Gateway proxy integration
- Created DynamoDB table for persistent storage
- Validated API using Postman and cURL
- Documented architecture using ADRs

--- 

### 💡 Practical Value

This project provides organizations with a ready‑to‑use blueprint for building lightweight, cost‑efficient backend services. By adopting this serverless pattern, companies gain:

- **Lower operational overhead** → no servers to manage or scale.
- **Reduced costs** → pay only for actual usage with fully managed services.
- **Faster delivery** → teams can deploy new APIs quickly without infrastructure setup.
- **Stronger security** → least‑privilege IAM and isolated execution environments.
- **Reusable architecture** → a repeatable template for future microservices and internal tools.

It enables teams to move faster, spend less, and operate more securely, all while following modern cloud‑native best practices.

---
### 🎓 What I Learned

- How serverless components interact
- How to design simple cloud architectures
- How to write ADRs
- How to deploy and test AWS service
- How to follow AWS Well‑Architected best practices

---

## ⭐ Support
If you find these projects helpful or inspiring, feel free to star the repository.