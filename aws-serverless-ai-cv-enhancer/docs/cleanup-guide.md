# AWS Resource Cleanup Guide

## Overview

This guide explains how to remove the AWS resources created throughout this project after you have finished learning or testing.

Cleaning up unused resources helps avoid unnecessary AWS charges.

> **Note**
>
> If you are using this project as part of your portfolio, you may want to keep the application deployed so you can demonstrate it to recruiters or hiring managers.

---

# Resources Created

During this project, the following AWS resources were created:

- AWS Lambda
- Amazon API Gateway (HTTP API)
- Amazon DynamoDB
- Amazon S3 Static Website
- Amazon CloudWatch Log Groups
- IAM Roles and Policies

---

# Recommended Cleanup Order

Delete resources in the following order:

```text
Amazon S3 Static Website
        │
        ▼
Amazon API Gateway
        │
        ▼
AWS Lambda
        │
        ▼
Amazon DynamoDB
        │
        ▼
CloudWatch Log Groups
        │
        ▼
IAM Roles and Policies
```

Deleting resources in this order helps avoid dependency-related issues.

---

# 1. Delete Amazon S3 Static Website

## AWS Console

Navigate to:

```text
Amazon S3
→ Buckets
→ serverless-ai-cv-enhancer-<account-id>
```

### Delete Objects

Select all objects and choose:

```text
Delete
```

### Delete Bucket

Choose:

```text
Delete bucket
```

Confirm the bucket name when prompted.

---

## AWS CLI

```bash
aws s3 rm \
  s3://serverless-ai-cv-enhancer-<account-id> \
  --recursive

aws s3 rb \
  s3://serverless-ai-cv-enhancer-<account-id>
```

---

# 2. Delete Amazon API Gateway

## AWS Console

Navigate to:

```text
Amazon API Gateway
→ APIs
→ serverless-ai-cv-enhancer-api
→ Delete
```

---

## AWS CLI

```bash
aws apigatewayv2 delete-api \
  --api-id YOUR_API_ID
```

---

# 3. Delete AWS Lambda

## AWS Console

Navigate to:

```text
AWS Lambda
→ serverless-ai-cv-enhancer
→ Delete
```

---

## AWS CLI

```bash
aws lambda delete-function \
  --function-name serverless-ai-cv-enhancer
```

---

# 4. Delete Amazon DynamoDB Table

## AWS Console

Navigate to:

```text
Amazon DynamoDB
→ Tables
→ ResumeEnhancementHistory
→ Delete table
```

---

## AWS CLI

```bash
aws dynamodb delete-table \
  --table-name ResumeEnhancementHistory
```

---

# 5. Delete CloudWatch Log Groups

CloudWatch log groups remain even after deleting Lambda functions.

## AWS Console

Navigate to:

```text
CloudWatch
→ Log groups
```

Delete:

```text
/aws/lambda/serverless-ai-cv-enhancer

/aws/apigateway/serverless-ai-cv-enhancer
```

---

## AWS CLI

```bash
aws logs delete-log-group \
  --log-group-name /aws/lambda/serverless-ai-cv-enhancer

aws logs delete-log-group \
  --log-group-name /aws/apigateway/serverless-ai-cv-enhancer
```

---

# 6. Delete IAM Resources

If you created a dedicated Lambda execution role for this project, you can remove it after deleting the Lambda function.

## AWS Console

Navigate to:

```text
IAM
→ Roles
→ serverless-ai-cv-enhancer-role
→ Delete
```

Also remove any inline policies created specifically for this project.

> Do not delete shared IAM roles or policies used by other applications.

---

# Verify Cleanup

After completing the cleanup steps, verify that:

- No Lambda functions remain
- No API Gateway APIs remain
- The DynamoDB table has been deleted
- The S3 bucket has been removed
- CloudWatch log groups have been deleted
- Any project-specific IAM roles have been removed

---

# Estimated Ongoing Costs

If left running, this project generally incurs very low costs because it uses serverless services.

Typical cost sources include:

- Amazon Bedrock inference requests
- API Gateway requests
- AWS Lambda invocations
- DynamoDB storage and requests
- Amazon S3 storage
- CloudWatch log storage

If you are no longer using the project, deleting these resources will prevent any future charges.

---

# Final Note

This project was designed as a hands-on learning exercise to demonstrate modern AWS serverless architecture and Generative AI integration.

Keeping the application deployed can be useful for showcasing your work in interviews or as part of your portfolio. If you no longer need the deployment, following this guide will safely remove the AWS resources created during the project.