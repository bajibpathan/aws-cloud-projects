# ADR-001: Use Separate S3 Buckets

## Status

Accepted

## Context

The application needs to store two different types of content:

* Uploaded resumes
* Generated portfolio website files

Uploaded resumes may contain sensitive personal information and are required only temporarily. Generated website files need longer retention and will eventually be delivered through Amazon CloudFront.

Using one bucket would require more complex permissions, lifecycle rules and event configurations.

## Decision

Use two separate Amazon S3 buckets:

1. A private resume upload bucket
2. A private generated website bucket

The resume bucket will store temporary source documents.

The website bucket will store generated HTML, CSS and static assets.

## Reasons

* Separates sensitive resumes from generated website content
* Simplifies IAM permissions
* Allows independent lifecycle policies
* Reduces the risk of exposing uploaded resumes
* Keeps S3 event notifications isolated
* Makes resource purposes easier to understand

## Alternatives Considered

### Single S3 Bucket with Prefixes

Example:

```text
uploads/
websites/
```

This would reduce the number of buckets but would require more complex permissions, lifecycle filters and bucket policies.

## Consequences

### Benefits

* Clear separation of responsibilities
* Simpler security controls
* Independent retention settings
* Easier troubleshooting and maintenance

### Trade-offs

* An additional S3 bucket must be managed
* Infrastructure configuration contains more resources

## Outcome

Two private S3 buckets will be used because the uploaded resumes and generated websites have different security, access and retention requirements.
