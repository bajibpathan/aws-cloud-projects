# ADR-005 – Implement Idempotent Processing for S3 Events

## Status

**Accepted**

---

# Context

Amazon S3 Event Notifications use an **at-least-once delivery** model.

This means the same event may be delivered more than once under certain conditions.

Possible scenarios include:

- Network retries
- Temporary service interruptions
- Internal retry mechanisms
- Distributed system behavior

Without additional safeguards, duplicate events could cause:

- Duplicate metadata records
- Incorrect processing statistics
- Increased Lambda executions
- Higher DynamoDB write costs
- Inconsistent application state

The application requires a reliable mechanism to ensure that processing the same event multiple times produces the same result.

---

# Decision

The application implements **idempotent processing**.

Each uploaded image generates a deterministic **ImageId** based on the object being processed.

Before writing metadata to Amazon DynamoDB, the Lambda function performs a conditional write.

If an item with the same `ImageId` already exists, the write is rejected and the duplicate event is ignored.

This ensures that each image is processed only once from a business perspective, even if the underlying event is delivered multiple times.

---

# Alternatives Considered

## No Duplicate Protection

### Pros

- Simpler implementation
- Less application logic

### Cons

- Duplicate metadata
- Inconsistent reporting
- Higher DynamoDB costs
- Unnecessary Lambda processing
- Reduced reliability

---

## Maintain Processed IDs in Memory

### Pros

- Fast duplicate detection

### Cons

- Does not survive Lambda execution environments
- Ineffective because Lambda is stateless
- Cannot scale reliably

---

## Amazon SQS FIFO Queue

### Pros

- Supports message deduplication
- Ordered message processing

### Cons

- Additional infrastructure
- Additional cost
- Unnecessary complexity for this project
- Amazon S3 Event Notifications do not directly support FIFO queues

---

## DynamoDB Conditional Writes (Selected)

### Pros

- Simple implementation
- Durable duplicate protection
- Works across all Lambda executions
- Supports serverless architecture
- Minimal operational overhead

### Cons

- Slightly more application logic
- Requires conditional write expressions

---

# Consequences

## Positive

- Prevents duplicate metadata records
- Ensures consistent application state
- Improves reliability
- Reduces unnecessary database writes
- Reduces storage growth
- Supports distributed event processing
- Aligns with AWS serverless best practices

## Negative

- Additional implementation complexity
- Requires deterministic identifier generation
- Conditional write failures must be handled gracefully

These trade-offs were considered acceptable because the increase in reliability significantly outweighs the additional implementation effort.

---

# Why Idempotency Was Necessary

Amazon S3 Event Notifications guarantee **at-least-once delivery**, not **exactly-once delivery**.

Example without idempotency:

```text
Upload Image

↓

S3 Event

↓

Lambda

↓

Store Metadata

↓

Duplicate Event

↓

Lambda

↓

Store Metadata Again
```

Result:

- Duplicate records
- Incorrect reporting
- Additional costs

---

With idempotent processing:

```text
Upload Image

↓

S3 Event

↓

Lambda

↓

Generate ImageId

↓

Conditional PutItem

↓

Metadata Stored

↓

Duplicate Event

↓

Generate Same ImageId

↓

Conditional PutItem

↓

Duplicate Ignored
```

Result:

- Single metadata record
- Consistent application state
- Reduced operational cost
- Reliable event processing

---

# Impact on the Project

Implementing idempotent processing improves multiple aspects of the solution.

### Reliability

- Prevents duplicate records
- Maintains data consistency
- Handles retry scenarios safely

---

### Cost Optimization

- Reduces unnecessary DynamoDB writes
- Prevents duplicate storage
- Avoids additional processing

---

### Operational Excellence

- Simplifies troubleshooting
- Produces consistent monitoring metrics
- Reduces operational noise

---

### Scalability

As event volume increases, duplicate events become more likely.

Idempotent processing ensures the application continues to behave correctly without requiring changes to the overall architecture.

---

# Alignment with AWS Well-Architected Framework

This decision supports several AWS Well-Architected pillars.

| Pillar | Benefit |
|----------|---------|
| Reliability | Prevents inconsistent processing caused by duplicate events |
| Operational Excellence | Simplifies troubleshooting and operational monitoring |
| Cost Optimization | Eliminates unnecessary processing and storage |
| Performance Efficiency | Reduces redundant database operations |

---

# Lessons Learned

Distributed systems cannot assume that events are delivered exactly once.

Designing applications to tolerate duplicate events is an important reliability practice.

Idempotent processing ensures that repeated execution produces the same business outcome, improving consistency, reducing operational risk, and making the application more resilient.

---

# References

- Amazon S3 Event Notifications Documentation
- AWS Lambda Best Practices
- Amazon DynamoDB Conditional Writes
- AWS Well-Architected Framework
- AWS Well-Architected Reliability Pillar