# AWS AI Resume Builder – Interview Guide

## Purpose

This document captures the architectural decisions, design rationale, AWS best practices, and interview questions related to the AWS AI Resume Builder project.

The goal is not only to build the solution but also to understand **why** each design decision was made.

---

# Phase 1 – Project Foundation

## Q1. What problem does this project solve?

The AWS AI Resume Builder automates the process of converting a traditional resume into a professional portfolio website.

Instead of manually creating a website, users upload a resume, and the application extracts the information, structures it using AI, and generates a static website.

---

## Q2. Why did you choose a serverless architecture?

Serverless architecture provides several advantages:

* No server management
* Automatic scaling
* Pay only for actual usage
* Faster development
* High availability through managed AWS services

Since resume uploads occur only when users submit documents, serverless is a cost-effective solution.

---

## Q3. Why is the architecture event-driven?

The application reacts to events instead of continuously checking for work.

Example:

```text
Resume uploaded

↓

Amazon S3 Event

↓

Lambda starts automatically
```

Benefits include:

* Loose coupling
* Better scalability
* Lower operational cost
* Improved reliability

---

## Q4. Why are architecture decisions documented separately?

Architecture Decision Records (ADRs) provide a historical record of important technical decisions.

Each ADR explains:

* The problem
* The decision
* Alternatives considered
* Benefits
* Trade-offs

This makes the project easier to understand and maintain.

---

## Q5. Why is documentation important?

Good documentation helps:

* New developers understand the project
* Reviewers evaluate design decisions
* Recruiters assess communication skills
* Teams maintain systems over time

Documentation is considered part of the software deliverable.

---

## Phase 1 Key Takeaways

* Design before implementation.
* Understand the business problem before selecting AWS services.
* Document architectural decisions as the project evolves.
* Build incrementally and validate each phase before moving forward.
* Focus on explaining **why**, not just **what**.
