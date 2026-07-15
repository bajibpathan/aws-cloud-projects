# ADR-001 – Use Amazon S3 for Object Storage

## Status

**Accepted**

---

# Context

The application requires a storage service capable of storing user-uploaded image files.

The storage solution should:

- Scale automatically
- Provide high durability
- Support event-driven processing
- Integrate natively with AWS Lambda
- Require minimal operational management

The project stores uploaded images rather than block-level or shared file-system data.

---

# Decision

Amazon S3 was selected as the primary storage service.

The bucket is configured with:

- Versioning
- Server-Side Encryption
- Bucket Owner Enforced Object Ownership
- Event Notifications

Amazon S3 acts as both the storage layer and the event source for the application.

---

# Alternatives Considered

## Amazon EBS

### Pros

- High-performance block storage
- Suitable for EC2 workloads

### Cons

- Requires an EC2 instance
- Cannot directly trigger Lambda
- Not designed for object storage
- Additional infrastructure management

---

## Amazon EFS

### Pros

- Shared file system
- Supports multiple EC2 instances

### Cons

- Higher operational complexity
- Requires network file system access
- Not designed for simple image uploads
- No native event notification model

---

## Local File System

### Pros

- Simple for development

### Cons

- Not scalable
- Not durable
- Single point of failure
- Unsuitable for cloud-native applications

---

# Consequences

## Positive

- Fully managed storage
- Virtually unlimited scalability
- High durability
- Native AWS Lambda integration
- Supports Versioning
- Supports Lifecycle Management
- Supports Server-Side Encryption

## Negative

- Event Notifications use at-least-once delivery
- Versioning increases storage usage
- HTTP website endpoint does not support HTTPS directly

These trade-offs were acceptable for this project.

---

# References

- Amazon S3 Documentation
- Amazon S3 Event Notifications
- AWS Well-Architected Framework
