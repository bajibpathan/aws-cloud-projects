# 📚 Architecture Decision Records (ADR) Index

This folder contains the Architecture Decision Records for the aws-lambda-execution-profiler project.

Each ADR documents a key technical decision made during the design and implementation of the Lambda profiling workflow.

---

## 📄 ADR Index

# Architecture Decision Records (ADR) Index

| ADR Number | Title | Status | File |
|-----------|--------|---------|-------|
| **[ADR‑001](./adr-001-choose-step-functions.md)** | Choosing AWS Step Functions for Profiling Workflow | Accepted | `adr-001-choose-step-functions.md` |
| **[ADR‑002](./adr-002-memory-configurations.md)** | Memory Configurations to Test | Accepted | `adr-002-memory-configurations.md` |
| **[ADR‑003](./adr-003-store-results-json.md)** | Storing Profiling Results in JSON Format | Accepted | `adr-003-store-results-json.md` |

---

## 📝 How ADRs Are Used in This Project

- ADRs help track why certain architectural choices were made.
- They provide clarity for future contributors and maintainers.
- They ensure decisions are documented, reviewable, and traceable.
- They keep the project aligned with AWS best practices and your portfolio standards.

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