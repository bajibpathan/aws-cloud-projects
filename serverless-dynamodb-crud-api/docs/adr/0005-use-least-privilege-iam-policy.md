# ADR 0005 — Use Least‑Privilege IAM Policy for Lambda

## Status
Accepted

## Context
The Lambda function needs permissions to interact with DynamoDB and CloudWatch Logs.  
We must ensure the role follows security best practices.

## Decision
Create a **custom IAM policy** with only the required DynamoDB and CloudWatch permissions.

## Rationale
- Follows AWS security best practices  
- Prevents over‑permissioning  
- Easy to understand for beginners  
- Ensures Lambda can only access the intended table  

## Alternatives Considered
### AWS Managed Policy: AmazonDynamoDBFullAccess
- Too broad  
- Grants permissions not needed for this project  

### AdministratorAccess
- Never appropriate for Lambda functions  

## Consequences
- Must update the policy manually if new features require more permissions  
