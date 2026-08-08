# ADR-004: Use Amazon Bedrock Converse API for Foundation Model Integration

## Status

Accepted

## Context

The application needs to integrate a foundation model for resume enhancement while remaining portable across supported models and minimizing vendor-specific request handling.

## Decision

Use Amazon Bedrock as the AI platform and integrate the model using the **Converse API**.

The initial implementation uses **Anthropic Claude Sonnet** through Amazon Bedrock.

## Why

Using Bedrock provides:

- Managed access to foundation models
- Unified security through IAM
- No direct integration with individual model providers
- Ability to change supported models with minimal application changes

The Converse API provides a consistent interface across supported models, reducing model-specific implementation details.

## Alternatives Considered

### InvokeModel API

Works well but requires model-specific request formats and makes switching models more difficult.

### Direct provider APIs

Calling providers directly would increase operational complexity, require separate authentication, and reduce portability.

## Consequences

### Positive

- Cleaner application architecture
- Easier model replacement in the future
- Centralized security using AWS IAM
- Better alignment with AWS best practices

### Trade-offs

- The application depends on Amazon Bedrock availability.
- Some model-specific features may require additional implementation if used in the future.
