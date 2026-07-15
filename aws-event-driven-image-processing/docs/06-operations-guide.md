# ⚙️ Operations Guide

## Overview

This document describes how to operate, validate, monitor, troubleshoot, estimate costs, and safely remove the resources used by the Event-Driven Image Processing project.

The goal is to ensure that another engineer can successfully deploy, operate, and decommission the solution.

---

# Deployment Order

Create resources in the following order.

```text
IAM Role

↓

Amazon S3 Bucket

↓

Amazon DynamoDB

↓

AWS Lambda

↓

Lambda Environment Variables

↓

S3 Event Notification

↓

CloudWatch Dashboard

↓

CloudWatch Alarm
```

---

# Operational Workflow

```text
Upload Image

↓

Amazon S3

↓

S3 Event Notification

↓

AWS Lambda

↓

Validate Image

↓

Amazon DynamoDB

↓

CloudWatch Logs

↓

CloudWatch Metrics

↓

CloudWatch Dashboard

↓

CloudWatch Alarm
```

---

# Daily Operational Checks

Verify:

- Lambda Invocations
- Lambda Errors
- Lambda Duration
- CloudWatch Alarm Status
- DynamoDB Items
- CloudWatch Logs

---

# Testing Checklist

## Valid Image

Expected:

- Lambda succeeds
- Metadata stored
- Dashboard updated

---

## Unsupported File

Expected:

- REJECTED
- No DynamoDB item

---

## Duplicate Event

Expected:

- DUPLICATE
- No duplicate metadata

---

## Invalid Event

Expected:

- FAILED
- Error logged

---

# Troubleshooting

## Lambda Not Triggered

Verify:

- S3 Event Notification
- Lambda Resource Policy
- Bucket Prefix

---

## No DynamoDB Record

Verify:

- Lambda IAM Role
- DynamoDB Table Name
- CloudWatch Logs

---

## CloudWatch Dashboard Empty

Verify:

- Lambda executed
- Metrics refresh interval
- Correct Region

---

# Estimated AWS Costs

This project stays within the AWS Free Tier for most learning environments.

Services used:

- Amazon S3
- AWS Lambda
- Amazon DynamoDB
- Amazon CloudWatch
- AWS IAM

Actual costs depend on usage.

Always review AWS Billing before leaving resources running.

---

# Resource Cleanup Order

Delete resources in the following order.

```text
CloudWatch Alarm

↓

CloudWatch Dashboard

↓

S3 Event Notification

↓

AWS Lambda

↓

IAM Role

↓

DynamoDB Table

↓

Delete S3 Objects

↓

Amazon S3 Bucket
```

Deleting resources in this order prevents dependency errors.

---

# Lessons Learned

Operating cloud applications involves more than deployment.

An engineer should also understand:

- Monitoring
- Validation
- Troubleshooting
- Cost management
- Resource cleanup

These activities are essential parts of running production cloud workloads.