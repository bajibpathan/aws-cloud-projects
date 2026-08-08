# ADR-003: Develop and Validate the Lambda Locally Before AWS Integration

## Status

Accepted

## Context

The backend Lambda function needs to receive API Gateway-style requests, parse the request body, validate input, and eventually call Amazon Bedrock.

Deploying every small code change to AWS would slow down development and make debugging more difficult.

Invalid requests should also be rejected before any paid foundation model call is made.

## Decision

Develop and test the Lambda locally first using simulated API Gateway events.

The Lambda will validate requests before any Amazon Bedrock integration is executed.

The initial validation covers:

- Missing request body
- Invalid JSON
- Missing job description
- Empty job description
- Missing resume bullets
- Invalid resume bullet types
- Empty resume bullet values

## Why

Local-first development makes it possible to test application logic quickly without repeatedly deploying to AWS.

Validating requests before Bedrock also prevents unnecessary model calls and improves API reliability.

This approach provides:

- Faster feedback during development
- Easier debugging
- Lower development cost
- Better separation between input validation and AI processing
- More predictable API behavior

## Alternatives Considered

### Deploy Every Change Directly to AWS Lambda

This would test the application in the real AWS environment immediately, but it would create a slower development loop and make simple code issues more difficult to isolate.

### Rely Only on Frontend Validation

Frontend validation improves user experience but cannot be trusted as the only validation layer because clients can call the API directly.

Backend validation is still required.

## Consequences

### Positive

- Faster local development
- Invalid requests are rejected early
- Bedrock calls are only made for valid input
- Easier testing of failure scenarios
- Cleaner separation of responsibilities

### Trade-offs

- Local tests do not reproduce every aspect of the AWS runtime
- Final behavior must still be tested after deployment to AWS
