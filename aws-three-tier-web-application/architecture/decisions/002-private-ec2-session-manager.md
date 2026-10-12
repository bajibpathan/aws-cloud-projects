# ADR-002: Use private EC2 instances and Session Manager

## Status

Accepted

## Decision

Run the Flask instances without public IPs and administer them through AWS Systems Manager Session Manager.

## Rationale

Only the ALB needs public exposure. Session Manager removes the need for inbound SSH, public instance addresses, and SSH-key distribution.

## Consequences

The instances require IAM permissions, the SSM Agent, and outbound connectivity to Systems Manager endpoints.

