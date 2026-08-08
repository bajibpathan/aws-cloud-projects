# Phase 5 – Lambda and Amazon Bedrock Integration

## Overview

In this phase, the application was transformed from a validated serverless backend into a working Generative AI application by integrating AWS Lambda with Amazon Bedrock.

The validated request is converted into a prompt, sent to Amazon Bedrock using the Converse API, and the enhanced resume bullets are returned to the caller.

---

## Objectives

- Integrate AWS Lambda with Amazon Bedrock
- Reuse the approved prompt template from Phase 4
- Build prompts dynamically
- Call Amazon Bedrock using the Converse API
- Return AI-generated resume bullets
- Handle Bedrock errors gracefully

---

## Architecture

```text
Client
   │
   ▼
AWS Lambda
   │
   ├── Validate Request
   ├── Build Prompt
   ├── Call Amazon Bedrock
   └── Return Response
```

---

## Implementation

### New Components

```text
lambda/enhance_resume/
├── config.py
├── prompt_builder.py
├── services/
│   └── bedrock_service.py
```

### Responsibilities

**config.py**

- Centralizes application configuration
- Stores model ID, Region and inference settings

**prompt_builder.py**

- Loads the approved prompt template
- Replaces template placeholders
- Produces the final prompt

**bedrock_service.py**

- Creates the Bedrock Runtime client
- Calls the Converse API
- Returns generated text
- Handles Bedrock service exceptions

---

## Bedrock Integration

- Service: Amazon Bedrock
- API: Converse API
- Runtime Client: boto3 bedrock-runtime
- Authentication: AWS IAM Credentials
- Prompt Version: resume-enhancer-v1.txt

---

## Testing

### Validation Tests

| Test | Result |
|------|--------|
| Valid Request | ✅ Passed |
| Missing Body | ✅ Passed |
| Invalid JSON | ✅ Passed |
| Missing Job Description | ✅ Passed |
| Empty Job Description | ✅ Passed |
| Resume Bullets Not List | ✅ Passed |
| Empty Resume Bullets | ✅ Passed |

### Bedrock Integration

The application successfully generated enhanced resume bullets through Amazon Bedrock after configuring the correct inference profile.

---

## Lessons Learned

- Validate requests before invoking a paid AI service.
- Keep prompt templates outside application code.
- Separate prompt building from model invocation.
- Use environment variables for model configuration.
- Amazon Nova inference requires an inference profile instead of direct on-demand model invocation.

---

## Deliverables

- Lambda integrated with Amazon Bedrock
- Dynamic prompt generation
- Successful local end-to-end testing
- Graceful Bedrock error handling

---

## Next Phase

**Phase 6 – API Gateway Integration**
