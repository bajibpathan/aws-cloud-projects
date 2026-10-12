# ADR-004: Use one NAT Gateway for the lab

## Status

Accepted for the cost-controlled lab

## Decision

Deploy one public NAT Gateway in `eu-west-2a` and route both Web subnets through it.

## Rationale

One NAT Gateway reduces the cost of a temporary practice environment.

## Consequences

The outbound path depends on one Availability Zone and cross-AZ data paths may occur. Production should use one NAT Gateway per AZ or suitable VPC endpoints.

