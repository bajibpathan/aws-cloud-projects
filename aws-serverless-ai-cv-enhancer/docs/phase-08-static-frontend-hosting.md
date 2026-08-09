# Phase 8 – Static Frontend Hosting on Amazon S3

## Overview

In this phase, a browser-based user interface was added to the Serverless AI CV Enhancer application.

Until this point, the application could only be tested using local scripts or API requests. By introducing a static frontend hosted on Amazon S3, users can now interact with the application through a web browser.

The frontend communicates with Amazon API Gateway, which invokes the AWS Lambda backend. The backend enhances resume content using Amazon Bedrock and stores enhancement history in Amazon DynamoDB.

This phase transforms the project into a complete end-to-end serverless application.

---

# Objectives

- Build a browser-based user interface
- Integrate the frontend with the existing REST API
- Host the frontend using Amazon S3 Static Website Hosting
- Configure CORS for browser communication
- Display AI-enhanced resume bullets
- Display previous enhancement history
- Keep the frontend lightweight using HTML, CSS, and JavaScript

---

# Architecture

## Before Phase 8

```text
Client
   │
   ▼
API Gateway
   │
   ▼
Lambda
   ├── Amazon Bedrock
   └── Amazon DynamoDB
```

## After Phase 8

```text
                 User Browser
                      │
                      ▼
        Amazon S3 Static Website
                      │
                      ▼
             Amazon API Gateway
                      │
                      ▼
                 AWS Lambda
                 │         │
                 ▼         ▼
        Amazon Bedrock  Amazon DynamoDB
```

---

# AWS Services Used

| Service | Purpose |
|----------|---------|
| Amazon S3 | Static website hosting |
| Amazon API Gateway | REST API |
| AWS Lambda | Backend logic |
| Amazon Bedrock | Resume enhancement |
| Amazon DynamoDB | Enhancement history |
| AWS IAM | Secure permissions |

---

# Frontend Structure

```text
frontend/
├── index.html
├── styles.css
└── app.js
```

| File | Purpose |
|------|---------|
| index.html | Application layout |
| styles.css | Styling |
| app.js | API communication and UI logic |

---

# User Workflow

```text
User enters

• Job Description
• Resume Bullets

        │

        ▼

POST /enhance

        │

        ▼

Amazon API Gateway

        │

        ▼

AWS Lambda

        │

        ▼

Amazon Bedrock

        │

        ▼

Enhanced Resume

        │

        ▼

Saved to DynamoDB

        │

        ▼

Displayed in Browser

        │

        ▼

GET /history

        │

        ▼

Display Previous Enhancements
```

---

# Browser Features

The frontend provides:

- Resume enhancement form
- Input validation
- Loading messages
- Error handling
- Enhanced resume display
- Enhancement history
- Refresh history button

---

# S3 Static Website Hosting

The frontend is hosted using Amazon S3 Static Website Hosting.

Benefits:

- Serverless
- Low cost
- Easy deployment
- No server management

---

# CORS Configuration

Amazon API Gateway was configured to allow requests from:

```text
http://localhost:8080

http://<bucket-name>.s3-website.ca-central-1.amazonaws.com
```

Allowed Methods:

- GET
- POST
- OPTIONS

Allowed Headers:

```text
content-type
```

---

# Deployment

Frontend deployment:

```text
Developer

      │

      ▼

aws s3 sync

      │

      ▼

Amazon S3 Bucket

      │

      ▼

Static Website Endpoint
```

---

# Testing

The following scenarios were verified.

| Test | Status |
|------|--------|
| Local frontend | ✅ |
| POST /enhance | ✅ |
| GET /history | ✅ |
| Amazon Bedrock integration | ✅ |
| DynamoDB history | ✅ |
| Browser CORS | ✅ |
| S3 static website | ✅ |

---

# Screenshots

```text
screenshots/
└── phase-08/
    ├── phase-08-local-frontend.png
    ├── phase-08-s3-static-website.png
    ├── phase-08-enhance-success.png
    ├── phase-08-history-ui.png
    └── phase-08-browser-network.png
```

---

# Lessons Learned

- Static websites can be hosted entirely on Amazon S3.
- API Gateway requires proper CORS configuration for browser clients.
- Separating HTML, CSS, and JavaScript improves maintainability.
- Browser-based testing provides a more realistic user experience.
- A lightweight frontend is sufficient for small serverless applications.

---

# Deliverables

- Browser UI
- S3 static website
- API integration
- History page
- CORS configuration
- End-to-end application

---

# Next Phase

**Phase 9 – Observability, Security Hardening & Production Readiness**

The final phase will focus on:

- CloudWatch structured logging
- Improved security
- Error handling improvements
- Final documentation
- Architecture diagrams
- Final project review