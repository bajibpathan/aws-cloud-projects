# 📦 Storage Layer Design

## Overview

The storage layer is the foundation of the Event-Driven Image Processing project.

Users upload images to an Amazon S3 bucket, which acts as the entry point for the entire workflow. Every image uploaded to the designated location will later trigger downstream processing through AWS Lambda.

At this stage of the project, the focus is on creating a secure, scalable, and reliable storage solution.

---

# 🎯 Objectives

The storage layer should:

- Store uploaded images securely.
- Support future event-driven processing.
- Protect data against accidental deletion.
- Encrypt data at rest.
- Organize uploaded files logically.
- Follow AWS security best practices.

---

# 🏗 Architecture

```text
User

↓

Amazon S3 Bucket

↓

uploads/
```

> Event Notifications will be added in the next phase.

---

# Why Amazon S3?

Amazon S3 was selected because it is designed for highly durable object storage and integrates natively with Amazon S3 Event Notifications.

The project stores image files rather than block devices or shared file systems. Amazon S3 provides the required scalability, durability, and native integration with AWS Lambda.

---

# Why not Amazon EBS?

Amazon EBS is block storage designed for Amazon EC2 instances.

Although EBS provides low-latency storage, it:

- Cannot directly store objects.
- Does not support native Event Notifications.
- Requires EC2 instances.
- Introduces unnecessary infrastructure management.

Since this project processes uploaded images, Amazon S3 is the more appropriate storage solution.

---

# Storage Configuration

| Configuration | Value |
|---------------|-------|
| Storage Type | Amazon S3 |
| Bucket Access | Private |
| Versioning | Enabled |
| Default Encryption | SSE-S3 |
| Object Ownership | Bucket Owner Enforced |
| Block Public Access | Enabled |

---

# Security Decisions

## Private Bucket

The bucket remains private to prevent unauthorized public access.

Future access will be granted using IAM Policies and Bucket Policies following the Principle of Least Privilege.

---

## Block Public Access

Block Public Access remains enabled to reduce the risk of accidentally exposing uploaded images.

---

## Versioning

Versioning was enabled to protect against accidental object deletion and overwrite.

Future project phases may also introduce Lifecycle Rules to manage previous object versions and optimize storage costs.

---

## Default Encryption

Server-Side Encryption (SSE-S3) encrypts all uploaded objects automatically without requiring key management.

This protects stored data and aligns with AWS security best practices.

---

## Bucket Owner Enforced

Object Ownership is configured as **Bucket Owner Enforced**.

This disables Access Control Lists (ACLs) and ensures the bucket owner owns every uploaded object.

Access permissions are managed using IAM Policies and Bucket Policies.

---

# Folder Structure

Currently the bucket contains:

```text
uploads/
```

The `uploads/` prefix represents incoming images.

Future project phases may introduce additional prefixes such as:

```text
uploads/

processed/

failed/

archive/
```

This organization helps separate incoming, processed, failed, and archived files while simplifying event filtering.

---

# Validation

The following validations were completed:

- S3 bucket created successfully.
- Versioning enabled.
- Default encryption enabled.
- Bucket Owner Enforced configured.
- Block Public Access enabled.
- Sample image uploaded to the `uploads/` prefix.

---

# Lessons Learned

- Amazon S3 is the most suitable storage service for object-based workloads.
- Storage should be designed before integrating compute services.
- Versioning protects against accidental object deletion.
- Encryption should be enabled from the beginning of a project.
- Organizing objects using prefixes simplifies future automation.

---

# Challenges

No major issues were encountered during the implementation of the storage layer.

---

# Future Enhancements

The next phase will introduce:

- AWS Lambda
- Amazon S3 Event Notifications
- IAM Role
- CloudWatch Logs

This will transform the storage layer into an event-driven architecture.

---

# References

- Amazon S3 Documentation
- Amazon S3 Best Practices
- AWS Well-Architected Framework - Security Pillar