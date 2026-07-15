# 🎤 AWS Event-Driven Image Processing - Interview Guide

## Overview

This document summarizes the design decisions, AWS services, implementation details, and common interview questions related to the **AWS Event-Driven Image Processing** project.

It serves as a quick reference when preparing for cloud engineering and AWS interviews.

---

# 📖 Project Summary

The project demonstrates how to build a production-inspired serverless application using AWS managed services.

When an image is uploaded to Amazon S3, an ObjectCreated event automatically invokes an AWS Lambda function. The function validates the uploaded image, generates a deterministic ImageId, prevents duplicate processing, stores metadata in Amazon DynamoDB, and publishes logs and metrics to Amazon CloudWatch.

The project also demonstrates operational excellence through documentation, monitoring, reliability improvements, and cost optimization.

---

# 🏗 Architecture

![AWS Event-Driven Image Processing](architecture/images/01-high-level-architecture.png)


---

# ☁ AWS Services

| Service | Purpose |
|----------|---------|
| Amazon S3 | Store uploaded images |
| AWS Lambda | Process image uploads |
| Amazon DynamoDB | Store image metadata |
| Amazon CloudWatch | Logs, Metrics, Dashboard, Alarm |
| AWS IAM | Least-Privilege Security |

---

# 🎯 Interview Questions

## Q1. Can you explain your project?

### Answer

This project demonstrates an event-driven serverless architecture.

When a user uploads an image to Amazon S3, an ObjectCreated event triggers an AWS Lambda function. The Lambda validates the image, generates a deterministic ImageId, prevents duplicate processing, stores metadata in Amazon DynamoDB, and publishes operational logs to Amazon CloudWatch.

The project also includes structured documentation, monitoring, reliability improvements, and cost optimization.

---

## Q2. Why did you choose Amazon S3?

### Answer

Amazon S3 provides:

- Highly durable object storage
- Automatic scalability
- Native Lambda integration
- Versioning
- Server-side encryption
- Event Notifications

Since the application stores images rather than block storage, Amazon S3 was the most appropriate choice.

---

## Q3. Why Lambda instead of EC2?

### Answer

The workload is event-driven and unpredictable.

Lambda automatically scales, requires no server management, integrates directly with Amazon S3, and follows a pay-for-use pricing model.

Using EC2 would introduce unnecessary infrastructure management and continuous compute costs.

---

## Q4. Why DynamoDB instead of Amazon RDS?

### Answer

The application stores simple image metadata.

There are no joins or complex relational queries.

DynamoDB provides:

- Serverless operation
- Automatic scaling
- Low latency
- Native Lambda integration

This makes it an ideal choice for metadata storage.

---

## Q5. Why CloudWatch?

### Answer

CloudWatch integrates natively with AWS services.

It automatically collects Lambda metrics and logs while supporting dashboards and alarms without requiring additional infrastructure.

---

## Q6. What is idempotent processing?

### Answer

Amazon S3 Event Notifications provide at-least-once delivery.

Duplicate events may occur.

To prevent duplicate metadata records, the application generates a deterministic ImageId and performs a DynamoDB conditional write.

If the ImageId already exists, the duplicate event is ignored.

---

## Q7. What reliability improvements did you implement?

### Answer

The project includes:

- File validation
- Duplicate protection
- Idempotent processing
- Conditional writes
- Structured logging
- Exception handling
- Processing status tracking

---

## Q8. How is the application monitored?

### Answer

The application uses Amazon CloudWatch for:

- Logs
- Metrics
- Dashboard
- Alarm

Structured logging improves troubleshooting and operational visibility.

---

## Q9. What security best practices were implemented?

### Answer

- IAM Least Privilege
- Server-Side Encryption
- Bucket Owner Enforced Object Ownership
- File Validation
- Controlled Error Responses
- Public Access Blocked

---

## Q10. How did you optimize costs?

### Answer

The project minimizes cost by using:

- Serverless architecture
- On-Demand DynamoDB
- Prefix filtering
- Structured logging
- CloudWatch log retention
- Resource cleanup procedures

---

# 🚀 Possible Future Improvements

For a production implementation, I would consider adding:

- Amazon SQS
- Dead Letter Queue (DLQ)
- Amazon EventBridge
- AWS Step Functions
- AWS X-Ray
- CI/CD Pipeline
- Infrastructure as Code (Terraform)
- Image processing (thumbnail generation)
- Automated testing

---

# 📚 Key Lessons Learned

Working on this project strengthened my understanding of:

- Event-Driven Architecture
- Serverless Computing
- Cloud Security
- Observability
- Reliability Engineering
- Cost Optimization
- AWS Well-Architected Framework
- Technical Documentation

---

# 💡 Interview Tip

When discussing this project, focus not only on the AWS services used but also on the engineering decisions behind the solution.

Explain:

- Why each service was selected.
- What alternatives were considered.
- How reliability was improved.
- How costs were controlled.
- What you would change for a production-scale implementation.

Interviewers are often more interested in your reasoning than in your ability to list AWS services.