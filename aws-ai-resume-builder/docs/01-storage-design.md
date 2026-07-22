# Storage Design

## Purpose

Store uploaded resumes securely and store generated portfolio websites separately.

---

## Architecture

Resume Upload
    ↓
Resume Bucket (Private)
    ↓
Resume Processing

Generated Website
    ↓
Website Bucket (Private)
    ↓
CloudFront

---

## Design Decisions

### Why two buckets?

- Separation of concerns
- Different lifecycle policies
- Simpler IAM permissions

### Why private buckets?

- Resumes contain sensitive information.
- Website delivery will happen through CloudFront.

### Encryption

- SSE-S3

### Resume Bucket Lifecycle

Delete uploaded resumes after **7 days** using an Amazon S3 Lifecycle Rule.

### Versioning

Resume bucket:
- Disabled

Website bucket:
- To be evaluated later


### Generated Website Bucket

The generated website bucket stores HTML, CSS, JavaScript and static assets.

Configuration:

* Private bucket
* Block Public Access enabled
* SSE-S3 encryption
* Versioning enabled
* Delivered through CloudFront later
* S3 static website hosting disabled
