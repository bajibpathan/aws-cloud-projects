# ADR-005: Lambda Service Layer Architecture

## Status

Accepted

---

## Context

As the Serverless AI CV Enhancer evolved, the AWS Lambda function became responsible for more than just parsing requests and returning responses.

The application now needs to:

- Validate incoming requests
- Build prompts dynamically
- Invoke Amazon Bedrock
- Handle AI service failures
- Return consistent API responses

Future phases will also introduce:

- Amazon API Gateway
- Amazon DynamoDB
- CloudWatch logging
- AWS X-Ray tracing

Keeping all of this logic inside a single `lambda_function.py` file would make the application difficult to maintain, test, and extend.

---

## Decision

Organize the Lambda application into small, focused modules, each with a single responsibility.

```text
lambda/
└── enhance_resume/
    ├── config.py
    ├── lambda_function.py
    ├── validator.py
    ├── response.py
    ├── prompts/
    │   └── prompt_builder.py
    ├── services/
    │   └── bedrock_service.py
    ├── local_test.py
    └── README.md
```

### Component Responsibilities

| Component | Responsibility |
|----------|----------------|
| `lambda_function.py` | Orchestrates the complete request flow |
| `validator.py` | Validates incoming requests |
| `response.py` | Builds API Gateway compatible responses |
| `config.py` | Centralizes application configuration |
| `prompts/prompt_builder.py` | Loads the approved prompt template and generates the final prompt |
| `services/bedrock_service.py` | Communicates with Amazon Bedrock using the Converse API |
| `local_test.py` | Executes local integration tests |

---

## Why

This design follows the **Single Responsibility Principle (SRP)** by ensuring each module has one clear responsibility.

Benefits include:

- Better separation of concerns
- Easier debugging
- Easier unit testing
- Improved readability
- Better maintainability
- Simpler future enhancements

This architecture also keeps AWS-specific integration isolated from the business logic, making the application easier to understand and extend.

---

## Alternatives Considered

### Option 1 – Single Lambda File

Implement all logic inside `lambda_function.py`.

```text
Lambda
├── Validation
├── Prompt Builder
├── Bedrock
├── Response
└── Configuration
```

**Rejected**

Reason:

- Difficult to maintain as the project grows
- Harder to test individual components
- Increased code complexity
- Poor separation of responsibilities

---

### Option 2 – Direct Bedrock Calls from Lambda

Invoke Amazon Bedrock directly from `lambda_function.py` without a dedicated service layer.

**Rejected**

Reason:

- Couples business logic with AWS service integration
- Makes model changes more difficult
- Reduces code reusability

---

## Consequences

### Positive

- Cleaner project structure
- Easier maintenance
- Better code organization
- Improved readability
- Easier testing
- Supports future expansion without increasing Lambda complexity
- Consistent pattern for adding future services such as DynamoDB and CloudWatch

### Trade-offs

- Introduces additional modules
- Requires developers to understand the project structure
- Slightly more files compared to a single-file Lambda implementation

---

## Future Impact

This architecture allows future integrations to follow the same pattern.

For example:

```text
services/
├── bedrock_service.py
├── history_service.py
├── logging_service.py
└── metrics_service.py
```

This keeps the Lambda handler focused on orchestration while individual services encapsulate their own responsibilities.

---

## Related ADRs

- **ADR-001** – Serverless Core Architecture
- **ADR-002** – Build Manually Before Infrastructure Automation
- **ADR-003** – Local-First Lambda Development and Validation
- **ADR-004** – Amazon Bedrock Integration Strategy