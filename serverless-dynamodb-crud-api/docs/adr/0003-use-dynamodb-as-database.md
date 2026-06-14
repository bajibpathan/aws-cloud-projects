# ADR 0003 — Use DynamoDB as the Database

## Status
Accepted

## Context
The project requires a simple, scalable, NoSQL database to store items using a primary key.

## Decision
Use **Amazon DynamoDB** as the data store.

## Rationale
- Fully serverless  
- No provisioning or scaling required  
- Millisecond performance  
- Perfect for key‑value CRUD operations  
- Integrates directly with Lambda  

## Alternatives Considered
### RDS (MySQL/PostgreSQL)
- Requires provisioning and maintenance  
- More complex for beginners  

### S3
- Not suitable for structured CRUD operations  

## Consequences
- Must design around DynamoDB’s NoSQL model  
- No relational joins (not needed for this project)  
