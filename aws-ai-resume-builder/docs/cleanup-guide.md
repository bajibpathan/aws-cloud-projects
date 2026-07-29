# Cleanup Guide

To avoid unnecessary AWS charges, remove the resources created during this project.

## Resources to Delete

- Amazon S3 Buckets
- CloudFront Distribution
- Lambda Functions
- API Gateway
- Amazon Cognito User Pool
- IAM Roles (created for the project)
- CloudWatch Log Groups (optional)

## Verification

After cleanup, verify:

- No Lambda functions remain.
- S3 buckets are deleted.
- CloudFront distribution is removed.
- API Gateway is deleted.
- Cognito resources are removed.