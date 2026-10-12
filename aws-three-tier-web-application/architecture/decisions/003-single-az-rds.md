# ADR-003: Use Single-AZ RDS for the rebuild

## Status

Accepted for the cost-controlled lab

## Decision

Use a free-tier-eligible Single-AZ RDS MySQL instance while retaining a two-AZ DB subnet group.

## Rationale

The account configuration did not offer Multi-AZ under the selected free-tier path. Single-AZ allowed application and database integration practice without the additional database cost.

## Consequences

The deployed database does not provide automatic cross-AZ failover. Multi-AZ remains the production recommendation and RDS failover testing is outside the rebuild scope.

