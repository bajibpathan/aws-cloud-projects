# ADR 001 — Choosing AWS Step Functions for Profiling Workflow

## Status
Accepted

## Context
The project requires running a Lambda function multiple times with different memory configurations (128 MB, 256 MB, 512 MB, 1024 MB, etc.). This process must be automated, repeatable, and capable of collecting execution metrics such as duration and cost. A manual or script-based approach would be error-prone and difficult to maintain.

## Decision
Use AWS Step Functions with the Lambda Power Tuning state machine to orchestrate the profiling workflow.

## Rationale
- Provides built-in orchestration and parallel execution
- Handles retries, errors, and branching logic
- Integrates natively with Lambda and CloudWatch
- The open-source Power Tuning workflow already exists and is well-maintained
- Reduces custom code and complexity

## Alternatives Considered
- Custom Python/Node.js script to invoke Lambda in a loop
- AWS Lambda function invoking itself recursively
- AWS CodeBuild or Step Functions Express Workflows

## Consequences
- Simplifies profiling logic and reduces code maintenance
- Requires IAM permissions for Step Functions
- Adds a small cost for state machine execution
- Provides a scalable, repeatable, production-grade profiling workflow
