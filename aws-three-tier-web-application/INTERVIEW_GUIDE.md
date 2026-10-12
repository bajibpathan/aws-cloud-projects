# Interview Guide

## Thirty-second summary

I deployed a three-tier recipe application on AWS using an internet-facing ALB, two private EC2 Flask servers managed by Auto Scaling, and a private RDS MySQL database. I separated the tiers with subnets and security-group references, used S3 for versioned artifacts, Secrets Manager for database credentials, and Session Manager for server access. I also diagnosed an unhealthy-target issue caused by an incorrect secret name.

## Common questions

### Why place EC2 in private subnets?

The ALB is the only public entry point. Private placement reduces exposure and ensures application traffic arrives through the controlled load-balancing tier.

### How does the ALB reach the instances?

The Web security group permits TCP `5000` only from the ALB security group. The target group registers the instances and health-checks `/`.

### Why use an Auto Scaling group with min, desired, and max all set to two?

The lab demonstrates instance replacement and multi-AZ placement rather than load-driven scaling. A production policy could raise the maximum and add target tracking.

### What caused the unhealthy targets?

The Python application referenced the wrong Secrets Manager secret name. The application could not initialize its database connection. Correcting the name, uploading the new S3 object version, and replacing the instances restored health.

### Is the complete system highly available?

No. The ALB and application tier span two AZs, but the rebuild uses Single-AZ RDS and one NAT Gateway. The project documents these honest limitations and the production improvements.

### Why does the database subnet group contain two subnets for a Single-AZ database?

RDS DB subnet groups require coverage across Availability Zones and provide placement flexibility. They also support a later Multi-AZ upgrade.

### Why use Session Manager instead of SSH?

Session Manager avoids public IPs, inbound port `22`, and SSH-key distribution while keeping access controlled through IAM.

### What would you change for production?

I would add HTTPS and WAF, RDS Multi-AZ, one NAT Gateway per AZ or VPC endpoints, separate private route tables, least-privilege IAM, Gunicorn with `systemd`, a dedicated health endpoint, and centralized observability.

## Scenario questions

### One instance fails. What happens?

The ALB stops routing to the unhealthy target. The Auto Scaling group launches a replacement to return desired capacity to two, and the new instance bootstraps from S3 before registering as healthy.

### Both targets time out. Where do you start?

I inspect the target-health reason, verify security-group references and port `5000`, connect through Session Manager, check `/var/log/user-data.log` and `/var/log/flask-app.log`, verify the listening socket, and run a local `curl` request.

### Why is `AmazonS3FullAccess` a concern?

It allows access beyond the application artifact bucket. The role should instead receive `s3:ListBucket` and `s3:GetObject` only for the required bucket and prefix.

### How would you test database failover?

After converting RDS to Multi-AZ, I would initiate a reboot with failover, observe the RDS event stream and AZ role change, and validate that the application reconnects through the unchanged RDS endpoint.

