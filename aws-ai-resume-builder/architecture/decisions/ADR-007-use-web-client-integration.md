# ADR-006: Browser-Based Web Client Integration

**Status:** Accepted

**Date:** 2026-07-27

## Context

The initial phases of the AI Resume Builder focused on building the backend infrastructure, including secure file uploads, authentication, resume processing, and AI-powered resume analysis. These components were tested independently using API testing tools.

To make the application usable by end users, a browser-based frontend was required. The frontend needed to authenticate users, securely upload resume files, and interact with backend services without exposing AWS credentials.

The solution also needed to:

- Authenticate users securely.
- Prevent unauthorized API access.
- Keep the Amazon S3 bucket private.
- Avoid sending large files through Lambda.
- Support direct browser uploads.
- Follow AWS security best practices.

---

## Decision

A lightweight browser-based frontend was implemented using HTML, CSS, and Vanilla JavaScript.

Authentication is handled by Amazon Cognito User Pools. After successful authentication, Cognito issues JWT tokens that are stored in the browser session.

The frontend uses the Cognito Access Token when calling a protected Amazon API Gateway HTTP API endpoint. A JWT Authorizer validates the token before allowing access to the backend Lambda function.

Instead of uploading files through Lambda, the backend generates a short-lived Amazon S3 Presigned URL. The browser then uploads the resume directly to Amazon S3 using this URL.

The final upload flow is:

```text
Browser
    │
    ▼
Amazon Cognito
    │
    ▼
HTTP API
    │
    ▼
Upload URL Lambda
    │
    ▼
Amazon S3 (Presigned URL)
    │
    ▼
Resume Processing Pipeline
```

---

## Rationale

This approach provides several advantages.

### Secure Authentication

Amazon Cognito manages user authentication without requiring custom authentication logic.

Benefits:

- Managed user authentication
- Secure JWT token generation
- No password handling in Lambda
- Easy integration with API Gateway

---

### HTTP API with JWT Authorizer

Amazon API Gateway HTTP API was selected instead of REST API because it provides native JWT authorization with lower latency and reduced cost.

Benefits:

- Lower request latency
- Lower operational cost
- Native JWT Authorizer support
- Simplified configuration
- Well suited for serverless workloads

---

### Direct Amazon S3 Upload

The application uses Amazon S3 Presigned URLs to upload resumes directly from the browser.

Benefits:

- Eliminates Lambda file streaming
- Reduces Lambda execution time
- Lowers API Gateway payload processing
- Supports larger file uploads
- Improves scalability

---

### Backend Validation

Although the browser validates the selected file, the backend performs its own validation before generating the Presigned URL.

The backend validates:

- Filename
- File type
- File size
- Upload permissions

This prevents malicious or modified client requests from bypassing browser validation.

---

## Consequences

### Positive

- Secure browser authentication using Amazon Cognito.
- No AWS credentials are exposed to the client.
- Private Amazon S3 bucket is maintained.
- Reduced backend processing and cost.
- Scalable upload architecture.
- Cleaner separation between frontend and backend.
- Alignment with AWS recommended patterns for browser uploads.

### Negative

- Additional Cognito configuration is required.
- Browser session management becomes necessary.
- CORS must be configured for both API Gateway and Amazon S3.
- JWT token expiration must be handled by the frontend.

---

## Alternatives Considered

### Upload Through Lambda

```
Browser
    │
    ▼
Lambda
    │
    ▼
Amazon S3
```

Pros

- Simple implementation
- No browser upload logic

Cons

- Larger Lambda payloads
- Higher execution cost
- Longer response times
- Less scalable for large files

This option was rejected.

---

### Public Amazon S3 Upload

Making the S3 bucket publicly writable was considered.

This option was rejected because it would:

- Allow unauthorized uploads
- Expose storage resources
- Increase security risks
- Violate least privilege principles

---

### Custom Authentication

A custom authentication system using Lambda was also considered.

This option was rejected because Amazon Cognito provides:

- Managed authentication
- JWT token issuance
- Password policies
- MFA support
- User lifecycle management

without additional implementation effort.

---

## Security Considerations

The following security controls were implemented:

- Amazon Cognito User Pool authentication
- JWT Authorizer on API Gateway HTTP API
- Access Token used for API authorization
- Private Amazon S3 bucket
- Short-lived Presigned URLs
- Backend file validation
- Filename sanitization
- Session-based token storage
- No AWS credentials stored in the browser

---

## References

- AWS Well-Architected Framework – Security Pillar
- Amazon Cognito User Pools
- Amazon API Gateway HTTP APIs
- Amazon S3 Presigned URLs
- JSON Web Tokens (JWT)