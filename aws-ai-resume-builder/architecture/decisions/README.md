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
| ADR-001 | Use Amazon S3 presigned URLs for secure resume uploads | Proposed |
| ADR-002 | Use separate S3 buckets for uploaded resumes and generated websites | Proposed |
| ADR-003 | Use asynchronous Amazon Textract processing | Proposed |
| ADR-004 | Use Amazon Bedrock to generate structured JSON instead of HTML | Proposed |
| ADR-005 | Use Amazon CloudFront for generated website delivery | Proposed |

---

## Naming Convention

ADR files will follow this naming format:

```text
ADR-<number>-<short-decision-name>.md
```
