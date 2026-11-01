# Project Summary

## Ritual Roast — Containerized Web Application on AWS

Modernized a recipe contest application from EC2-hosted components to separate Next.js and Flask services on ECS Fargate in eu-west-2. An internet-facing ALB uses path-based routing to connect users to private tasks, while RDS MySQL stores recipes and Secrets Manager supplies credentials.

## Engineering outcome

- Reused a six-subnet VPC across two AZs.
- Built and published two Docker images to private ECR repositories.
- Configured separate task and execution roles and secret-specific access.
- Ran two tasks per service, each sized at 1 vCPU and 2 GiB.
- Validated four healthy targets and end-to-end recipe submission/retrieval.
- Confirmed initial secret rotation success.
- Released a countdown update through a forced frontend rolling deployment.
- Completed lab cleanup.

## Cost-aware tradeoffs

Single-AZ RDS and one NAT gateway reduced the temporary lab footprint. These remain availability constraints. HTTP, shared application permissions and mutable image tags are documented lab choices.

## Status

Implementation, functional validation, frontend update and cleanup completed. Screenshot captures can be added using the grouped evidence index. No load-test or failover result is claimed.

## Attribution

Application scenario and original source: IaaS Academy. AWS implementation, configuration, validation and operational learning: Baji Pathan.
