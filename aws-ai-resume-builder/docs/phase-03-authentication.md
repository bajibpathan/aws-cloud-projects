# Authentication Design

## Purpose

Allow only authenticated users to access the resume upload API.

---

## Architecture

User
↓
Amazon Cognito
↓
JWT Token
↓
API Gateway JWT Authorizer
↓
Protected Upload API
↓
Upload URL Lambda
↓
Amazon S3 Presigned URL

---

## Design Decisions

### Why use Amazon Cognito?

* Provides managed user registration and sign-in.
* Securely stores and manages user credentials.
* Generates JSON Web Tokens.
* Integrates directly with Amazon API Gateway.
* Avoids creating a custom authentication system.

### Cognito User Pool

The User Pool manages:

* User registration
* User sign-in
* Password policies
* Email verification
* Account recovery
* Authentication tokens

### Sign-In Method

* Email address

### App Client

A Cognito App Client is created for the frontend application.

Configuration:

* Client secret disabled
* User authentication flows enabled
* Refresh token flow enabled

### Why disable the client secret?

A browser-based application cannot securely store a client secret.

The App Client therefore does not use a secret.

### Authentication Tokens

Amazon Cognito generates:

* ID token
* Access token
* Refresh token

The access token is used to call the protected upload API.

### Authorization Header

```text
Authorization: Bearer <access-token>
```

### API Gateway JWT Authorizer

The JWT authorizer validates:

* Token signature
* Token expiry
* Token issuer
* App Client audience
* Authorization header

### Protected Route

```text
POST /upload-url
```

The JWT authorizer is attached to this route.

### Request Flow

Valid token:

```text
User
    ↓
API Gateway
    ↓
JWT Validated
    ↓
Lambda Invoked
```

Invalid or missing token:

```text
User
    ↓
API Gateway
    ↓
401 Unauthorized
```

The Lambda function is not invoked when authentication fails.

### CORS

API Gateway CORS allows:

* The frontend origin
* `POST`
* `OPTIONS`
* `Content-Type`
* `Authorization`

### Security

* User passwords are managed by Amazon Cognito.
* Passwords are not stored in the application.
* Tokens are not committed to GitHub.
* Tokens should not be written to CloudWatch logs.
* API Gateway validates tokens before invoking Lambda.
* The upload bucket remains private.
* The App Client does not contain a client secret.
