# ADR-006: Use Amazon Bedrock for AI Resume Analysis

## Status

Accepted

## Context

Amazon Textract extracts text from uploaded resumes, but the extracted content is not organized into a consistent structure that can be used directly to generate a portfolio website.

The application requires an AI processing layer that can:

* Understand resume content
* Identify common resume sections
* Organize information into structured JSON
* Follow strict instructions
* Avoid inventing missing information
* Integrate with the existing AWS serverless architecture

## Decision

Use Amazon Bedrock with Anthropic Claude Sonnet 4.6 to transform Textract-generated resume text into structured JSON.

The AI processing logic will run in a separate Lambda function named:

```text
ai-resume-analyzer
```

The Lambda will invoke the model using the Amazon Bedrock Converse API and the following inference profile:

```text
us.anthropic.claude-sonnet-4-6
```

Textract output and AI output will be stored in the same processed-data bucket under different prefixes:

```text
textract-output/
ai-output/
```

## Reasons

* Amazon Bedrock is a managed AWS service.
* It integrates with IAM and the AWS SDK.
* No model infrastructure needs to be maintained.
* Claude performs well at instruction following and structured extraction.
* A separate Lambda keeps document extraction and AI processing independent.
* Separate S3 prefixes provide logical isolation without adding an unnecessary bucket.
* Structured JSON separates resume content from website presentation.

## Alternatives Considered

### Generate HTML directly using the model

Rejected because it would tightly couple AI content processing with website design.

Structured JSON allows the website generator to control:

* HTML structure
* CSS
* Templates
* Accessibility
* Validation
* Future design changes

### Run an open-source model on Amazon EC2 or Amazon SageMaker

Rejected for the current project because it would introduce model hosting, scaling, patching and operational overhead.

### Use the direct foundation-model ID

Rejected because Claude Sonnet 4.6 did not support on-demand throughput through the direct model ID.

The following value failed:

```text
anthropic.claude-sonnet-4-6
```

The inference profile was required:

```text
us.anthropic.claude-sonnet-4-6
```

### Create a separate AI-output bucket

Rejected because Textract and AI output are both intermediate processed artifacts. Prefix-level separation provides sufficient organization for the current requirements.

## Consequences

### Positive

* Managed AI integration
* Strong structured-data generation
* Independent scaling of AI processing
* Clear separation of responsibilities
* Easier troubleshooting
* Output can support multiple website templates
* Token usage can be stored for cost analysis

### Negative

* Bedrock usage introduces model-inference cost.
* Output must still be validated.
* Model behavior can vary.
* Cross-Region inference may require broader IAM or organizational permissions.
* Sensitive resume information is sent to a managed foundation-model service.
* Retry and failure-handling mechanisms must be added for production readiness.

## Security Controls

* Use a dedicated Lambda execution role.
* Restrict S3 access to required prefixes.
* Do not log complete resume text.
* Treat resume text as untrusted input.
* Instruct the model to ignore embedded instructions.
* Validate model output before storage.
* Keep all S3 buckets private.
* Do not commit JWTs, presigned URLs or personal resume data to GitHub.

## Outcome

The application successfully converts Textract-generated resume text into validated structured JSON using Claude Sonnet 4.6 through Amazon Bedrock.

The generated data is stored under the `ai-output/` prefix and is ready for the portfolio website generation phase.
