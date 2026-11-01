# ADR-004: Use one NAT gateway for the lab

## Status

Accepted for the lab

## Decision

Create rr-nat-gw in public subnet AZ 2a and route private outbound traffic through it.

## Rationale

Reduce temporary lab cost.

## Consequences

Outbound connectivity depends on one AZ and may involve cross-AZ traffic; consider per-AZ NAT or suitable endpoints.
