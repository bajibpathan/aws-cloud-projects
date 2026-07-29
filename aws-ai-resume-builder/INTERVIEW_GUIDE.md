# INTERVIEW GUIDE

This guide contains common interview questions based on the AWS AI Resume Builder project. The answers are intentionally short and focus on the implementation used in this project.

---

# Project Overview

### Tell me about this project.

This is a serverless AWS application that converts a resume into a professional portfolio website using Amazon Textract, Amazon Bedrock, AWS Lambda, Amazon S3, and CloudFront.

### Why did you build this project?

To gain hands-on experience building a real-world serverless application using AWS managed services and Generative AI.

### Why serverless?

The application only processes resumes when users upload them, so serverless reduces infrastructure management and scales automatically.

### Which AWS services did you use?

- Amazon Cognito
- API Gateway
- AWS Lambda
- Amazon S3
- Amazon Textract
- Amazon Bedrock
- CloudFront
- IAM
- CloudWatch

### What was the biggest challenge?

Integrating multiple AWS services securely and troubleshooting IAM permissions during development.

---

# Amazon S3

### Why did you use Amazon S3?

To store uploaded resumes, generated portfolio websites, and frontend assets.

### Why multiple buckets?

To separate resumes, generated websites, and frontend files, making permissions and management simpler.

### Why Presigned URLs?

To allow direct browser uploads without exposing AWS credentials.

### Why not upload through Lambda?

Direct uploads reduce Lambda execution time, improve performance, and lower costs.

### What triggers the processing workflow?

An S3 ObjectCreated event triggers the resume processing Lambda function.

### Why enable Versioning?

To protect files from accidental deletion or overwrites.

### How is S3 secured?

Buckets are private, uploads use Presigned URLs, and access is controlled through IAM.

---

# AWS Lambda

### Why Lambda?

To run the application logic without managing servers.

### Why multiple Lambda functions?

Each function has a single responsibility, making the application easier to maintain.

### How are Lambda functions triggered?

By API Gateway for APIs and S3 Event Notifications for resume processing.

### Why not EC2?

The workload is event-driven, so Lambda is simpler and more cost-effective.

### What happens if Lambda fails?

Errors are logged in CloudWatch. In production, retries or DLQs can be added.

### What would you improve?

I'd use AWS Step Functions to orchestrate the workflow and improve error handling.

---

# API Gateway

### Why API Gateway?

To securely expose Lambda functions as REST APIs.

### Why not invoke Lambda directly?

API Gateway provides authentication, request validation, throttling, and a single API endpoint.

### How is the API secured?

Amazon Cognito authorizers validate authenticated users before invoking Lambda.

### Which APIs were implemented?

- Generate Presigned URL
- Resume Processing
- Portfolio Generation (if applicable)

---

# Amazon Cognito

### Why Cognito?

To authenticate users without building a custom authentication system.

### Why not build your own login system?

Cognito is more secure, scalable, and integrates well with AWS services.

### What authentication flow did you use?

User Pool authentication.

### What happens after login?

The frontend receives authentication tokens and uses them to call protected APIs.

---

# Amazon Textract

### Why Textract?

To extract text from uploaded resumes automatically.

### Why Textract instead of OCR libraries?

Textract is fully managed and works well with PDFs and scanned documents.

### What output does Textract produce?

Structured text that is passed to Amazon Bedrock.

### What file formats are supported?

PDFs and image formats such as PNG and JPEG.

---

# Amazon Bedrock

### Why Bedrock?

To analyze resume content and generate structured information using an LLM.

### Which model did you use?

Claude Sonnet (or the model used in your implementation).

### Why return JSON?

JSON is easier for Lambda to process when generating HTML.

### What challenge did you face?

Configuring the correct inference profile and prompt engineering.

### What would you improve?

Validate AI responses before generating the portfolio.

---

# CloudFront

### Why CloudFront?

To deliver generated portfolio websites with lower latency.

### Why not access S3 directly?

CloudFront improves performance and adds another security layer.

### How is content updated?

When new files are uploaded to S3, CloudFront serves the latest content after cache refresh or invalidation.

---

# IAM

### Why IAM?

To provide least-privilege permissions between AWS services.

### Which IAM roles did you create?

- Lambda Execution Role
- Textract Access
- Bedrock Access
- S3 Access

### Biggest IAM issue?

Missing permissions while integrating AWS services.

### How did you troubleshoot?

Using CloudWatch logs and IAM policy reviews.

---

# CloudWatch

### Why CloudWatch?

To monitor Lambda execution and troubleshoot errors.

### What did you monitor?

- Lambda Logs
- Execution Errors
- Request Flow

### Why is CloudWatch important?

It helps identify failures and debug the application quickly.

---

# Architecture

### Why event-driven?

Each AWS service reacts to events instead of continuously polling.

### Why separate Lambda functions?

Single Responsibility Principle.

### Why use managed services?

Less infrastructure management and better scalability.

### Which AWS service is central to the workflow?

Amazon S3, because it starts the resume processing pipeline.

### What architectural pattern did you use?

Serverless Event-Driven Architecture.

### What would you change for production?

Use Step Functions, SQS, CI/CD, WAF, and better monitoring.

---

# Security

### How is the application secured?

Amazon Cognito, IAM roles, private S3 buckets, and Presigned URLs.

### How are uploads protected?

Temporary Presigned URLs.

### How is AWS access controlled?

IAM roles with least privilege.

### Are S3 buckets public?

No.

### How would you improve security?

Add WAF, GuardDuty, encryption, Secrets Manager, and security monitoring.

---

# Troubleshooting

### What was the most difficult issue?

IAM permission errors while integrating Textract and Bedrock.

### How did you debug Lambda failures?

CloudWatch Logs.

### How did you verify S3 events?

CloudWatch Logs and Event Notifications.

### How did you troubleshoot Bedrock?

Verified model access, inference profile, IAM permissions, and prompt format.

### How did you troubleshoot Textract?

Verified supported file formats, S3 permissions, and API responses.

### Biggest lesson learned?

Most integration issues were caused by missing IAM permissions or incorrect service configuration.

---

# Production Improvements

### What would you improve?

- AWS Step Functions
- Amazon SQS
- CI/CD Pipeline
- CloudFormation/Terraform
- AWS WAF
- Dead Letter Queues
- Better Monitoring
- Cost Optimization