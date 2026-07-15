# ADR-003 – Use Amazon DynamoDB for Metadata Storage

## Status

**Accepted**

---

# Context

The application needs to store metadata for every successfully processed image.

The metadata includes:

- ImageId
- Bucket Name
- Object Key
- File Extension
- Upload Timestamp
- Processing Status

The database should:

- Scale automatically
- Provide low-latency access
- Integrate with AWS Lambda
- Require minimal administration
- Support serverless workloads
- Handle unpredictable traffic

The application stores simple metadata records and does not require complex joins, transactions across multiple tables, or relational queries.

---

# Decision

Amazon DynamoDB was selected as the metadata store.

The table uses:

- On-Demand Capacity Mode
- Primary Key: ImageId
- Conditional Writes
- No secondary indexes
- No DynamoDB Streams
- No Global Tables

The Lambda function writes one metadata record for each successfully processed image.

Conditional writes ensure duplicate events do not create duplicate records.

---

# Alternatives Considered

## Amazon RDS

### Pros

- Supports SQL
- Relational data model
- ACID transactions
- Mature ecosystem

### Cons

- Requires database administration
- Capacity planning
- Scaling considerations
- Higher operational overhead
- Less suitable for unpredictable serverless workloads

---

## Amazon Aurora

### Pros

- High availability
- Automatic backups
- Better scalability than traditional RDS
- MySQL/PostgreSQL compatibility

### Cons

- Higher cost for this workload
- More operational complexity
- Unnecessary for storing simple metadata

---

## Amazon ElastiCache

### Pros

- Extremely low latency
- Ideal for caching

### Cons

- Data is not intended as the primary persistent store
- Additional infrastructure
- Does not meet long-term metadata storage requirements

---

# Consequences

## Positive

- Fully managed NoSQL database
- Automatic scaling
- Low-latency performance
- Native AWS Lambda integration
- No infrastructure management
- Pay-per-request pricing with On-Demand capacity
- Supports conditional writes for idempotent processing

## Negative

- No relational joins
- Different data modeling approach compared to SQL databases
- Query flexibility depends on key design
- Global Tables and Streams introduce additional cost if enabled

These trade-offs were acceptable because the application stores independent metadata records rather than relational business data.

---

# Why DynamoDB Was the Best Choice

The application's access pattern is simple:

```text
Image Uploaded

↓

Generate ImageId

↓

Store Metadata

↓

Retrieve Metadata (if required)
```

A relational database would introduce unnecessary operational overhead for this workflow.

DynamoDB aligns naturally with the application's event-driven, serverless architecture.

---

# References

- Amazon DynamoDB Documentation
- DynamoDB Best Practices
- AWS Well-Architected Framework