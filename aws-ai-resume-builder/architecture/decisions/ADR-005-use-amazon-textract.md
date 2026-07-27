# ADR-005: Use Amazon Textract for Resume Text Extraction

## Status

Accepted

## Context

The application requires text extraction from uploaded resume documents before AI-based analysis can be performed.

## Decision

Use Amazon Textract to extract text from resumes stored in Amazon S3.

## Reasons

- Fully managed AWS service
- Native integration with Amazon S3 and AWS Lambda
- No OCR infrastructure to maintain
- Suitable for serverless architectures
- Returns text and confidence information

## Alternatives Considered

### Tesseract OCR

Rejected because it would require packaging, maintenance, scaling, and additional Lambda dependencies.

### Custom OCR Service

Rejected because it would increase operational complexity and development effort.

### Amazon Comprehend

Not selected because Comprehend analyzes existing text but does not perform OCR on PDF documents.

## Consequences

### Benefits

- Reduced operational overhead
- Serverless integration
- Automatic scaling
- Structured OCR response

### Trade-offs

- Usage-based cost
- Document format and page limitations depend on the Textract API used
- Additional processing may be required for complex layouts