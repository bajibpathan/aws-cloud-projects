# ADR-004: Use Amazon Cognito and API Gateway JWT Authorization

## Status

Accepted

---

## Date

2026-07-22

---

## Context

The resume upload API generates Amazon S3 presigned URLs that allow users to upload resume files to a private S3 bucket.

Because resumes may contain personally identifiable information, the API must not allow anonymous users to generate upload URLs.

The authentication solution needed to:

* Authenticate application users securely.
* Prevent unauthenticated API access.
* Avoid implementing custom password storage.
* Integrate with Amazon API Gateway.
* Support a future browser-based frontend.
* Scale without requiring dedicated authentication servers.

The following approaches were considered:

1. Build custom authentication inside AWS Lambda.
2. Use API keys.
3. Use Amazon Cognito User Pools with an API Gateway JWT authorizer.

---

## Decision

The application uses **Amazon Cognito User Pools** for user authentication and an **Amazon API Gateway JWT authorizer** to protect the upload API.

The authentication flow is:

```text
User
  │
  ▼
Amazon Cognito
  │
  │ Access Token
  ▼
Client Application
  │
  │ Authorization: Bearer <access-token>
  ▼
API Gateway JWT Authorizer
  │
  │ Token Valid
  ▼
POST /upload-url
  │
  ▼
AWS Lambda
  │
  ▼
S3 Presigned Upload URL
```

The client authenticates with Amazon Cognito and receives a JSON Web Token.

The client includes the access token in the HTTP `Authorization` header when calling the upload API.

API Gateway validates the token before invoking the Lambda function.

Requests without a valid token are rejected with:

```text
401 Unauthorized
```

---

## Rationale

### Managed User Authentication

Amazon Cognito manages:

* User registration
* Password policies
* Password storage
* Authentication
* Account recovery
* Token generation
* Token expiration

This avoids building and maintaining a custom authentication system.

### API-Level Protection

The JWT authorizer validates requests before they reach AWS Lambda.

This means unauthorized requests do not invoke the Lambda function.

### Improved Security

API Gateway validates:

* Token signature
* Token issuer
* Token audience or client identifier
* Token expiration

Only users authenticated through the configured Cognito user pool can access the protected route.

### Scalability

Amazon Cognito and API Gateway are managed services that scale automatically.

The application does not require dedicated authentication servers.

### Future Frontend Integration

The Cognito app client can later be integrated with a browser-based frontend using an OAuth authorization-code flow with PKCE.

---

## Configuration

### Cognito User Pool

```text
ai-resume-builder-users-dev
```

### Cognito App Client

```text
ai-resume-builder-web-client-dev
```

The application client is configured as a public client without a client secret.

Browser applications cannot securely store client secrets.

### API Gateway Authorizer

```text
cognito-jwt-authorizer-dev
```

### Identity Source

```text
$request.header.Authorization
```

### Protected Route

```text
POST /upload-url
```

### AWS Region

```text
us-east-1
```

---

## Alternatives Considered

### Option 1 – Custom Authentication in Lambda

#### Advantages

* Complete control over authentication logic.
* Customizable user-management workflow.

#### Disadvantages

* Requires secure password storage.
* Requires password-reset functionality.
* Increases security risk.
* Adds significant development and maintenance effort.
* Lambda would need to process every authentication request.

#### Decision

Rejected.

---

### Option 2 – API Keys

#### Advantages

* Simple to configure.
* Useful for API usage tracking.

#### Disadvantages

* API keys do not authenticate individual users.
* Keys may be copied or shared.
* They are not intended to protect user accounts.
* They do not provide user registration or password management.

#### Decision

Rejected.

---

### Option 3 – Cognito User Pools with JWT Authorization

#### Advantages

* Managed user authentication.
* Secure password handling.
* Native integration with API Gateway.
* Token-based authorization.
* Automatic scaling.
* Supports future frontend integration.

#### Disadvantages

* Adds Cognito configuration complexity.
* Clients must obtain and manage JWT tokens.
* OAuth configuration will be required when the frontend login experience is implemented.

#### Decision

Accepted.

---

## Consequences

### Positive

* The upload API is no longer publicly accessible.
* Unauthorized requests are blocked before Lambda invocation.
* Passwords are managed securely by Amazon Cognito.
* Authentication scales automatically.
* The architecture supports future frontend authentication.
* No custom authentication server is required.

### Negative

* The client must obtain and send an access token.
* Cognito introduces additional configuration and testing.
* Token expiration and refresh must be handled by the future frontend.
* Users must be managed within the Cognito user pool.

---

## Security Considerations

* The app client does not contain a client secret.
* Access tokens must never be stored in GitHub.
* Tokens must not appear in project screenshots.
* The upload API accepts tokens only from the configured Cognito user pool.
* Access tokens expire automatically.
* HTTPS must be used for API communication.
* Authorization scopes may be introduced later for more granular access control.

---

## Testing

The following tests were completed:

```text
Request without token
        ↓
401 Unauthorized
```

```text
Valid Cognito credentials
        ↓
Access token issued
        ↓
Authenticated API request
        ↓
200 OK
        ↓
Presigned upload URL returned
```

```text
Presigned URL
        ↓
Resume uploaded
        ↓
Private Amazon S3 bucket
```

---

## Related Components

* Amazon Cognito User Pools
* Amazon API Gateway
* API Gateway JWT Authorizer
* AWS Lambda
* Amazon S3
* AWS Identity and Access Management
* Amazon CloudWatch

---

## References

* Amazon Cognito User Pools
* API Gateway HTTP API JWT Authorizers
* AWS Well-Architected Framework – Security Pillar
* AWS Well-Architected Framework – Operational Excellence Pillar
