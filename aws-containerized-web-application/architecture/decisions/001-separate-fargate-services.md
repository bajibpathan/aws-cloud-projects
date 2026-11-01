# ADR-001: Separate frontend and backend Fargate services

## Status

Accepted for the lab

## Decision

Run Next.js and Flask as separate services, with two tasks each.

## Rationale

Reduce host administration and allow independent application releases.

## Consequences

The team still manages images, task sizing and permissions; dynamic scaling requires explicit policies.
