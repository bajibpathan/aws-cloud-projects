# Secure Upload Design

## Purpose

Allow users to upload resumes securely without exposing AWS credentials or sending the resume file through API Gateway and Lambda.

---

## Architecture

User
↓
API Gateway
↓
Upload URL Lambda
↓
Generate Presigned URL
↓
User Uploads Directly to S3
↓
Private Resume Bucket

---

## Design Decisions

### Why use a presigned URL?

* Allows the frontend to upload directly to Amazon S3.
* AWS credentials are not exposed to the user.
* The resume file does not pass through Lambda.
* Reduces Lambda processing and API Gateway payload usage.
* Presigned URLs automatically expire.

### Why use API Gateway?

* Provides an HTTP endpoint for the frontend.
* Integrates directly with AWS Lambda.
* Supports CORS configuration.
* Authentication can be added later.

### API Type

* HTTP API

### API Route

```text
POST /upload-url
```

### Upload URL Lambda

The Lambda function:

* Receives the file name, content type and file size.
* Validates the upload request.
* Generates a unique object key.
* Creates an Amazon S3 presigned URL.
* Returns the upload URL to the frontend.

### Supported File Types

* PDF
* DOCX

### Maximum File Size

* 5 MB

### Object Key Structure

```text
uploads/<uuid>/<file-name>
```

A UUID is used to:

* Prevent file name conflicts.
* Create a unique folder for every upload.
* Make each uploaded resume easier to track.

### Presigned URL Expiry

* Presigned URLs expire after a short period.
* The expiry value is configured using a Lambda environment variable.

### Lambda Environment Variables

```text
UPLOAD_BUCKET_NAME
UPLOAD_PREFIX
PRESIGNED_URL_EXPIRY
MAX_FILE_SIZE_BYTES
```

### IAM Permissions

The Upload URL Lambda has permission to:

* Upload objects only to the resume bucket.
* Write objects only under the `uploads/` prefix.
* Write execution logs to Amazon CloudWatch.

### Security

* Resume bucket remains private.
* Block Public Access remains enabled.
* No AWS credentials are sent to the frontend.
* Presigned URLs are temporary.
* File type and file size are validated.
* Bucket names and configuration values are not hardcoded.

### CORS

CORS is configured for:

* The frontend origin.
* `POST` requests.
* `OPTIONS` requests.
* `Content-Type` header.

The production configuration should allow only the deployed frontend domain.
