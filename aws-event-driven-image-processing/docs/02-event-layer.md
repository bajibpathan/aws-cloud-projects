# ⚡ Event Layer Design

## Overview

The Event Layer connects the storage layer with the compute layer by enabling event-driven processing.

Whenever a new image is uploaded to the designated location in the Amazon S3 bucket, Amazon S3 automatically generates an event notification that invokes an AWS Lambda function. This eliminates the need for applications to continuously monitor or poll the bucket for new files.

At this stage of the project, the Lambda function receives the event, extracts the uploaded object's information, and records the execution details in Amazon CloudWatch Logs.

---

# 🎯 Objectives

The Event Layer should:

- Automatically detect new image uploads.
- Trigger processing without manual intervention.
- Invoke the AWS Lambda function only for uploaded images.
- Prevent unnecessary Lambda executions.
- Provide logging for troubleshooting and validation.

---

# 🏗 Architecture

```text
User

        │

Upload Image

        ▼

Amazon S3 Bucket

        │

ObjectCreated Event

        ▼

Amazon S3 Event Notification

        │

        ▼

AWS Lambda

        │

        ▼

Amazon CloudWatch Logs
```

---

# Why Amazon S3 Event Notifications?

Amazon S3 Event Notifications provide a native event-driven mechanism to automatically invoke downstream services whenever an object event occurs.

For this project, Event Notifications eliminate the need to continuously check the S3 bucket for newly uploaded images. Instead, AWS automatically invokes the Lambda function whenever an image is uploaded.

This approach results in:

- Lower operational overhead
- Near real-time processing
- Automatic scaling
- Cost-effective architecture

---

# Why AWS Lambda?

AWS Lambda was selected because it is a serverless compute service that integrates natively with Amazon S3 Event Notifications.

Since image uploads occur unpredictably, running dedicated servers would be unnecessary and costly.

AWS Lambda automatically scales based on incoming events and charges only for actual execution time.

---

# Why Not Amazon EC2?

Amazon EC2 requires:

- Provisioning virtual machines
- Operating system maintenance
- Capacity planning
- Continuous server availability

For an event-driven workload where processing occurs only after an image upload, AWS Lambda is the more appropriate solution.

---

# Event Configuration

| Configuration | Value |
|---------------|-------|
| Event Source | Amazon S3 |
| Event Type | ObjectCreated (All) |
| Prefix Filter | `uploads/` |
| Destination | AWS Lambda |
| Lambda Function | `event-image-processor` |

---

# Design Decisions

## ObjectCreated Events

Only **ObjectCreated** events are configured because the project currently processes newly uploaded images.

Future enhancements may include handling object deletion or update events if business requirements change.

---

## Prefix Filtering

The Event Notification is configured to monitor only the `uploads/` prefix.

This ensures that only newly uploaded images trigger the Lambda function.

Future project phases may introduce additional prefixes such as:

```text
uploads/

processed/

failed/

archive/
```

Using prefix filtering also helps prevent recursive processing if Lambda writes processed files to another location.

---

# Permissions

Two different permission models are involved in this integration.

## Lambda Execution Role

The Lambda Execution Role grants the Lambda function permission to access other AWS services.

At this stage, the role contains only:

- AWSLambdaBasicExecutionRole

This allows the function to create and write logs in Amazon CloudWatch.

---

## Lambda Resource-Based Policy

Amazon S3 requires permission to invoke the Lambda function.

When the Event Notification was created, AWS automatically added a resource-based policy allowing:

- Principal: `s3.amazonaws.com`
- Action: `lambda:InvokeFunction`

Without this permission, Amazon S3 would not be able to invoke the Lambda function.

---

# Validation

The following validations were successfully completed:

- Lambda function created successfully.
- Manual Lambda test executed successfully.
- S3 event JSON parsed successfully.
- Amazon S3 Event Notification configured.
- Image uploaded to the `uploads/` prefix.
- Lambda invoked automatically.
- Bucket name and object key extracted successfully.
- CloudWatch Logs validated.

---

# Screenshots

The following screenshots were captured as implementation evidence:

- Lambda Function Overview
- Lambda Configuration
- Manual Test Execution
- CloudWatch Logs
- Amazon S3 Event Notification
- Lambda Trigger
- Resource-Based Policy

---

# Lessons Learned

- Event-driven architectures eliminate the need for continuous polling.
- Amazon S3 can automatically invoke AWS Lambda using Event Notifications.
- Prefix filtering improves efficiency and helps prevent recursive processing.
- Lambda Execution Roles and Resource-Based Policies serve different purposes.
- CloudWatch Logs provide valuable information for troubleshooting and validation.

---

# Challenges

## Challenge

Initially, it was unclear why both an IAM Role and a Resource-Based Policy were required.

### Root Cause

The Lambda Execution Role controls what the Lambda function is allowed to do after it starts running.

The Resource-Based Policy controls who is allowed to invoke the Lambda function.

Both permissions are required for successful integration.

### Resolution

Verified both permission models and confirmed successful end-to-end event processing.

---

# Future Enhancements

The current implementation directly invokes AWS Lambda.

Future versions of the project will introduce:

- Amazon DynamoDB for metadata storage
- Amazon SQS to improve reliability and absorb traffic spikes
- Dead Letter Queue (DLQ) for failed message processing
- Amazon EventBridge for advanced event routing
- Image validation and metadata extraction
- Thumbnail generation
- Infrastructure as Code (Terraform)

---

# References

- Amazon S3 Event Notifications Documentation
- AWS Lambda Documentation
- AWS IAM Documentation
- Amazon CloudWatch Documentation