# ADR-006: API Gateway HTTP API Strategy

## Status

Accepted

## Context

The application requires a public HTTPS endpoint to invoke AWS Lambda securely.

## Decision

Use **Amazon API Gateway HTTP API** with Lambda proxy integration.

Endpoint:

```text
POST /enhance
```

## Why

- Lower cost than REST API
- Native Lambda integration
- Built-in CORS support
- Lower latency
- Meets current project requirements

## Alternatives Considered

### API Gateway REST API

Rejected because it introduces additional complexity and cost.

### Lambda Function URL

Rejected because API Gateway provides better routing, CORS support, and future extensibility.

## Consequences

### Positive

- Clean HTTPS endpoint
- Easy integration with Lambda
- Simple CORS configuration
- Supports future expansion

### Trade-offs

- Additional AWS resource to manage

## Related ADRs

- ADR-001 – Serverless Core Architecture
- ADR-004 – Amazon Bedrock Integration Strategy
- ADR-005 – Lambda Service Layer Architecture
