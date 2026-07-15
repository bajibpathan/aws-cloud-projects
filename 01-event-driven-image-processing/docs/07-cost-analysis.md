# 💰 Cost Analysis and Optimization

## Overview

Cloud cost management is an essential responsibility of a Cloud Engineer. Designing a scalable architecture is important, but ensuring that it remains cost-effective throughout its lifecycle is equally critical.

The Event-Driven Image Processing project was intentionally designed using serverless and fully managed AWS services to minimize operational overhead while following a pay-for-usage pricing model.

Unlike traditional infrastructure where virtual machines run continuously, the services used in this project incur costs primarily when they are actively used. This makes the architecture both scalable and cost-efficient for workloads with variable or unpredictable traffic.

This document explains the cost model of each AWS service used in the project, identifies potential cost drivers, highlights optimization opportunities, and documents the strategies implemented to keep operational costs low.

---

# 🎯 Objectives

The purpose of this document is to:

- Understand how each AWS service is billed.
- Identify the primary cost drivers within the architecture.
- Explain the design decisions made to minimize costs.
- Document best practices for controlling AWS spending.
- Identify potential cost risks.
- Provide recommendations for future production deployments.

---

# 🏗 Cost Flow Architecture

```text
                User Uploads Image
                        │
                        ▼
                 Amazon S3 Bucket
          Storage + Requests + Versioning
                        │
                        ▼
              S3 Event Notification
                  (No Direct Cost)
                        │
                        ▼
                  AWS Lambda
         Invocations + Duration + Memory
                        │
                        ▼
              Amazon DynamoDB
      Write Requests + Storage + Reads
                        │
                        ▼
             Amazon CloudWatch
      Logs + Metrics + Dashboard + Alarm
```

---

# 💡 Cost Optimization Philosophy

One of the primary design goals of this project was to maximize learning while minimizing operational costs.

The following principles guided the architecture:

- Use serverless services whenever possible.
- Avoid always-running compute resources.
- Pay only for actual usage.
- Prevent unnecessary Lambda executions.
- Prevent duplicate database writes.
- Configure log retention.
- Remove unused resources after testing.

These principles align with the **AWS Well-Architected Cost Optimization Pillar**, which encourages organizations to continuously evaluate resource usage and eliminate unnecessary costs.

---

# 📊 AWS Services Used

The following AWS services contribute to the operational cost of the project.

| Service | Purpose | Pricing Model |
|----------|---------|---------------|
| Amazon S3 | Store uploaded images | Storage, requests, data transfer, object versions |
| AWS Lambda | Process uploaded images | Invocations and execution duration |
| Amazon DynamoDB | Store image metadata | On-Demand read/write requests and storage |
| Amazon CloudWatch | Logs, metrics, dashboards and alarms | Log ingestion, storage, dashboards, alarms and custom metrics |
| AWS IAM | Identity and access management | No additional charge |
| Amazon S3 Event Notifications | Trigger Lambda function | No separate charge |

Although several services do not have direct pricing, they can indirectly influence overall costs by increasing usage of other AWS services.

---

# 📈 Estimated Cost Profile

For a small learning environment, the architecture is expected to have a very low operational cost.

Typical characteristics include:

- Small image uploads
- Low request volume
- Minimal Lambda execution time
- Small DynamoDB table
- Limited CloudWatch logging
- One dashboard
- One alarm

Under these conditions, the project should remain inexpensive to operate. However, costs increase as workload, storage, and monitoring requirements grow.

---

# 📌 Cost Drivers

Each AWS service has one or more factors that directly influence cost.

| Service | Primary Cost Drivers |
|----------|----------------------|
| Amazon S3 | Storage, PUT/GET requests, object versions, data transfer |
| AWS Lambda | Number of invocations, execution duration, configured memory |
| Amazon DynamoDB | Read requests, write requests, storage |
| Amazon CloudWatch | Log volume, retention period, dashboards, alarms |
| AWS IAM | No direct cost |
| S3 Event Notifications | No direct cost |

Understanding these cost drivers helps engineers optimize architectures before unnecessary spending occurs.

---

# 🎯 Design Decisions That Reduce Cost

Several implementation decisions were intentionally made to reduce operational costs.

| Design Decision | Cost Benefit |
|-----------------|--------------|
| Serverless architecture | No always-running compute resources |
| Lambda triggered only by S3 uploads | Eliminates idle processing |
| Prefix filtering (`uploads/`) | Prevents unnecessary Lambda executions |
| Deterministic ImageId | Prevents duplicate DynamoDB records |
| DynamoDB On-Demand mode | Eliminates capacity planning for unpredictable workloads |
| Structured logging | Improves troubleshooting while avoiding excessive log volume |
| CloudWatch log retention (30 days) | Prevents indefinite log storage |
| Versioning enabled | Protects data while allowing lifecycle policies to manage storage costs later |

---

# ⚖ Cost vs Architecture Trade-offs

During the design of this project, several architectural decisions were evaluated from both technical and financial perspectives.

| Decision | Benefit | Trade-off |
|----------|---------|-----------|
| Serverless services | Low operational overhead and pay-for-use pricing | Costs scale with usage |
| DynamoDB On-Demand | Automatic scaling without capacity planning | Higher cost than provisioned mode for predictable workloads |
| S3 Versioning | Protects against accidental deletion | Additional storage consumption |
| CloudWatch Dashboard | Simplifies monitoring | Small additional monitoring cost |
| CloudWatch Alarm | Proactive failure detection | Minor ongoing monitoring cost |

These trade-offs were considered acceptable because the project prioritizes simplicity, reliability, and operational visibility while maintaining a low overall cost.

---

# 📖 Cost Analysis Roadmap

The following sections provide a detailed cost analysis for each AWS service used in the project.

The upcoming sections include:

- Amazon S3 Cost Analysis
- AWS Lambda Cost Analysis
- Amazon DynamoDB Cost Analysis
- Amazon CloudWatch Cost Analysis
- AWS IAM Cost Considerations
- Cost Monitoring
- Cost Optimization Best Practices
- Future Cost Improvements
- References

---

---

# 🪣 Amazon S3 Cost Analysis

Amazon S3 stores the original images uploaded by users and serves as the entry point for the event-driven workflow.

Because Amazon S3 follows a pay-as-you-use pricing model, charges depend on how the service is used rather than simply creating a bucket.

## Pricing Components

Amazon S3 charges may include:

- Data storage
- PUT, COPY, POST and LIST requests
- GET requests
- Data transfer
- Lifecycle transitions
- Object retrieval
- Version storage
- Replication (if enabled)
- Transfer Acceleration (if enabled)

---

## Why Amazon S3?

Amazon S3 was selected because it provides:

- Virtually unlimited scalability
- High durability (11 nines)
- Native integration with AWS Lambda
- Built-in event notifications
- Versioning support
- Lifecycle Management
- Serverless architecture compatibility

Unlike Amazon EBS or Amazon EFS, Amazon S3 is designed specifically for object storage and event-driven workloads.

---

## Cost Drivers

The main factors affecting Amazon S3 costs are:

| Cost Driver | Impact |
|-------------|--------|
| Number of uploaded objects | Increases storage usage |
| Object size | Larger files consume more storage |
| PUT requests | Every upload generates a request charge |
| GET requests | Downloads increase request charges |
| Versioning | Previous versions continue consuming storage |
| Data transfer | Charges may apply for outbound traffic |

---

## Versioning Considerations

Versioning is enabled in this project to protect against accidental deletion and overwrites.

Example:

```text
photo.jpg

↓

Version 1

↓

Upload new photo.jpg

↓

Version 2

↓

Version 1 still exists
```

Although only Version 2 is the latest object, Version 1 continues consuming storage until it is permanently removed.

Versioning improves data protection but may gradually increase storage costs if older versions are never cleaned up.

---

## Cost Optimization Strategies

The following practices help minimize Amazon S3 costs:

- Upload only sample images during testing.
- Delete unused objects after validation.
- Remove old object versions when no longer required.
- Configure Lifecycle policies for long-running environments.
- Keep Transfer Acceleration disabled unless global uploads require it.
- Avoid Cross-Region Replication unless business requirements justify additional storage costs.

---

## Best Practices

- Store only required data.
- Regularly review bucket contents.
- Enable Lifecycle rules for production workloads.
- Monitor storage growth.
- Clean up test data after project completion.

---

# ⚡ AWS Lambda Cost Analysis

AWS Lambda processes every uploaded image and stores its metadata in Amazon DynamoDB.

Unlike traditional virtual machines, AWS Lambda charges only when code is executed.

No compute resources remain running while the application is idle.

---

## Pricing Components

Lambda pricing depends primarily on:

- Number of invocations
- Execution duration
- Allocated memory
- Architecture (x86 or ARM)
- Additional ephemeral storage (if configured)
- Provisioned Concurrency (if enabled)

---

## Why AWS Lambda?

AWS Lambda was selected because:

- No server management
- Automatic scaling
- Native integration with Amazon S3
- Event-driven architecture
- Pay only when executed

This perfectly matches the application's workload, where processing occurs only when images are uploaded.

---

## Current Configuration

| Setting | Value |
|----------|-------|
| Memory | 128 MB |
| Timeout | 10 Seconds |
| Runtime | Python |
| Trigger | Amazon S3 |
| Provisioned Concurrency | Disabled |

The function performs lightweight processing and normally completes within milliseconds.

---

## Cost Drivers

| Cost Driver | Impact |
|-------------|--------|
| Number of uploads | More uploads increase invocations |
| Processing time | Longer execution increases cost |
| Memory allocation | Higher memory increases execution cost |
| Recursive execution | May generate unnecessary invocations |

---

## Cost Optimization Strategies

Several implementation decisions reduce Lambda costs.

### Prefix Filtering

Only uploads inside the following folder trigger Lambda:

```text
uploads/
```

This prevents unnecessary Lambda executions for unrelated objects.

---

### File Validation

Unsupported file types are rejected immediately.

Example:

```text
document.pdf

↓

Rejected

↓

No DynamoDB Write
```

Rejecting invalid files early reduces processing time and unnecessary database operations.

---

### Idempotency

Duplicate S3 events can occur.

The project generates a deterministic ImageId and performs a conditional DynamoDB write.

Benefits include:

- Prevents duplicate database records.
- Eliminates unnecessary processing.
- Reduces DynamoDB storage growth.

---

### Structured Logging

Structured logs simplify troubleshooting.

Efficient troubleshooting reduces operational effort and minimizes the need for repeated testing.

---

## Best Practices

- Allocate only the required memory.
- Keep execution time low.
- Prevent recursive invocations.
- Remove unused Lambda versions.
- Monitor execution duration through CloudWatch.

---

# 🗄 Amazon DynamoDB Cost Analysis

Amazon DynamoDB stores image metadata generated by the Lambda function.

The application stores one metadata record for each successfully processed image.

---

## Pricing Components

DynamoDB pricing depends on:

- Read requests
- Write requests
- Storage
- Global Tables
- DynamoDB Streams
- Point-in-Time Recovery
- Backups

---

## Why DynamoDB?

Amazon DynamoDB was selected because:

- Fully serverless
- Automatic scaling
- High availability
- Low latency
- Native AWS integration
- No infrastructure management

Since the project stores metadata rather than relational data, DynamoDB is an ideal choice.

---

## Current Configuration

| Setting | Value |
|----------|-------|
| Capacity Mode | On-Demand |
| Primary Key | ImageId |
| Streams | Disabled |
| Point-in-Time Recovery | Disabled |
| Global Tables | Disabled |

---

## Why On-Demand Capacity?

Image uploads occur unpredictably.

Provisioned capacity would require manually estimating throughput.

On-Demand mode automatically scales based on actual request volume.

Benefits include:

- No capacity planning
- Automatic scaling
- Better fit for learning projects
- Pay only for actual usage

---

## Cost Drivers

| Cost Driver | Impact |
|-------------|--------|
| Number of writes | More uploads create more write requests |
| Number of reads | Metadata lookups increase read costs |
| Table size | Larger metadata consumes more storage |
| Backups | Increase storage costs |
| Global Tables | Replicate storage across Regions |

---

## Cost Optimization Strategies

The project minimizes DynamoDB costs by:

- Using On-Demand capacity.
- Preventing duplicate writes.
- Storing only essential metadata.
- Disabling unnecessary features.
- Avoiding full table scans.

---

## Idempotency Cost Benefit

Without idempotency:

```text
Upload

↓

Duplicate Event

↓

Two Database Records
```

With idempotency:

```text
Upload

↓

Duplicate Event

↓

Duplicate Ignored
```

This reduces:

- Storage usage
- Write requests
- Future read operations

while maintaining data consistency.

---

## Best Practices

- Use On-Demand mode for unpredictable workloads.
- Keep metadata concise.
- Disable unused DynamoDB features.
- Use key-based access instead of table scans.
- Delete test data after completing the project.


---

# 📊 Amazon CloudWatch Cost Analysis

Amazon CloudWatch provides operational visibility into the application by collecting logs, metrics, dashboards, and alarms.

Throughout this project, CloudWatch is used to:

- Store Lambda execution logs
- Publish Lambda performance metrics
- Display operational dashboards
- Monitor application failures through CloudWatch Alarms

CloudWatch is an essential operational service, but it can become one of the largest contributors to cost if log growth is not managed properly.

---

## Pricing Components

CloudWatch pricing may include:

- Log ingestion
- Log storage
- Custom metrics
- Dashboards
- Alarms
- Logs Insights queries
- API requests

---

## Why Amazon CloudWatch?

CloudWatch was selected because it provides native integration with AWS Lambda without requiring additional infrastructure.

Benefits include:

- Automatic Lambda metrics
- Centralized logging
- Operational dashboards
- Proactive alerting
- Native AWS integration

CloudWatch allows engineers to monitor application health without deploying external monitoring tools.

---

## Current Configuration

| Component | Configuration |
|-----------|---------------|
| Log Group | `/aws/lambda/event-image-processor` |
| Log Retention | 30 Days |
| Dashboard | EventImageProcessingDashboard |
| Alarm | EventImageProcessorLambdaErrors |
| Custom Metrics | None |

---

## Cost Drivers

| Cost Driver | Impact |
|-------------|--------|
| Log volume | More Lambda executions generate additional logs |
| Log retention | Longer retention increases storage costs |
| Dashboard widgets | Multiple dashboards increase monitoring costs |
| Alarms | Each alarm contributes to monitoring costs |
| Custom metrics | Additional metrics increase costs |

---

## Cost Optimization Strategies

Several decisions were made to minimize CloudWatch costs.

### Log Retention

Rather than retaining logs indefinitely, the project uses:

```text
30 Days
```

This provides sufficient troubleshooting history while preventing continuous log storage growth.

---

### Structured Logging

Only meaningful operational information is logged.

Each log includes:

- Request ID
- Bucket Name
- Object Key
- Processing Status
- Processing Duration

Verbose debugging information is intentionally avoided.

---

### Minimal Monitoring Resources

The project currently uses:

- One Dashboard
- One Alarm

This keeps operational visibility high while avoiding unnecessary monitoring costs.

---

## Best Practices

- Configure log retention.
- Avoid excessive debug logging.
- Create alarms only for meaningful operational events.
- Delete unused dashboards after project completion.
- Regularly review CloudWatch storage usage.

---

# 🔐 AWS IAM Cost Considerations

AWS Identity and Access Management (IAM) does not incur a separate service charge.

Although IAM itself is free, poorly configured permissions can indirectly increase AWS costs.

---

## Why IAM Matters for Cost

Broad permissions may allow users or applications to:

- Launch unnecessary resources.
- Access additional AWS services.
- Modify infrastructure.
- Create unexpected operational costs.

Applying the Principle of Least Privilege reduces both security risks and accidental spending.

---

## Current IAM Configuration

The Lambda execution role includes only the permissions required for this project.

Current permissions:

```text
AWSLambdaBasicExecutionRole

dynamodb:PutItem
```

The Lambda function cannot:

- Delete DynamoDB tables
- Create new AWS resources
- Modify S3 buckets
- Access unrelated AWS services

Restricting permissions helps protect the AWS account while reducing the possibility of unintended resource creation.

---

## Best Practices

- Follow the Principle of Least Privilege.
- Avoid AdministratorAccess.
- Remove unused IAM roles.
- Remove unused IAM policies.
- Periodically review attached permissions.

---

# ⚠ Potential Cost Risks

Although the project is designed to remain inexpensive, several scenarios could increase operational costs.

---

## Risk 1 – S3 Version Growth

Because Versioning is enabled, older object versions continue consuming storage.

Example:

```text
Version 1

↓

Version 2

↓

Version 3
```

All versions remain stored until they are permanently deleted.

### Mitigation

- Delete unnecessary object versions.
- Configure Lifecycle policies for production environments.

---

## Risk 2 – Excessive CloudWatch Logs

Applications generating large amounts of logs may significantly increase CloudWatch costs.

### Mitigation

- Log only useful operational information.
- Configure log retention.
- Remove unnecessary debug logging.

---

## Risk 3 – Recursive Lambda Execution

A recursive workflow may repeatedly trigger Lambda.

Example:

```text
Upload

↓

Lambda

↓

Writes New File

↓

Triggers Lambda Again

↓

Infinite Loop
```

### Mitigation

The project limits triggers to the following prefix:

```text
uploads/
```

Generated files should be stored under a different prefix such as:

```text
processed/
```

---

## Risk 4 – Duplicate Event Processing

Duplicate S3 events may increase Lambda executions and DynamoDB writes.

### Mitigation

The project implements:

- Deterministic ImageId
- DynamoDB Conditional Writes

Duplicate events are safely ignored.

---

## Risk 5 – Forgotten Resources

Learning projects often continue generating small charges because resources remain deployed after testing.

Examples include:

- S3 Buckets
- CloudWatch Dashboards
- CloudWatch Alarms
- DynamoDB Tables
- Lambda Functions

### Mitigation

A complete cleanup procedure is documented in:

```text
06-operations-guide.md
```

---

# 📈 Cost Monitoring

Monitoring AWS spending is an important operational responsibility.

---

## AWS Billing Dashboard

The Billing Dashboard provides the official breakdown of AWS charges.

Navigation:

```text
AWS Console

↓

Billing and Cost Management

↓

Bills
```

Review charges by:

- AWS Service
- Region
- Usage Type

---

## AWS Cost Explorer

AWS Cost Explorer helps visualize spending trends over time.

Useful reports include:

- Daily Cost
- Monthly Cost
- Cost by Service
- Cost by Region

Cost Explorer is valuable for identifying unexpected spending patterns.

---

## AWS Budgets

AWS Budgets can notify users when spending exceeds a defined threshold.

Example:

```text
Budget Name

↓

AWS-Learning-Budget

↓

Monthly Budget

↓

Notification at 80%
```

Budget notifications help detect unexpected costs before they become significant.

---

## Cost Allocation Tags

Although tags were not required for this learning project, they are highly recommended for production environments.

Example:

| Tag | Example |
|------|---------|
| Project | EventDrivenImageProcessing |
| Environment | Learning |
| Owner | Baji |
| ManagedBy | Manual |

Tags simplify:

- Cost allocation
- Billing reports
- Resource organization
- Operational management

---

# 📊 Operational Cost Review Checklist

Regular operational reviews should include:

- Review AWS Billing Dashboard.
- Review Cost Explorer.
- Verify S3 storage growth.
- Review CloudWatch log size.
- Review DynamoDB storage.
- Review Lambda execution duration.
- Delete unused AWS resources.
- Review IAM roles and policies.

Performing these reviews regularly helps maintain a cost-efficient AWS environment.

---

---

# 🚀 Cost Optimization Recommendations

Designing a cost-effective cloud solution is an ongoing process rather than a one-time activity. Although this project operates with minimal AWS resources, following cost optimization best practices ensures that the architecture remains efficient as it grows.

The following recommendations help minimize operational costs while maintaining reliability and scalability.

---

## Amazon S3

### Recommendations

- Delete unused test images after validation.
- Remove non-current object versions when no longer required.
- Configure Lifecycle Rules for long-running environments.
- Keep Transfer Acceleration disabled unless global uploads require improved performance.
- Avoid Cross-Region Replication unless there is a business requirement.
- Store only the data required by the application.

---

## AWS Lambda

### Recommendations

- Allocate only the memory required by the workload.
- Keep execution duration as short as possible.
- Reject unsupported files early.
- Prevent recursive invocations.
- Remove unused Lambda versions.
- Monitor execution duration through CloudWatch.

---

## Amazon DynamoDB

### Recommendations

- Continue using On-Demand Capacity for unpredictable workloads.
- Store only essential metadata.
- Prevent duplicate writes using conditional expressions.
- Disable unnecessary features such as Streams or Global Tables unless required.
- Delete temporary metadata after project completion.

---

## Amazon CloudWatch

### Recommendations

- Configure log retention.
- Avoid excessive logging.
- Create only meaningful alarms.
- Delete dashboards and alarms after completing the project.
- Review CloudWatch storage periodically.

---

## AWS IAM

### Recommendations

- Follow the Principle of Least Privilege.
- Remove unused IAM roles.
- Remove unused IAM policies.
- Avoid overly permissive policies such as `AdministratorAccess`.
- Periodically review attached permissions.

---

# 📈 Scaling Considerations

Although this project is designed for learning purposes, production workloads require additional planning.

As the number of uploaded images increases, the following services are likely to become the primary cost drivers.

| Service | Scaling Impact |
|----------|----------------|
| Amazon S3 | Increased storage and request costs |
| AWS Lambda | Increased invocations and execution duration |
| Amazon DynamoDB | Increased read/write capacity and storage |
| Amazon CloudWatch | Larger log volume and additional monitoring |

Future versions of the project may introduce:

- Amazon SQS
- Dead Letter Queue (DLQ)
- AWS Step Functions
- Amazon EventBridge
- AWS X-Ray
- Amazon SNS Notifications

These services improve scalability and reliability but also introduce additional operational costs that should be evaluated before implementation.

---

# 🧪 Validation Checklist

The following validation steps were completed as part of the project.

## Amazon S3

- [ ] Versioning enabled
- [ ] Server-side encryption enabled
- [ ] Bucket Owner Enforced enabled
- [ ] Event Notification configured
- [ ] Prefix filtering configured

---

## AWS Lambda

- [ ] S3 trigger configured
- [ ] Environment variables configured
- [ ] Structured logging implemented
- [ ] File validation implemented
- [ ] Idempotent processing implemented
- [ ] Error handling validated

---

## Amazon DynamoDB

- [ ] On-Demand capacity enabled
- [ ] Metadata successfully stored
- [ ] Duplicate records prevented
- [ ] Conditional writes verified

---

## Amazon CloudWatch

- [ ] Log retention configured
- [ ] Dashboard created
- [ ] Error alarm configured
- [ ] Structured logs verified
- [ ] Metrics validated

---

## Cost Management

- [ ] Billing Dashboard reviewed
- [ ] Resource inventory verified
- [ ] CloudWatch log retention configured
- [ ] Unused resources identified
- [ ] Cleanup plan documented

---

# 📚 Lessons Learned

Developing this project provided valuable insights into cost optimization within AWS.

### Serverless Does Not Mean Free

Although serverless services eliminate infrastructure management, charges are still based on actual usage. Monitoring resource consumption remains essential.

---

### Small Design Decisions Influence Cost

Several implementation choices helped reduce operational costs.

Examples include:

- Prefix filtering
- Idempotent processing
- Structured logging
- Log retention configuration
- On-Demand DynamoDB capacity

These improvements reduce unnecessary processing and storage.

---

### Monitoring Helps Reduce Cost

CloudWatch is not only useful for troubleshooting but also for identifying inefficiencies such as:

- Long Lambda execution times
- Unexpected invocation spikes
- Excessive logging
- Application failures

Operational visibility directly supports cost optimization.

---

### Cleanup Is Part of Cloud Engineering

Many learning environments continue generating charges because resources remain deployed after testing.

Cloud Engineers should always plan for:

- Deployment
- Monitoring
- Cost management
- Resource cleanup

---

### Cost Optimization Is Continuous

Cost optimization is not a one-time task.

As architectures evolve, engineers should regularly review:

- Storage usage
- Lambda execution metrics
- Database growth
- Monitoring resources
- Billing reports

Continuous review helps ensure that cloud solutions remain efficient over time.

---

# 💡 Key Takeaways

- Serverless architectures help minimize operational overhead.
- Pay-for-use pricing requires continuous monitoring.
- Versioning improves durability but increases storage usage.
- Structured logging improves troubleshooting while keeping log volume manageable.
- Idempotent processing reduces duplicate writes and unnecessary costs.
- Monitoring and billing reviews are essential operational activities.
- Resource cleanup should always be included in the project lifecycle.
- Cost optimization should be considered during every design decision.

---

# 📖 References

The following AWS documentation provides additional information about pricing and cost optimization.

## Amazon S3 Pricing

https://aws.amazon.com/s3/pricing/

---

## AWS Lambda Pricing

https://aws.amazon.com/lambda/pricing/

---

## Amazon DynamoDB Pricing

https://aws.amazon.com/dynamodb/pricing/

---

## Amazon CloudWatch Pricing

https://aws.amazon.com/cloudwatch/pricing/

---

## AWS Pricing Calculator

https://calculator.aws/

---

## AWS Billing and Cost Management

https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/

---

## AWS Budgets

https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html

---

## AWS Well-Architected Framework

https://docs.aws.amazon.com/wellarchitected/latest/framework/

---

## AWS Well-Architected Cost Optimization Pillar

https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/

---

# ✅ Conclusion

The Event-Driven Image Processing project demonstrates that effective cloud engineering extends beyond building functional solutions. It also requires designing architectures that are secure, observable, reliable, scalable, and cost-efficient.

By selecting serverless services, implementing idempotent processing, configuring operational monitoring, and documenting cleanup procedures, this project follows many of the design principles recommended by the AWS Well-Architected Framework.

Understanding the pricing model of each AWS service and applying cost optimization best practices helps ensure that cloud solutions remain efficient throughout their lifecycle.

The next step is to perform the documented cleanup process, verify that all resources have been removed successfully, and archive the project as a complete portfolio demonstrating the end-to-end lifecycle of a production-inspired serverless application.

