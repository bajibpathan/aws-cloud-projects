# Project Summary

## Ritual Roast — Three-Tier Web Application on AWS

Ritual Roast is a manually deployed three-tier recipe application built in `eu-west-2`. Users access a Flask application through an internet-facing Application Load Balancer, submit recipes, and retrieve data stored in Amazon RDS for MySQL.

### Engineering outcome

- Designed a `10.16.0.0/16` VPC with six subnets across two Availability Zones.
- Placed the ALB in public subnets and the EC2 and RDS tiers in private subnets.
- Used a launch template and Auto Scaling group to maintain two application instances.
- Protected tier-to-tier traffic with security-group references.
- Delivered application artifacts from a versioned, private S3 bucket.
- Stored database credentials in Secrets Manager with rotation configured.
- Used Systems Manager Session Manager instead of public SSH.
- Validated ALB access, healthy targets, recipe submission, and database retrieval.
- Diagnosed unhealthy targets caused by an incorrect secret name.

### Cost-aware deviation

The original capstone specified RDS Multi-AZ. The rebuild uses a free-tier-eligible Single-AZ database to control cost. The two-AZ DB subnet group preserves a clear upgrade path, but the deployed database does not provide cross-AZ failover.

### Current status

The application works end to end. EC2 replacement testing and resource cleanup remain to be completed and documented before the project is marked fully complete.

### Skills demonstrated

AWS networking, EC2, Auto Scaling, load balancing, RDS, S3, Secrets Manager, IAM, Systems Manager, Linux bootstrap troubleshooting, security boundaries, availability trade-offs, cost awareness, and technical documentation.

