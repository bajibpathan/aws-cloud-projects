# ADR-002: Build Manually Before Introducing Terraform

## Status

Accepted

## Context

The project will eventually benefit from Infrastructure as Code, but the primary goal is to understand how each AWS service works and how the services connect.

Introducing Terraform too early could make it possible to create resources without fully understanding the underlying AWS configuration.

## Decision

Build and configure the application manually first.

Terraform will be introduced only after the working application has been implemented and understood.

## Why

This sequence allows each AWS resource to be learned independently before automating it.

The manual-first approach helps build understanding of:

- Resource configuration
- IAM permissions
- Service integrations
- Runtime behavior
- Troubleshooting
- Cost implications

Once the manual implementation works, the same resources can be recreated using Terraform with much better understanding.

## Alternatives Considered

### Terraform from the Beginning

Starting with Terraform would provide repeatable infrastructure immediately, but it could hide important AWS concepts behind configuration files before the underlying services are understood.

### AWS CloudFormation or AWS SAM

CloudFormation and SAM are valid AWS-native Infrastructure as Code options, but Terraform is planned later because it is widely used in cloud engineering roles and aligns with the broader learning goals of the project.

## Consequences

### Positive

- Better understanding of AWS services
- Easier troubleshooting during early development
- Clearer learning progression
- Terraform becomes easier to understand later

### Trade-offs

- Some resources will initially be created manually
- The infrastructure will not be fully reproducible until the Terraform phase
- Manual configuration introduces some temporary repetition
