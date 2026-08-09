# 📂 Repository Structure

![AWS](https://img.shields.io/badge/AWS-Repository%20Structure-FF9900?logo=amazonaws&logoColor=white)
![Portfolio](https://img.shields.io/badge/Portfolio-Documentation-blueviolet)

This document explains how the AWS Cloud Engineering Portfolio is organized and the purpose of each directory.

The repository is designed to provide a consistent structure across all projects, making it easy to navigate, maintain, and extend as new cloud engineering projects are added.

---

# 🎯 Purpose

The repository structure follows a documentation-first approach.

Every project aims to include:

- Clear project documentation
- Architecture diagrams
- Architecture Decision Records (ADRs)
- Technical implementation guides
- Interview preparation material
- Supporting assets and screenshots

A consistent structure helps readers quickly locate information and makes future projects easier to maintain.

---

# 🏗️ Repository Overview

```text
aws-cloud-projects/

├── README.md                     # Portfolio homepage
├── LICENSE
│
├── assets/                       # Shared portfolio assets
│   ├── banner.png
│   ├── architecture/
│   ├── branding/
│   ├── icons/
│   └── thumbnails/
│
├── docs/                         # Portfolio reference documentation
│   ├── AWS_SERVICES.md
│   ├── CLOUD_SKILLS.md
│   ├── ENGINEERING_PRINCIPLES.md
│   ├── LEARNING_ROADMAP.md
│   └── REPOSITORY_STRUCTURE.md
│
├── templates/                    # Reusable documentation templates
│   ├── README_TEMPLATE.md
│   ├── TECHNICAL_OVERVIEW_TEMPLATE.md
│   ├── INTERVIEW_GUIDE_TEMPLATE.md
│   ├── PROJECT_STRUCTURE_TEMPLATE.md
│   └── PROJECT_CHECKLIST.md
│
├── aws-ai-resume-builder/
├── serverless-ai-cv-enhancer/
├── aws-event-driven-image-processing/
├── serverless-dynamodb-crud-api/
├── aws-lambda-execution-profiler/
├── static-website-hosting-on-amazon-s3/
│
└── future-projects...
```

---

# 📁 Directory Guide

## 📄 Root Directory

Contains the portfolio homepage, licensing information, and top-level project folders.

---

## 🎨 assets/

Stores shared assets used across the portfolio.

Examples include:

- Portfolio banner
- Architecture thumbnails
- Shared icons
- Branding assets

---

## 📚 docs/

Contains portfolio-level documentation that applies across multiple projects.

Examples include:

- AWS service reference
- Cloud engineering skills
- Engineering principles
- Learning roadmap
- Repository documentation

---

## 📝 templates/

Reusable templates that standardize documentation across every project.

Templates include:

- README
- Technical Overview
- Interview Guide
- Repository Structure
- Project Completion Checklist

---

## 🚀 Project Directories

Each project is maintained in its own folder.

Projects follow a consistent documentation standard while remaining independent and self-contained.

Typical project contents include:

- README
- Architecture diagrams
- Architecture Decision Records (ADRs)
- Technical documentation
- Interview guide
- Source code
- Screenshots

---

# 📐 Project Structure Standard

Every project follows this structure where applicable.

```text
project-name/

├── README.md
├── PROJECT_SUMMARY.md
├── TECHNICAL_OVERVIEW.md
├── INTERVIEW_GUIDE.md
├── LICENSE
│
├── architecture/
│   ├── decisions/
│   └── images/
│
├── docs/
│
├── src/
│
├── screenshots/
│
├── policies/
│
├── sample-events/
│
└── assets/
```

Not every project requires every folder.

Only directories relevant to the project's architecture are included.

---

# 🎯 Repository Design Principles

The repository is organized around the following principles:

- Consistent documentation across all projects
- Modular project organization
- Reusable documentation templates
- Clear separation of portfolio-level and project-level documentation
- Documentation-first approach
- Easy navigation and maintainability
- Scalability for future projects

---

# 🚀 Future Growth

As additional AWS projects are completed, new project folders will be added while continuing to follow the same repository structure and documentation standards.

This approach ensures consistency as the portfolio expands to include Infrastructure as Code, containers, Kubernetes, CI/CD, networking, and advanced cloud architectures.

---

# 🎯 Key Takeaway

A well-organized repository improves maintainability, readability, and discoverability.

By following consistent documentation standards and project structures, this portfolio is designed to grow into a comprehensive cloud engineering knowledge base while remaining easy to navigate and maintain.