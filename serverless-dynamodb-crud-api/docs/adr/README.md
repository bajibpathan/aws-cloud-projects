## 📘 Architecture Decision Records (ADR) Index

This folder contains all Architecture Decision Records (ADRs) for the Serverless CRUD API project.

ADRs document the key technical decisions made during the design and implementation of the system.

Each ADR includes:

- Context — Why the decision was needed
- Decision — What was chosen
- Rationale — Why this option was selected
- Alternatives — Other options considered
- Consequences — Impact of the decision

---

## 📄 ADR List

| ADR Number | Title                               | Description                                                   |
|------------|---------------------------------------|---------------------------------------------------------------|
| [0001](0001-use-lambda-for-compute.md)       | Use AWS Lambda for Compute            | Decision to use Lambda as the serverless compute layer.       |
| [0002](0002-use-api-gateway-as-entrypoint.md)       | Use API Gateway as API Entry Point    | Decision to expose the API using Amazon API Gateway.          |
| [0003](0003-use-dynamodb-as-database.md)       | Use DynamoDB as the Database          | Decision to store CRUD items in DynamoDB.                     |
| [0004](0004-use-single-lambda-handler-pattern.md)       | Use Single Lambda Handler Pattern     | Decision to route all operations through one Lambda function. |
| [0005](0005-use-least-privilege-iam-policy.md)       | Use Least‑Privilege IAM Policy        | Decision to create a custom IAM policy with minimal permissions. |

---

## 🧭 How to Use This Folder

Start with ADR 0001 and read in order — each ADR builds on previous decisions.

Add new ADRs whenever you introduce new architectural changes.

Never delete old ADRs — they represent historical decisions.

If a decision changes, create a new ADR and mark the old one as Superseded.

---

## 📝 Template for New ADRs

This ADR template can be used for future decisions:

```markdown
# ADR XXXX — Title

## Status
Proposed / Accepted / Superseded

## Context
Explain the problem or requirement that led to this decision.

## Decision
State the decision clearly.

## Rationale
Explain why this decision was chosen.

## Alternatives Considered
- Option A
- Option B
- Option C

## Consequences
Explain the positive and negative impacts of this decision.
```