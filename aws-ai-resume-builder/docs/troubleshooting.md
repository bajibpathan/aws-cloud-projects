# Troubleshooting Guide

## S3 Upload Failed

**Cause**

Invalid Presigned URL or expired URL.

**Resolution**

- Generate a new Presigned URL.
- Verify bucket permissions.
- Check CORS configuration.

---

## Lambda Permission Error

**Cause**

Missing IAM permissions.

**Resolution**

- Review the Lambda execution role.
- Verify S3, Textract, and Bedrock permissions.

---

## Textract Access Denied

**Cause**

Lambda role doesn't have Textract permissions.

**Resolution**

Grant the required Textract actions to the execution role.

---

## Bedrock Invocation Failed

**Cause**

Model access or inference profile isn't configured.

**Resolution**

- Verify model access.
- Check the inference profile.
- Confirm IAM permissions.

---

## Portfolio Not Updated

**Cause**

CloudFront cache.

**Resolution**

Create a CloudFront invalidation or wait for the cache to expire.