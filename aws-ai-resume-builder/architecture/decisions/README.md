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

| ADR | Title | Status |
|------|-------|--------|
| ADR-001 | Use Separate S3 Buckets | Accepted |
| ADR-002 | Use Different Versioning Strategies | Accepted |
| ADR-003 | Use Amazon S3 Presigned URLs for Secure Resume Uploads | Accepted |
| ADR-004 | Use Amazon Cognito and API Gateway JWT Authorization | Accepted |
---

## Naming Convention

ADR files will follow this naming format:

```text
ADR-<number>-<short-decision-name>.md
```
