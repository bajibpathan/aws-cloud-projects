# ADR-007: DynamoDB History Data Model

## Status

Accepted

---

## Context

The application initially returned enhanced resume bullets directly to the client without storing any history.

To improve usability and demonstrate real-world application design, successful resume enhancements need to be persisted and made available for future retrieval.

The application also needs to support future features such as:

- User authentication
- Pagination
- Enhancement history
- Search
- Analytics

---

## Decision

Amazon DynamoDB was selected as the persistence layer.

Table:

```text
ResumeEnhancementHistory
```

Primary Key:

| Attribute | Purpose |
|-----------|---------|
| userId | Partition Key |
| createdAt | Sort Key |

Each enhancement also stores a globally unique:

```text
enhancementId
```

---

## Rationale

The table is designed around application access patterns rather than entities.

Primary access patterns:

1. Save enhancement
2. Retrieve enhancement history
3. Return newest enhancements first

Using:

```text
Partition Key:
userId

Sort Key:
createdAt
```

allows DynamoDB to efficiently retrieve enhancement history without performing table scans.

---

## Alternatives Considered

### Option 1

Partition Key:

```text
enhancementId
```

Rejected because:

- Cannot efficiently retrieve user history
- Requires table scan
- Difficult to extend

---

### Option 2

Relational Database

Rejected because:

- Higher operational overhead
- Less aligned with serverless architecture
- Unnecessary complexity for current requirements

---

## Consequences

### Positive

- Efficient history retrieval
- Supports future authentication
- Supports pagination
- Supports Global Secondary Indexes
- Fully serverless

### Trade-offs

- Data modelling must follow access patterns
- Eventual consistency should be considered where applicable

---

## Future Enhancements

Potential improvements include:

- Amazon Cognito integration
- Per-user enhancement history
- Pagination
- Global Secondary Indexes
- Time-to-Live (TTL) for old enhancements

---

## Related ADRs

- ADR-001 – Serverless Core Architecture
- ADR-004 – Amazon Bedrock Integration Strategy
- ADR-005 – Lambda Service Layer Architecture
- ADR-006 – API Gateway HTTP API Strategy