# Interview Guide

## Introduction

This guide contains common interview questions and sample answers based on the **Serverless AI CV Enhancer** project.

The answers are intentionally concise and focus on explaining the project clearly rather than demonstrating deep AWS theory.

---

# Project Overview

## 1. Tell me about this project.

The Serverless AI CV Enhancer is a production-inspired Generative AI application built on AWS. It allows users to submit a target job description and their existing resume bullet points. The application validates the request, builds a structured prompt, invokes Amazon Bedrock to enhance the content, stores the enhancement history in DynamoDB, and returns the improved resume bullets through a browser-based frontend.

---

# Architecture

## 2. Can you walk me through the architecture?

The frontend is hosted on Amazon S3 and communicates with Amazon API Gateway through HTTP APIs. API Gateway invokes an AWS Lambda function that validates the request, generates the prompt, calls Amazon Bedrock, stores the enhancement history in DynamoDB, and returns the response. CloudWatch captures logs, while AWS X-Ray provides request tracing.

---

## 3. Why did you choose a serverless architecture?

A serverless architecture eliminates server management, automatically scales based on demand, and follows a pay-per-use pricing model. It allowed me to focus on building the application logic rather than managing infrastructure.

---

# AWS Lambda

## 4. What is the role of Lambda in this project?

Lambda is the application's backend. It validates incoming requests, builds prompts, invokes Amazon Bedrock, stores enhancement history in DynamoDB, and formats API responses.

---

## 5. How did you organize the Lambda code?

The Lambda function follows a modular structure with separate modules for validation, response handling, configuration, prompt generation, and AWS service integrations. This keeps the code easier to maintain and test.

---

# Amazon Bedrock

## 6. Why did you use Amazon Bedrock?

Amazon Bedrock provides access to foundation models without managing AI infrastructure. It allowed me to integrate Generative AI into the application using AWS-managed services.

---

## 7. What is prompt engineering, and how did you use it?

Instead of building prompts directly inside the Lambda function, I stored the prompt template separately and generated prompts dynamically. This makes prompt updates easier without changing the application logic.

---

# Amazon DynamoDB

## 8. Why did you choose DynamoDB?

The application stores enhancement history using DynamoDB because it is fully managed, serverless, highly scalable, and integrates well with Lambda.

---

## 9. What information is stored in DynamoDB?

Each enhancement stores:

- Enhancement ID
- Timestamp
- Job description
- Original resume bullets
- Enhanced resume bullets
- Prompt version
- Model identifier

---

# API Gateway

## 10. Why did you use API Gateway?

API Gateway exposes secure HTTP endpoints for the frontend and routes requests to the Lambda function. It also handles CORS configuration for browser access.

---

# Security

## 11. How did you secure the application?

The application validates all requests before invoking Amazon Bedrock, uses least-privilege IAM permissions, stores configuration in environment variables, restricts CORS, and avoids logging sensitive resume content.

---

# Observability

## 12. How did you monitor the application?

Amazon CloudWatch captures application logs and runtime information, while AWS X-Ray provides request tracing to help understand request flow and troubleshoot issues.

---

# Testing

## 13. How did you test the application?

I performed local testing using a dedicated test script, validated different request scenarios, tested API Gateway integration, verified DynamoDB persistence, and tested the complete application through the browser frontend.

---

# Lessons Learned

## 14. What was the biggest challenge?

One of the biggest challenges was integrating Amazon Bedrock correctly, particularly understanding inference profiles and structuring prompts to produce consistent results. It also reinforced the importance of modular code and thorough testing.

---

# Future Improvements

## 15. What would you improve if this were a production application?

Potential improvements include:

- Amazon Cognito authentication
- CloudFront with HTTPS
- Custom domain using Route 53
- CI/CD pipeline using GitHub Actions
- Infrastructure as Code using Terraform or AWS SAM
- Pagination for enhancement history
- Enhanced monitoring dashboards and alarms

---

# Key Technologies

- AWS Lambda
- Amazon API Gateway
- Amazon Bedrock
- Amazon DynamoDB
- Amazon S3
- Amazon CloudWatch
- AWS X-Ray
- AWS IAM
- Python

---

# Interview Tips

When discussing this project:

- Explain the overall architecture before diving into AWS services.
- Focus on why each AWS service was selected.
- Describe the request flow from the frontend to the AI response.
- Highlight the security, observability, and testing practices you implemented.
- Be honest about the project being a learning exercise while emphasizing the production-inspired design principles.