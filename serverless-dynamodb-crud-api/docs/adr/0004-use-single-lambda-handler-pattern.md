# ADR 0004 — Use a Single Lambda Handler for All Operations

## Status
Accepted

## Context
The API supports multiple operations (create, read, update, delete, list).  
We must decide whether to use:
- One Lambda per operation, or  
- A single Lambda that routes operations internally  

## Decision
Use **one Lambda function** that handles all operations based on the `operation` field in the request.

## Rationale
- Simpler for beginners  
- Easier to deploy and maintain  
- Reduces number of Lambda functions  
- Matches the tutorial and learning goals  

## Alternatives Considered
### One Lambda per operation
- More modular  
- Better for large production systems  
- But adds complexity for a beginner project  

## Consequences
- The handler file grows as more operations are added  
- Routing logic must be maintained manually  
