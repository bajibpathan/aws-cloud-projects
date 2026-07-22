# Architecture Decision Records

Architecture Decision Records (ADRs) capture the important technical decisions made during the design and implementation of the AWS AI Resume Builder.

Each ADR documents:

- The problem or architectural requirement
- The decision that was made
- The reason behind the decision
- Alternative approaches considered
- Benefits and trade-offs
- The impact on the overall architecture

ADRs will be created as each project phase is designed, implemented and validated.

---

## ADR Status Definitions

| Status | Meaning |
|---|---|
| Proposed | The decision is under review and has not yet been implemented |
| Accepted | The decision has been approved and will be implemented |
| Implemented | The decision has been implemented and validated |
| Superseded | The decision has been replaced by a newer ADR |
| Rejected | The decision was considered but not selected |

---

## ADR Index

| ADR | Decision | Status |
|---|---|:---:|
| [ADR-001](ADR-001-use-separate-s3-buckets.md) | Use separate S3 buckets for resumes and generated websites | Accepted |
| [ADR-002](ADR-002-use-different-versioning-strategies.md) | Use different versioning strategies for the S3 buckets | Accepted |
---

## Naming Convention

ADR files will follow this naming format:

```text
ADR-<number>-<short-decision-name>.md
```
