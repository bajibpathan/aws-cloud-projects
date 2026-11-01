# Project Requirements

## Business context

Ritual Roast needs a recipe contest application that a small development team can operate with less server administration. The previous EC2 deployment co-hosted frontend and backend components. The containerized version separates Next.js and Flask to support independent deployments and scaling configuration.

## Functional requirements

- Open the recipe application through a public endpoint.
- Submit recipes through the frontend and Flask API.
- Store recipes in MySQL and show them in a gallery.
- Retrieve database connection details from Secrets Manager.
- Release a frontend countdown correction without rebuilding the backend.

## Technical requirements

- Deploy in eu-west-2 using the existing 10.16.0.0/16 VPC.
- Run two Fargate tasks per service in private web subnets.
- Route default requests to Next.js and /api/* to Flask through an ALB.
- Use private ECR repositories and a private RDS database.
- Validate target health, recipe submission, retrieval, and the frontend release.
- Remove temporary resources after practice.

## Scope

Console deployment, Docker builds, IAM, networking, service deployment, validation, rolling update and cleanup were included. Terraform, CI/CD, automatic scaling policies, measured zero-downtime testing and production failover were outside the completed scope.
