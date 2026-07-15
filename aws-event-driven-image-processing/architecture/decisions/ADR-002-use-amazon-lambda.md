# ADR-002 – Use AWS Lambda for Event Processing

## Status

**Accepted**

---

# Context

The application requires a compute service that automatically processes image uploads whenever a new object is added to Amazon S3.

The compute service should:

- Automatically respond to Amazon S3 events
- Scale based on incoming workload
- Require minimal infrastructure management
- Integrate with other AWS services
- Follow a pay-for-use pricing model

Since image uploads occur unpredictably, keeping dedicated servers running continuously would result in unnecessary operational overhead and cost.

---

# Decision

AWS Lambda was selected as the compute service for processing uploaded images.

The Lambda function is responsible for:

- Receiving Amazon S3 ObjectCreated events
- Validating uploaded files
- Generating a deterministic ImageId
- Preventing duplicate processing
- Writing metadata to Amazon DynamoDB
- Publishing structured logs to Amazon CloudWatch

The function executes only when an event occurs, making it a natural fit for an event-driven architecture.

---

# Alternatives Considered

## Amazon EC2

### Pros

- Full control over the operating system
- Suitable for long-running applications
- Supports custom software installation

### Cons

- Requires server management
- Manual scaling
- Higher operational overhead
- Continuous compute costs even when idle
- Additional monitoring and patching responsibilities

---

## Amazon ECS

### Pros

- Container-based deployment
- Good for microservices
- Supports horizontal scaling

### Cons

- Requires container image management
- Additional infrastructure complexity
- Not necessary for lightweight event processing

---

## AWS Step Functions

### Pros

- Excellent for workflow orchestration
- Built-in retry and error handling
- Visual workflow representation

### Cons

- Adds unnecessary complexity for a single processing step
- Better suited to multi-step business workflows

---

# Consequences

## Positive

- Fully managed compute service
- Automatic scaling
- Native integration with Amazon S3
- Pay only for execution time
- No server management
- Simplified deployment
- Native CloudWatch integration

## Negative

- Execution time limits
- Cold starts may occur
- Stateless execution model
- Limited local storage

These trade-offs were acceptable because the function performs lightweight processing and completes within a few seconds.

---

# References

- AWS Lambda Documentation
- AWS Lambda Best Practices
- AWS Well-Architected Framework