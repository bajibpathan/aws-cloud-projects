# 🛡 Reliability and Resilience Layer Design

## Overview

The Reliability and Resilience Layer enhances the Event-Driven Image Processing application by ensuring it can safely handle duplicate events, invalid uploads, and unexpected processing errors.

Amazon S3 Event Notifications use an **at-least-once delivery** model, meaning the same event may be delivered more than once. Without additional controls, duplicate events could create duplicate metadata records in Amazon DynamoDB.

This phase improves the application by introducing idempotent processing, file validation, structured logging, and enhanced error handling. These improvements increase the reliability of the application while maintaining a simple serverless architecture.

Rather than introducing additional AWS services, this phase focuses on improving the quality and robustness of the existing solution.

---

# 🎯 Objectives

The Reliability and Resilience Layer should:

- Prevent duplicate metadata records.
- Process only supported image formats.
- Reject unsupported files safely.
- Handle malformed S3 events gracefully.
- Improve application reliability.
- Generate structured logs for troubleshooting.
- Track processing status throughout the workflow.
- Maintain least-privilege security.

---

# 🏗 Architecture

```text
                        User
                          │
                    Upload Object
                          │
                          ▼
                  Amazon S3 Bucket
                          │
                ObjectCreated Event
                          │
                          ▼
                     AWS Lambda
                          │
                 Parse and Validate
                          │
          ┌───────────────┼────────────────┐
          │               │                │
          ▼               ▼                ▼
    Valid Image     Unsupported File   Invalid Event
          │               │                │
          ▼               ▼                ▼
 Generate Stable      Log REJECTED     Log FAILED
    ImageId                 │               │
          │                 └──────┬────────┘
          ▼                        ▼
 Conditional DynamoDB      Amazon CloudWatch
       PutItem                  Logs
          │
    ┌─────┴─────────┐
    │               │
    ▼               ▼
New Record      Duplicate Record
    │               │
    ▼               ▼
METADATA_STORED   DUPLICATE
```

---

# 💡 Design Decision

## Design Decision #5 – Why Improve Reliability Within the Lambda Function?

The primary goal of this phase is to improve the reliability of the existing architecture without increasing its complexity.

The application currently processes one image upload at a time using a direct integration between Amazon S3 and AWS Lambda. Before introducing additional services such as Amazon SQS or AWS Step Functions, it is important to ensure that the Lambda function itself can safely handle common failure scenarios.

The following reliability improvements were implemented directly within the Lambda function:

- Deterministic image identifiers
- Idempotent DynamoDB writes
- File-type validation
- Structured JSON logging
- Processing status tracking
- Improved exception handling

These enhancements significantly improve the application's resilience while keeping the architecture simple and easy to understand.

---

## Alternatives Considered

| Option | Decision |
|----------|----------|
| **Application-level reliability controls** | ✅ Selected because they improve resilience without introducing additional AWS services. |
| **Amazon SQS** | Deferred to a future version of the project where buffering, retry control, and traffic spikes will be addressed. |
| **Dead Letter Queue (DLQ)** | Deferred until asynchronous failure handling is introduced. |
| **AWS Step Functions** | Not selected because the current workflow does not require orchestration across multiple processing steps. |
| **Random UUID for every upload** | Replaced because duplicate S3 events would generate multiple metadata records for the same object. |

---

## Benefits

The chosen approach provides several advantages:

- Prevents duplicate metadata records.
- Rejects unsupported uploads before database operations.
- Produces consistent structured logs.
- Improves troubleshooting.
- Maintains a simple serverless architecture.
- Requires no additional AWS services.
- Preserves the existing least-privilege IAM model.

---

## Trade-offs

Although this implementation improves reliability, several trade-offs remain.

- Unsupported files are logged but not stored in a dedicated failure table.
- File validation is based on the object extension rather than inspecting the actual file contents.
- Retry buffering is not available without Amazon SQS.
- The current implementation processes only the first record within an S3 event notification.

These trade-offs are acceptable for Version 1 of the project and are documented as future enhancements.

---

# ⚙️ Implementation Details

## Deterministic Image Identifier

The initial implementation generated a random UUID every time the Lambda function was invoked.

```python
image_id = str(uuid.uuid4())
```

Although this uniquely identified each database record, it introduced a reliability issue.

Amazon S3 Event Notifications use an **at-least-once delivery** model. If the same event is delivered multiple times, generating a new UUID for every invocation results in duplicate metadata records for the same uploaded object.

To solve this problem, the application now generates a deterministic identifier using:

```text
Bucket Name + Object Key + Version ID
```

The combined value is hashed using SHA-256.

```python
unique_value = f"{bucket_name}:{object_key}:{version_id}"

image_id = hashlib.sha256(
    unique_value.encode("utf-8")
).hexdigest()
```

Using the same bucket name, object key, and version ID always produces the same ImageId.

This makes the application idempotent because repeated processing of the same object generates the same primary key.

---

## DynamoDB Conditional Writes

Generating a deterministic ImageId alone does not prevent duplicate records.

To ensure that metadata is written only once, the Lambda function performs a conditional write.

```python
table.put_item(
    Item=item,
    ConditionExpression="attribute_not_exists(ImageId)"
)
```

This condition instructs DynamoDB to create the item only when the ImageId does not already exist.

If the same event is received again, DynamoDB raises a `ConditionalCheckFailedException`.

The Lambda function treats this as a duplicate event rather than a processing failure.

Benefits of this approach include:

- Prevents duplicate metadata records.
- Avoids overwriting existing records.
- Makes repeated event processing safe.
- Improves overall application reliability.

---

## Supported File Validation

The application is designed to process only image files.

Currently supported extensions include:

```text
.jpg
.jpeg
.png
```

The supported extensions are stored in a Python set.

```python
SUPPORTED_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png"
}
```

Before any database operation is performed, the uploaded object's extension is validated.

If the uploaded object is not a supported image type, processing stops immediately.

The Lambda function:

- Writes a structured warning log.
- Returns a controlled response.
- Does not create a DynamoDB record.

This prevents unsupported files from entering downstream processing.

---

## Processing Status Tracking

Instead of recording only successful uploads, the application now tracks the current processing state.

| Status | Description |
|----------|-------------|
| RECEIVED | Lambda received the S3 event. |
| VALIDATED | The uploaded file passed validation. |
| METADATA_STORED | Metadata was successfully stored in DynamoDB. |
| DUPLICATE | The event was previously processed and safely ignored. |
| REJECTED | The uploaded file type is not supported. |
| FAILED | Processing failed because of an unexpected error. |

A successful upload follows this lifecycle:

```text
RECEIVED

↓

VALIDATED

↓

METADATA_STORED
```

A duplicate event follows:

```text
RECEIVED

↓

VALIDATED

↓

DUPLICATE
```

An unsupported upload follows:

```text
RECEIVED

↓

REJECTED
```

These statuses make troubleshooting significantly easier because every upload can be traced through its processing lifecycle.

---

## Structured Logging

The original implementation relied on simple print statements.

```python
print("Metadata stored successfully")
```

Although functional, plain-text logs become difficult to search and analyze as applications grow.

The application now writes structured JSON logs.

Example:

```json
{
  "message": "Image metadata stored successfully",
  "requestId": "example-request-id",
  "status": "METADATA_STORED",
  "imageId": "example-image-id",
  "bucket": "example-bucket",
  "objectKey": "uploads/sample.jpg",
  "processingTimeMs": 38.42
}
```

Structured logs provide several advantages:

- Easier searching in CloudWatch Logs Insights.
- Consistent log format.
- Improved troubleshooting.
- Better support for operational dashboards.
- Simpler integration with external observability platforms.

---

## Processing Duration

The Lambda function records the total processing time for every invocation.

Processing begins by recording the current high-resolution timestamp.

```python
start_time = time.perf_counter()
```

At the end of processing, the elapsed execution time is calculated.

```python
processing_time_ms = round(
    (time.perf_counter() - start_time) * 1000,
    2
)
```

The processing duration is included in every structured log.

Monitoring execution time helps identify:

- Slow Lambda executions.
- Performance regressions.
- Processing bottlenecks.
- Future optimization opportunities.

---

## Error Handling

The Lambda function now distinguishes between different failure scenarios instead of treating every exception the same.

### Duplicate Event

Duplicate events are detected using the DynamoDB conditional write.

Result:

```text
Status = DUPLICATE
```

The invocation returns successfully because the event has already been processed.

---

### Unsupported File

When the uploaded file extension is not supported:

- Processing stops immediately.
- Metadata is not written to DynamoDB.
- A warning is written to CloudWatch Logs.

Result:

```text
Status = REJECTED
```

---

### Invalid S3 Event

Malformed or incomplete S3 events are detected before processing.

Examples include:

- Missing Records collection
- Missing bucket information
- Missing object key

The function returns a controlled error response.

Result:

```text
Status = FAILED
```

---

### DynamoDB Failure

Unexpected DynamoDB client errors are logged with detailed diagnostic information.

The exception is re-raised so that AWS Lambda records the invocation as a failed execution.

Result:

```text
Status = FAILED
```

---

### Unexpected Error

Any unexpected runtime exception is treated as a processing failure.

The application logs:

- Request ID
- Bucket Name
- Object Key
- Exception Type
- Error Message
- Processing Duration

The exception is then re-raised to allow CloudWatch and Lambda metrics to capture the failure.


---

# 🔐 Security Decisions

## Principle of Least Privilege

No additional IAM permissions were introduced during this phase.

The Lambda execution role continues to use only the permissions required to perform its responsibilities.

Current permissions include:

```text
AWSLambdaBasicExecutionRole

dynamodb:PutItem
```

The Lambda function **cannot**:

- Delete DynamoDB items
- Update existing records
- Scan the DynamoDB table
- Create or delete DynamoDB tables
- Access other DynamoDB tables
- Modify Amazon S3 objects

Restricting permissions reduces the application's attack surface and follows the AWS Principle of Least Privilege.

---

## Input Validation

The Lambda function validates uploaded file extensions before performing any database operation.

Only the following image formats are accepted:

```text
.jpg
.jpeg
.png
```

Files with unsupported extensions are rejected immediately.

Benefits of early validation include:

- Preventing unsupported files from entering downstream processing.
- Avoiding unnecessary DynamoDB writes.
- Reducing Lambda execution time.
- Simplifying future image-processing workflows.

Although extension validation provides a useful first layer of protection, future versions should also validate:

- MIME type
- File signature (magic number)
- Maximum file size
- Image dimensions

---

## Controlled Error Responses

The application separates internal diagnostic information from client responses.

Detailed information, including stack traces and exception details, is written only to Amazon CloudWatch Logs.

The Lambda response contains only high-level status information.

Example:

```json
{
    "message": "Unsupported file type",
    "status": "REJECTED"
}
```

This approach prevents sensitive implementation details from being exposed to consumers of the API.

---

# 🧪 Validation

The following scenarios were successfully tested during implementation.

---

## Scenario 1 – Valid Image Upload

Input:

```text
uploads/status-test.jpg
```

Expected processing flow:

```text
RECEIVED

↓

VALIDATED

↓

METADATA_STORED
```

Validation performed:

- Lambda executed successfully.
- Image metadata was written to DynamoDB.
- Processing status was stored as **METADATA_STORED**.
- Structured CloudWatch logs were generated.

---

## Scenario 2 – Duplicate Event

The same S3 event was executed multiple times using the same:

- Bucket Name
- Object Key
- Version ID

Expected result:

```text
DUPLICATE
```

Validation performed:

- Only one DynamoDB record exists.
- Duplicate event was safely ignored.
- Lambda returned a successful response.
- Structured logs identified the duplicate event.

---

## Scenario 3 – Unsupported File

Input:

```text
uploads/document.pdf
```

Expected processing flow:

```text
RECEIVED

↓

REJECTED
```

Validation performed:

- Processing stopped immediately.
- No metadata record was created.
- Warning log generated.
- Response returned with **REJECTED** status.

---

## Scenario 4 – Invalid Event

Input:

```json
{
    "message": "Invalid Event"
}
```

Expected result:

```text
FAILED
```

Validation performed:

- Invalid event detected.
- Controlled error response returned.
- Failure recorded in CloudWatch Logs.
- Lambda execution completed without creating database records.

---

## Scenario 5 – CloudWatch Verification

Verified:

- Structured JSON logs
- Request IDs
- Processing duration
- Processing status
- CloudWatch Metrics
- CloudWatch Dashboard
- CloudWatch Alarm

---

# 📸 Implementation Evidence

The following screenshots were captured throughout this phase.

| Screenshot | Description |
|------------|-------------|
| 34-idempotent-lambda-code.png | Deterministic ImageId implementation |
| 35-first-event-success.png | Successful metadata creation |
| 36-duplicate-event-ignored.png | Duplicate event safely ignored |
| 37-single-dynamodb-record.png | DynamoDB contains only one record |
| 38-file-validation-code.png | File validation logic |
| 39-supported-image-success.png | Valid image processed successfully |
| 40-unsupported-file-rejected.png | Unsupported file rejected |
| 41-no-dynamodb-record-for-pdf.png | No metadata stored for rejected file |
| 42-structured-logging-code.png | Structured logging implementation |
| 43-valid-image-status-logs.png | Successful processing lifecycle |
| 44-duplicate-status-log.png | Duplicate event log |
| 45-rejected-file-status-log.png | Rejected file log |
| 46-invalid-event-failed-log.png | Invalid event failure log |
| 47-dynamodb-metadata-stored-status.png | DynamoDB item with processing status |

---

# 📚 Lessons Learned

This phase introduced several important reliability concepts commonly used in production systems.

### Idempotency is Essential

Distributed systems must assume that events can be delivered more than once.

Generating deterministic identifiers and using DynamoDB conditional writes prevents duplicate processing.

---

### Validation Should Happen Early

Rejecting unsupported files before database operations:

- Reduces unnecessary work
- Improves performance
- Simplifies downstream processing

---

### Structured Logging Improves Troubleshooting

Structured JSON logs are significantly easier to:

- Search
- Filter
- Analyze
- Integrate with monitoring platforms

than plain-text log messages.

---

### Different Failure Types Require Different Responses

Not every unsuccessful request is an application failure.

The project now distinguishes between:

- Duplicate events
- Unsupported uploads
- Invalid events
- Processing failures

Each scenario is handled independently.

---

### Reliability Can Be Improved Incrementally

Many reliability improvements can be achieved through thoughtful application design without immediately introducing additional AWS services.

Understanding these design patterns is important before expanding the architecture.

---

# 🧩 Challenges

## Challenge 1 – Duplicate Metadata Records

### Problem

Using a random UUID caused duplicate metadata records when the same S3 event was delivered multiple times.

### Solution

A deterministic ImageId was generated from:

- Bucket Name
- Object Key
- Version ID

DynamoDB conditional writes ensure metadata is stored only once.

---

## Challenge 2 – Distinguishing Expected Conditions from Errors

### Problem

Initially, duplicate events and unsupported files were treated as generic failures.

### Solution

Separate processing states were introduced:

```text
RECEIVED

VALIDATED

METADATA_STORED

DUPLICATE

REJECTED

FAILED
```

This provides much better operational visibility.

---

## Challenge 3 – Plain-Text Logging

### Problem

Simple print statements lacked consistency and made troubleshooting more difficult.

### Solution

A reusable structured logging function was implemented.

Every log now includes:

- Request ID
- Bucket Name
- Object Key
- Processing Status
- Processing Duration

This makes CloudWatch Logs significantly easier to analyze.

---

---

# 🔮 Future Enhancements

The current implementation establishes a reliable and resilient foundation for the Event-Driven Image Processing application.

Future versions of the project will introduce additional AWS services and architectural patterns to improve scalability, fault tolerance, security, and operational excellence.

## Amazon SQS

Introduce Amazon SQS between Amazon S3 and AWS Lambda to decouple the storage and processing layers.

Benefits include:

- Message buffering
- Better traffic handling
- Controlled retry behavior
- Improved fault tolerance
- Protection against sudden traffic spikes

---

## Dead Letter Queue (DLQ)

Configure a Dead Letter Queue (DLQ) for messages that cannot be processed successfully after multiple retry attempts.

Benefits include:

- Preventing message loss
- Simplifying troubleshooting
- Supporting manual reprocessing
- Improving operational visibility

---

## Amazon EventBridge

Replace the direct S3-to-Lambda integration with Amazon EventBridge to support event routing across multiple AWS services.

Possible future consumers include:

- AWS Lambda
- Amazon SNS
- Amazon SQS
- AWS Step Functions
- Amazon ECS

This enables a more flexible and extensible event-driven architecture.

---

## Image Processing

Extend the Lambda function to perform image processing tasks such as:

- Thumbnail generation
- Image resizing
- Image optimization
- Watermarking
- Format conversion

---

## Content Validation

Improve file validation beyond checking file extensions.

Future validation may include:

- MIME type verification
- Magic number (file signature) validation
- Image dimension validation
- Maximum file size limits
- Corrupted image detection

These improvements help prevent malicious or invalid uploads.

---

## Processing Status Tracking

Expand the metadata model to track the complete processing lifecycle.

Possible statuses include:

```text
RECEIVED

↓

VALIDATED

↓

QUEUED

↓

PROCESSING

↓

PROCESSED

↓

COMPLETED
```

Additional failure states may include:

```text
REJECTED

FAILED

RETRYING

EXPIRED
```

---

## CloudWatch Enhancements

Enhance operational monitoring by introducing:

- CloudWatch Metric Filters
- Custom CloudWatch Metrics
- CloudWatch Logs Insights queries
- Enhanced dashboards
- Amazon SNS notifications

These features provide improved operational visibility and faster incident detection.

---

## AWS X-Ray

Enable AWS X-Ray to trace requests across AWS services.

Benefits include:

- End-to-end request tracing
- Performance bottleneck identification
- Dependency visualization
- Faster root cause analysis

---

## Infrastructure as Code

Provision the complete solution using Terraform.

Resources to manage include:

- Amazon S3
- AWS Lambda
- Amazon DynamoDB
- IAM Roles
- CloudWatch Dashboard
- CloudWatch Alarms
- Event Notifications

Infrastructure as Code will improve repeatability, consistency, and deployment automation.

---

## CI/CD Pipeline

Implement a continuous integration and deployment pipeline.

Potential services include:

- GitHub Actions
- AWS CodePipeline
- AWS CodeBuild

The pipeline can automate:

- Code validation
- Unit testing
- Security scanning
- Deployment
- Infrastructure provisioning

---

## Automated Testing

Introduce automated testing for the Lambda function.

Examples include:

- Unit tests
- Integration tests
- Event simulation tests
- End-to-end workflow validation

Automated testing increases confidence during future enhancements.

---

## Security Enhancements

Future security improvements may include:

- AWS KMS customer-managed encryption keys
- AWS Secrets Manager
- AWS Systems Manager Parameter Store
- Amazon Macie
- Amazon GuardDuty
- AWS Config Rules

These services strengthen governance and security posture.

---

# 📖 References

The following AWS documentation was used throughout the implementation of this phase.

## AWS Lambda

https://docs.aws.amazon.com/lambda/

---

## Amazon S3 Event Notifications

https://docs.aws.amazon.com/AmazonS3/latest/userguide/EventNotifications.html

---

## Amazon DynamoDB

https://docs.aws.amazon.com/amazondynamodb/

---

## DynamoDB Conditional Writes

https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.ConditionExpressions.html

---

## Amazon CloudWatch

https://docs.aws.amazon.com/AmazonCloudWatch/

---

## AWS IAM Best Practices

https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html

---

## AWS Well-Architected Framework

https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html

---

## AWS Well-Architected Reliability Pillar

https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html

---

# ✅ Phase Summary

At the end of this phase, the Event-Driven Image Processing application includes the following reliability improvements:

- Deterministic image identifiers
- Idempotent DynamoDB writes
- Duplicate event protection
- File extension validation
- Structured JSON logging
- Processing status tracking
- Improved exception handling
- Processing duration measurement
- Controlled error responses
- Production-inspired reliability practices

These enhancements significantly improve the application's robustness while keeping the architecture simple, scalable, and fully serverless.

The project is now ready for the next phase, where additional AWS services and architectural patterns will be introduced to further improve scalability, resilience, and production readiness.