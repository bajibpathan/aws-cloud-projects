# Sample Resumes

This directory contains sanitized resume files used to test the AWS AI Resume Builder.

## Data Privacy

Do not store or commit real resumes containing personal, confidential or sensitive information.

Examples of information that must be removed or replaced include:

* Full legal names
* Personal email addresses
* Phone numbers
* Home addresses
* Employer-confidential information
* Employee or customer identifiers
* Government-issued identification numbers
* Financial information

## Recommended Test Data

Use a fictional resume containing sample information such as:

```text
Name: Alex Morgan
Role: Cloud Support Engineer
Email: alex.morgan@example.com
Phone: 000-000-0000
Location: Toronto, Ontario
```

The work experience, education and technical skills should also be fictional or fully anonymized.

## Supported Test Files

The initial implementation will focus on:

* PDF resumes
* Microsoft Word documents, if supported during implementation

Additional document formats may be evaluated later.

## Naming Convention

Use clear filenames such as:

```text
sample-resume.pdf
sample-cloud-engineer-resume.pdf
sample-devops-engineer-resume.docx
```

Do not use filenames containing real names, employee numbers or other sensitive information.

## Testing Purpose

Sample resumes will be used to validate:

* S3 presigned URL uploads
* File type validation
* Amazon Textract text extraction
* Amazon Bedrock resume transformation
* JSON response validation
* Static portfolio website generation
* Error-handling scenarios
