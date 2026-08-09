# ADR-008: Static Frontend Hosting Strategy

## Status

Accepted

---

## Context

The backend services were fully implemented using:

- AWS Lambda
- Amazon API Gateway
- Amazon Bedrock
- Amazon DynamoDB

Although functional, the application could only be accessed through API requests or local scripts.

A browser-based interface was required to demonstrate the complete application.

---

## Decision

The frontend will be implemented using:

- HTML
- CSS
- Vanilla JavaScript

and hosted using:

Amazon S3 Static Website Hosting.

---

## Rationale

This approach provides:

- Minimal operational overhead
- Very low cost
- Fully serverless deployment
- Simple architecture
- Easy maintenance
- Excellent learning opportunity

The frontend communicates directly with Amazon API Gateway using REST APIs.

---

## Alternatives Considered

### React

Pros

- Component-based
- Modern ecosystem

Rejected because:

- Adds unnecessary complexity
- Requires build tooling
- Does not align with the learning goals of this project

---

### AWS Amplify

Pros

- Managed frontend hosting
- Built-in CI/CD
- HTTPS support

Rejected because:

- Abstracts away deployment details
- Additional service to learn
- More complex than required for this project

---

### EC2 Web Server

Rejected because:

- Requires server management
- Higher operational overhead
- Not aligned with a serverless architecture

---

## Consequences

### Positive

- Low cost
- Fully serverless
- Easy deployment
- Simple maintenance
- Fast browser experience

### Trade-offs

Amazon S3 Static Website Hosting only supports HTTP.

For production deployments, Amazon CloudFront or AWS Amplify Hosting would typically be used to provide HTTPS, custom domains, and additional security features.

---

## Future Enhancements

Future improvements may include:

- Amazon CloudFront
- Custom domain
- HTTPS
- Amazon Cognito authentication
- Responsive design improvements

---

## Related ADRs

- ADR-001 – Serverless Core Architecture
- ADR-004 – Amazon Bedrock Integration Strategy
- ADR-006 – API Gateway HTTP API Strategy
- ADR-007 – DynamoDB History Data Model