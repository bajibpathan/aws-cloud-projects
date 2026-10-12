# Technical Overview

## Platform

| Item | Implementation |
|---|---|
| Region | `eu-west-2` |
| VPC | `ritual-roast-vpc` — `10.16.0.0/16` |
| Availability Zones | `eu-west-2a`, `eu-west-2b` |
| Public entry point | Internet-facing Application Load Balancer |
| Application runtime | Flask on Amazon Linux 2023 EC2 instances |
| Application port | `5000` |
| Database | Single-AZ Amazon RDS for MySQL |
| Database port | `3306` |
| Artifact source | Versioned private S3 bucket |
| Administration | AWS Systems Manager Session Manager |

## Component interactions

1. The ALB listener accepts HTTP on port `80`.
2. The listener forwards traffic to `ritual-roast-app-tg` on port `5000`.
3. The target group checks `/` and forwards only to healthy instances.
4. The Auto Scaling group maintains two instances across the Web subnets.
5. User data downloads the `flask/` application directory from S3 and starts the application.
6. The application calls Secrets Manager for current database credentials.
7. The application connects to RDS MySQL through the database security group.

## Routing

- `ritual-roast-public-rt` routes `0.0.0.0/0` to `ritual-roast-igw`.
- Both public subnets are explicitly associated with the public route table.
- The Web and Data subnets use `ritual-roast-main-rt` implicitly.
- The main route table sends `0.0.0.0/0` to `ritual-roast-ngw`.

## EC2 identity

`ritual-roast-master-ec2-iam-role` includes:

- `AmazonSSMManagedInstanceCore`
- `AmazonS3FullAccess`
- `ritual-roast-rds-db-secret-policy`

The S3 permission is broader than required and is documented as a future least-privilege improvement.

## Availability boundaries

The ALB and application instances span two Availability Zones. Auto Scaling can replace an unhealthy instance. The Single-AZ database and single NAT Gateway remain failure-domain dependencies in the lab implementation.

## Operational logs

The bootstrap process writes to `/var/log/user-data.log`. The Flask process writes to `/var/log/flask-app.log`. These logs were used to diagnose the initial target-health failure.

## Production hardening

- HTTPS with ACM and an HTTP-to-HTTPS redirect
- AWS WAF at the ALB
- Gunicorn and `systemd` for application process management
- Dedicated `/health` endpoint
- RDS Multi-AZ and managed credential rotation validation
- One NAT Gateway per AZ or service-specific VPC endpoints
- Separate application and database route tables
- Bucket-scoped S3 permissions
- CloudWatch logs, alarms, dashboards, and VPC Flow Logs

