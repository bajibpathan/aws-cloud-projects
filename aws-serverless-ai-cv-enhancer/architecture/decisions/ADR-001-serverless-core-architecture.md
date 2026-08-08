# ADR-001: Use a Serverless Core Architecture

## Status

Accepted

## Context

The Serverless AI CV Enhancer needs a simple architecture that can accept a request, run application logic, call a foundation model, and store enhancement history.

The project is intended to remain beginner-friendly, cost-conscious, and easy to operate.

The original project idea is based on four managed AWS services:

- Amazon API Gateway
- AWS Lambda
- Amazon Bedrock
- Amazon DynamoDB

## Decision

Use a serverless core architecture based on:

- Amazon API Gateway as the public API entry point
- AWS Lambda for request handling and application logic
- Amazon Bedrock for foundation model access
- Amazon DynamoDB for enhancement history

Do not introduce EC2 instances, containers, or always-running compute for the core implementation.

## Why

This approach keeps the architecture focused on the learning goals of the project while reducing operational overhead.

It also provides:

- Managed scaling
- Pay-per-use pricing
- No server patching
- No container management
- Simple integration between AWS services
- A clear architecture that is easy to explain in interviews

## Alternatives Considered

### Amazon EC2

EC2 would provide full control over the operating system and application runtime, but it would introduce server management, patching, scaling, and idle cost that are unnecessary for this project.

### Containers on Amazon ECS or Amazon EKS

Containers would be useful for more complex workloads, but they would add orchestration and deployment complexity without improving the core learning goals of this application.

## Consequences

### Positive

- Simple architecture
- Lower operational overhead
- Cost-efficient for low usage
- Easy to scale
- Strong fit for a small API-driven GenAI application

### Trade-offs

- The application depends on AWS managed services
- Some advanced runtime customization is limited compared with EC2 or containers
- Service-specific limits must be considered as the project grows
