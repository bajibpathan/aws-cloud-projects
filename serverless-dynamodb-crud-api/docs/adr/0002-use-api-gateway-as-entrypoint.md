# ADR 0002 — Use API Gateway as the API Entry Point

## Status
Accepted

## Context
The project needs a public HTTPS endpoint to receive requests and trigger backend logic.

## Decision
Use **Amazon API Gateway (REST API)** as the entry point.

## Rationale
- Fully managed API service  
- Native integration with Lambda  
- Supports request validation, throttling, and logging  
- Beginner‑friendly configuration  
- No servers or load balancers required  

## Alternatives Considered
### Application Load Balancer (ALB)
- Works with Lambda but adds unnecessary complexity  
- Not ideal for simple JSON‑based APIs  

### CloudFront + Lambda@Edge
- Designed for edge compute, not CRUD APIs  

## Consequences
- API Gateway pricing is per request  
- REST API is more expensive than HTTP API (acceptable for learning)  
