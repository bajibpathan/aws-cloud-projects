# Phase 06 – Web Client Integration

## Overview

In this phase, a browser-based frontend was integrated with the backend services built in the previous phases. The frontend allows authenticated users to securely upload resume files without exposing AWS credentials or making the Amazon S3 bucket public.

The implementation uses Amazon Cognito for user authentication, Amazon API Gateway HTTP API with a JWT Authorizer for API protection, and Amazon S3 Presigned URLs for secure direct uploads.

This phase connects all previously implemented backend components into a complete end-to-end workflow.

---

# Objectives

The primary objectives of this phase were to:

* Build a simple browser-based user interface.
* Authenticate users using Amazon Cognito.
* Protect backend APIs using JWT authentication.
* Validate resume files before upload.
* Generate secure Amazon S3 Presigned URLs.
* Upload resumes directly from the browser to Amazon S3.
* Trigger the existing resume-processing pipeline after a successful upload.

---

# Architecture

```text
Browser
    │
    │ Login
    ▼
Amazon Cognito
    │
    │ Access Token
    ▼
API Gateway HTTP API
    │
    │ JWT Authorizer
    ▼
Upload URL Lambda
    │
    │ Presigned URL
    ▼
Browser
    │
    │ PUT Resume
    ▼
Amazon S3
    │
    ▼
Resume Processing Pipeline
```

---

# AWS Services Used

| Service              | Purpose                        |
| -------------------- | ------------------------------ |
| Amazon Cognito       | User authentication            |
| API Gateway HTTP API | Protected backend API          |
| JWT Authorizer       | Token validation               |
| AWS Lambda           | Generate Presigned URL         |
| Amazon S3            | Resume storage                 |
| Amazon Textract      | Resume text extraction         |
| Amazon Bedrock       | AI resume analysis             |
| Amazon CloudWatch    | Monitoring and troubleshooting |

---

# Frontend Components

The frontend was implemented using Vanilla JavaScript to keep the application lightweight.

```text
frontend/
├── index.html
├── style.css
└── app.js
```

## index.html

Responsible for:

* Login form
* Upload form
* Status messages
* Sign Out button

---

## style.css

Responsible for:

* Page layout
* Responsive design
* Form styling
* Success and error messages

---

## app.js

Responsible for:

* Cognito authentication
* Session management
* JWT token handling
* File validation
* HTTP API communication
* Direct S3 uploads
* Sign out functionality

---

# Authentication Flow

The application authenticates users using Amazon Cognito User Pools.

```text
User
 │
 ▼
Enter Username & Password
 │
 ▼
Amazon Cognito
 │
 ▼
Access Token
 │
 ▼
Session Storage
```

After successful authentication:

* Login form is hidden.
* Upload form is displayed.
* JWT tokens are stored in browser session storage.
* The Cognito Access Token is used when calling protected backend APIs.

---

# Secure Upload Flow

The upload process consists of two separate requests.

## Step 1 – Request Presigned URL

The frontend sends the following request:

```http
POST /upload-url
```

Headers

```http
Authorization: Bearer ACCESS_TOKEN
Content-Type: application/json
```

Request body

```json
{
  "filename": "resume.pdf",
  "contentType": "application/pdf",
  "fileSize": 2097152
}
```

The backend validates the request before generating a Presigned URL.

---

## Step 2 – Upload Resume

The frontend uploads the PDF directly to Amazon S3.

```text
Browser
    │
    ▼
Amazon S3
```

Request

```http
PUT PresignedURL
```

Headers

```http
Content-Type: application/pdf
```

Body

```text
PDF Resume
```

Because the upload is performed directly against Amazon S3, the file does not pass through API Gateway or Lambda.

---

# File Validation

The frontend validates:

* File selected
* PDF format
* Maximum file size (5 MB)

The backend also validates:

* Filename
* File type
* File size

Backend validation ensures that security does not depend on browser-side checks.

---

# Security Controls

The following controls were implemented during this phase.

* Amazon Cognito authentication
* JWT Authorizer
* Access Token authorization
* Private Amazon S3 bucket
* Short-lived Presigned URLs
* Backend file validation
* Filename sanitization
* Session-based authentication
* No AWS credentials in the frontend

---

# Testing Performed

The following scenarios were successfully tested.

| Test                                 | Result   |
| ------------------------------------ | -------- |
| Login using Cognito                  | ✅ Passed |
| Invalid login                        | ✅ Passed |
| JWT protected API                    | ✅ Passed |
| Generate Presigned URL               | ✅ Passed |
| Direct S3 upload                     | ✅ Passed |
| Resume stored in S3                  | ✅ Passed |
| Resume-processing pipeline triggered | ✅ Passed |
| Sign Out                             | ✅ Passed |

---

# Issues Encountered

## Request Field Name

Initially the frontend sent:

```json
{
  "fileName": "resume.pdf"
}
```

The Lambda function expected:

```json
{
  "filename": "resume.pdf"
}
```

The request body was updated to match the backend contract.

---

## Missing fileSize

The initial request body omitted the `fileSize` property.

Lambda returned:

```json
{
  "message": "A valid fileSize is required"
}
```

The request was updated to include:

```json
{
  "filename": "resume.pdf",
  "contentType": "application/pdf",
  "fileSize": 2097152
}
```

---

# Lessons Learned

During this phase, the following concepts were reinforced:

* Secure browser authentication using Amazon Cognito.
* Protecting APIs with JWT Authorizers.
* Direct browser uploads using Amazon S3 Presigned URLs.
* Importance of backend validation.
* Managing browser sessions securely.
* Configuring CORS for API Gateway and Amazon S3.
* Building scalable upload architectures without exposing AWS credentials.

---

# Outcome

At the end of this phase, the AI Resume Builder supports secure browser-based resume uploads.

Authenticated users can upload PDF resumes directly to a private Amazon S3 bucket, where the existing backend pipeline automatically performs resume processing and AI analysis.

This completes the end-to-end upload workflow and prepares the project for the next phase.

---

# Next Phase

**Phase 07 – Portfolio Website Generator**

The next phase will generate a professional portfolio website from the processed resume data, enabling users to publish and share their resumes through a modern web interface.
