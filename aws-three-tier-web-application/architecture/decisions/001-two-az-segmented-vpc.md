# ADR-001: Use a two-AZ segmented VPC

## Status

Accepted

## Decision

Use a `10.16.0.0/16` VPC with separate Public, Web, and Data subnet pairs across `eu-west-2a` and `eu-west-2b`.

## Rationale

The design separates exposure and traffic responsibilities while allowing the ALB and application tier to span failure domains.

## Consequences

The design is easier to secure and reason about, but creates more network resources and requires deliberate route-table and security-group configuration.

