# ADR-002: Use ALB path routing

## Status

Accepted for the lab

## Decision

Route /api/* to Flask and default traffic to Next.js using separate IP target groups.

## Rationale

Use one public entry point while preserving separate service deployment.

## Consequences

Health paths and ports must match each application. HTTPS remains a production improvement.
