# ADR-003: Use Single-AZ RDS for the lab

## Status

Accepted for the lab

## Decision

Deploy one private db.t3.micro MySQL instance.

## Rationale

Control the cost of a temporary training environment.

## Consequences

The database has no Multi-AZ standby; use Multi-AZ for an appropriate production availability target.
