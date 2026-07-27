# Resume Processing Design

## Purpose

Automatically extract text from uploaded resumes and store the extracted content as structured JSON for AI analysis.

---

## Architecture

Resume Uploaded
↓
Private Resume Bucket
↓
S3 Object Created Event
↓
Resume Processor Lambda
↓
Amazon Textract
↓
Extracted Resume Text
↓
Structured JSON
↓
Processed Folder in Amazon S3

---

## Design Decisions

### Why use event-driven processing?

* Resume processing starts automatically after upload.
* The frontend does not need to call another processing API.
* Components remain loosely coupled.
* The solution scales automatically.
* Failed processing can be monitored separately from uploads.

### S3 Event Notification

The resume bucket invokes the processing Lambda when a new object is created.

Configuration:

```text
Event: ObjectCreated
Prefix: uploads/
Destination: Resume Processor Lambda
```

The prefix prevents the Lambda from processing unrelated objects.

### Resume Processor Lambda

The Lambda function:

* Receives the Amazon S3 event.
* Reads the bucket name and object key.
* Validates the uploaded document.
* Sends the document to Amazon Textract.
* Extracts text lines and confidence values.
* Creates structured JSON.
* Stores the result in Amazon S3.
* Writes processing logs to Amazon CloudWatch.

### Why use Amazon Textract?

* Fully managed document text extraction service.
* Integrates directly with Amazon S3 and AWS Lambda.
* No OCR servers or libraries need to be maintained.
* Returns extracted text and confidence values.
* Supports serverless document-processing workflows.

### Textract API

The current implementation uses:

```text
DetectDocumentText
```

This is suitable for the current resume-processing implementation.

Asynchronous Textract processing may be evaluated later for larger or multi-page documents.

### Input Structure

```text
uploads/<uuid>/<resume-file>
```

### Output Structure

```text
processed/<uuid>/<resume-file>.json
```

### Structured JSON

The generated JSON contains:

* Source document name
* Source bucket and object key
* Processing timestamp
* Extracted full text
* Individual text lines
* Confidence values
* Processing metadata

### Lambda Environment Variables

```text
PROCESSED_BUCKET_NAME
OUTPUT_PREFIX
```

### IAM Permissions

The Resume Processor Lambda has permission to:

* Read uploaded resumes from the `uploads/` prefix.
* Write processed JSON under the `processed/` prefix.
* Call Amazon Textract.
* Write logs to Amazon CloudWatch.

Required actions include:

```text
s3:GetObject
s3:PutObject
textract:DetectDocumentText
```

### Error Handling

The Lambda handles:

* Missing S3 objects
* Access denied errors
* Unsupported documents
* Amazon Textract failures
* Invalid event records
* Unexpected processing errors

Errors are written to Amazon CloudWatch Logs.

### Security

* Resume bucket remains private.
* Processed resume data remains private.
* Lambda follows least-privilege IAM permissions.
* Resource names are configured using environment variables.
* Uploaded resumes are not made publicly accessible.
* Resume text is stored only for downstream application processing.
* Sensitive resume data should not be written unnecessarily to logs.

### Troubleshooting

The following issues were identified during implementation:

#### Missing S3 Permission

The Lambda role initially did not have:

```text
s3:GetObject
```

The permission issue was confirmed using the IAM Policy Simulator and corrected using a least-privilege policy.

#### Invalid S3 Object Error

Amazon Textract could not access the uploaded object because the Lambda execution role did not have permission to read it.

#### Unsupported Document Error

The test document was not supported or was not a valid PDF.

Testing was completed using a valid supported PDF document.

#### Textract Subscription Error

Amazon Textract initially returned a subscription-related error.

The service access issue was resolved before completing the test.

### Resume Retention

Uploaded resumes continue to follow the lifecycle configuration defined in the storage phase.

* Uploaded resumes are deleted after 7 days.
* Processed JSON retention can be evaluated separately based on application requirements.
