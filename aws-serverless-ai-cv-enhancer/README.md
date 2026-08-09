<div align="center">

# 🤖 Serverless AI CV Enhancer

### Production-inspired Serverless Generative AI Application built with AWS

Enhance resume bullet points using **Amazon Bedrock**, **AWS Lambda**, **Amazon API Gateway**, and **Amazon DynamoDB**.

![AWS](https://img.shields.io/badge/AWS-Cloud-orange?logo=amazonaws)
![Amazon Bedrock](https://img.shields.io/badge/Amazon-Bedrock-purple)
![AWS Lambda](https://img.shields.io/badge/AWS-Lambda-FF9900?logo=awslambda)
![API Gateway](https://img.shields.io/badge/API-Gateway-2E73B8)
![Amazon DynamoDB](https://img.shields.io/badge/DynamoDB-4053D6)
![Amazon S3](https://img.shields.io/badge/Amazon-S3-569A31)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Serverless](https://img.shields.io/badge/Architecture-Serverless-success)

</div>

---

# 📖 Project Overview

Serverless AI CV Enhancer is a production-inspired serverless application that improves resume bullet points for a target job description using **Amazon Bedrock**.

The application accepts:

- A job description
- Existing resume bullet points

It then:

1. Validates the request
2. Builds a structured prompt
3. Invokes Amazon Bedrock
4. Returns enhanced resume bullet points
5. Stores enhancement history in Amazon DynamoDB
6. Displays previous enhancements through a browser-based frontend

The project was built to learn modern AWS serverless architecture, Generative AI integration, and cloud engineering best practices.

---

# 🏗️ Architecture

The application follows a fully managed serverless architecture using AWS services.

<p align="center">
    <img
        src="architecture/diagrams/00-high-level-architecture.png"
        alt="High-Level Architecture"
        width="900">
</p>

Additional architecture diagrams are available in:

```text
architecture/diagrams/
```

---

# ✨ Features

- AI-powered resume enhancement
- Amazon Bedrock integration
- Prompt engineering
- AWS Lambda backend
- Amazon API Gateway HTTP API
- Amazon DynamoDB enhancement history
- Amazon S3 static website hosting
- Browser-based frontend
- Structured logging
- AWS X-Ray tracing
- Input validation
- Production-style error handling

---

# ☁️ AWS Services

| Service | Purpose |
|----------|---------|
| AWS Lambda | Backend application logic |
| Amazon API Gateway | REST API |
| Amazon Bedrock | Resume enhancement |
| Amazon DynamoDB | Enhancement history |
| Amazon S3 | Static website hosting |
| Amazon CloudWatch | Logging and monitoring |
| AWS X-Ray | Distributed tracing |
| AWS IAM | Security and access control |

---

# 📸 Screenshots

The repository contains screenshots covering every implementation phase.

```text
screenshots/

├── phase-01/
├── phase-02/
├── phase-03/
├── phase-04/
├── phase-05/
├── phase-06/
├── phase-07/
├── phase-08/
└── phase-09/
```

Example screenshots include:

- Application UI
- Amazon Bedrock integration
- API Gateway
- DynamoDB
- CloudWatch logs
- AWS X-Ray
- IAM permissions
- Browser testing

---

# 🚀 Quick Start

Clone the repository:

```bash
git clone https://github.com/<your-github-username>/aws-serverless-ai-cv-enhancer.git

cd aws-serverless-ai-cv-enhancer
```

Configure AWS credentials:

```bash
aws configure
```

Run the local tests:

```bash
python3 lambda/enhance_resume/local_test.py
```

Run the frontend locally:

```bash
cd frontend

python3 -m http.server 8080
```

Open:

```text
http://localhost:8080
```

Update `frontend/config.js` with your API Gateway endpoint before testing.

---

# 📂 Repository Structure

```text
aws-serverless-ai-cv-enhancer/
│
├── README.md
├── TECHNICAL_OVERVIEW.md
├── INTERVIEW_GUIDE.md
│
├── architecture/
├── docs/
├── frontend/
├── lambda/
├── policies/
├── prompts/
├── sample-events/
└── screenshots/
```

---

# 📚 Documentation

| Document | Description |
|----------|-------------|
| `README.md` | Project overview and quick start |
| `TECHNICAL_OVERVIEW.md` | Executive technical summary |
| `INTERVIEW_GUIDE.md` | Beginner-friendly interview guide |
| `docs/` | Phase-by-phase implementation |
| `architecture/decisions/` | Architecture Decision Records (ADRs) |
| `lambda/enhance_resume/README.md` | Lambda implementation details |

---

# 🎯 Skills Demonstrated

This project demonstrates practical experience with:

- AWS Lambda
- Amazon Bedrock
- Amazon API Gateway
- Amazon DynamoDB
- Amazon S3
- CloudWatch
- AWS X-Ray
- IAM
- Serverless Architecture
- REST APIs
- Prompt Engineering
- Python
- Git & GitHub

---

# 🙏 Acknowledgement

This project was inspired by the **Serverless AI CV Enhancer** concept shared by **Lefteris Karageorgiou**.

This repository is **my own implementation**, built from scratch as a hands-on learning and portfolio project. Every implementation phase, architecture diagram, documentation page, Architecture Decision Record (ADR), and testing workflow was created as part of my journey to learn AWS Serverless technologies and Amazon Bedrock.

Special thanks to **Lefteris Karageorgiou** for creating educational cloud content that inspired this project.

---

# 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for the complete license terms.

This repository is intended for:

- Learning
- Portfolio development
- AWS Serverless practice
- Generative AI experimentation

Feel free to fork this repository for your own learning, experimentation, and skill development.

If you build upon this project, please provide appropriate attribution and create your own implementation rather than copying the repository as-is.

---

<div align="center">

### ⭐ If you found this repository useful, consider giving it a star!

Happy Learning! 🚀

</div>