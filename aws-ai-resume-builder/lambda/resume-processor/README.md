# Resume Processor Lambda

This Lambda function processes resumes uploaded to Amazon S3.

## Responsibilities

- Receive the S3 upload event
- Read the uploaded resume
- Call Amazon Textract
- Extract text and confidence information
- Generate structured JSON
- Store the processed JSON in Amazon S3

## Trigger

Amazon S3 ObjectCreated event.

## Environment Variables

| Variable | Description |
|----------|-------------|
| PROCESSED_BUCKET_NAME | Destination bucket for JSON output |
| OUTPUT_PREFIX | Output folder, such as `processed/` |

## Required IAM Permissions

- `s3:GetObject`
- `s3:PutObject`
- `textract:DetectDocumentText`
- CloudWatch Logs permissions

## Supported Input

- Valid PDF documents supported by the implemented Textract API

## Output

```text
processed/<resume-id>/<filename>.json