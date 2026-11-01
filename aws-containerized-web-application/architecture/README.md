# Architecture Design

## Overview

Separate Next.js and Flask ECS services run on Fargate with two tasks each. The ALB routes by path to IP target groups. RDS and application tasks remain private; Secrets Manager supplies credentials and a VPC-connected Lambda performs rotation.

![Containerized application architecture](images/ritual-roast-container-architecture.png)

## Request flow

```mermaid
flowchart TD
    User["User browser"] -->|"HTTP :80"| ALB
    subgraph VPC["VPC 10.16.0.0/16 · eu-west-2"]
        subgraph Public["Public subnets · AZ 2a and 2b"]
            ALB["Internet-facing ALB"]
            NAT["One NAT gateway · AZ 2a"]
            Builder["Temporary EC2 Docker build server"]
        end
        subgraph Web["Private web subnets · AZ 2a and 2b"]
            FE["Next.js ECS service · 2 Fargate tasks · :3000"]
            BE["Flask ECS service · 2 Fargate tasks · :5000"]
        end
        subgraph Data["Private data subnets"]
            DB["RDS MySQL · Single-AZ · :3306"]
            Rotation["Secret rotation Lambda"]
        end
        ALB -->|"Default / Next.js target group"| FE
        ALB -->|"/api/* / Flask target group"| BE
        BE --> DB
        Rotation --> DB
        FE -.->|"Outbound access"| NAT
        BE -.->|"Outbound access"| NAT
    end
    Builder -->|"Build and push"| ECR["Two private ECR repositories"]
    ECR -.->|"Image source"| FE
    ECR -.->|"Image source"| BE
    BE -->|"GetSecretValue"| Secrets["Secrets Manager"]
    Rotation -->|"Rotate credentials"| Secrets
    FE -.-> Logs["CloudWatch Logs"]
    BE -.-> Logs
```

## Availability boundaries

The ALB uses two public subnets. Services are configured with two private web subnets. The lab uses Single-AZ MySQL and a single NAT gateway. The subnet group spans two AZs but does not make the database Multi-AZ. A cluster is a logical service/task grouping rather than an independent network security boundary.

## Architecture decisions

- [ADR-001: Separate Fargate services](decisions/001-separate-fargate-services.md)
- [ADR-002: ALB path routing](decisions/002-alb-path-routing.md)
- [ADR-003: Single-AZ RDS](decisions/003-single-az-rds.md)
- [ADR-004: Single NAT gateway](decisions/004-single-nat-gateway.md)

See [Network Design](../docs/02-network-design.md), [Security Design](../docs/03-security-design.md), and [Technical Overview](../TECHNICAL_OVERVIEW.md).
