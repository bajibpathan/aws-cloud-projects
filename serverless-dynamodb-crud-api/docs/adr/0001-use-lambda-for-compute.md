# ADR 0001 — Use AWS Lambda for Compute

## Status
Accepted

## Context
The project requires backend logic to process CRUD operations triggered via an HTTPS API.  
The compute layer must be:
- Serverless
- Low‑cost
- Easy to maintain
- Beginner‑friendly

## Decision
Use **AWS Lambda** as the compute service.

## Rationale
- No servers to manage  
- Automatically scales with traffic  
- Pay‑per‑use pricing  
- Native integration with API Gateway and DynamoDB  
- Ideal for small, event‑driven workloads  

## Alternatives Considered
### EC2
- Too heavy for this use case  
- Requires patching, scaling, and maintenance  

### ECS / Fargate
- More complex container orchestration  
- Overkill for simple CRUD logic  

### App Runner
- Good for web apps, but unnecessary for a single function  

## Consequences
- Cold starts may occur (acceptable for this project)  
- Logic must fit within Lambda execution limits  
