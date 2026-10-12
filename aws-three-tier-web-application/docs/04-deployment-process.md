# Manual Deployment Process

## Ordered deployment

The order below respects resource dependencies and minimizes rework.

1. Create `ritual-roast-vpc` with DNS support.
2. Create the six Public, Web, and Data subnets.
3. Create and attach `ritual-roast-igw`.
4. Create `ritual-roast-public-rt`, add the Internet Gateway route, and associate the Public subnets.
5. Create `ritual-roast-ngw` with `ritual-roast-eip` in `PublicSubnet-01-2a`.
6. Add the NAT route to `ritual-roast-main-rt`.
7. Create the ALB, Web, and DB security groups.
8. Create `ritual-roast-master-ec2-iam-role`.
9. Create the versioned, private S3 artifact bucket and upload the supplied `flask/` directory.
10. Create `ritual-roast-rds-subnet-group`.
11. Create the private Single-AZ RDS MySQL instance.
12. Create `ritual-roast-rds-db-secret` and enable rotation.
13. Update the application with the exact Region and secret name, then upload a new S3 object version.
14. Create `ritual-roast-app-tg` on port `5000` with health path `/`.
15. Create `ritual-roast-app-alb` in the two Public subnets.
16. Create `ritual-roast-launch-template` with Amazon Linux 2023, the Web security group, EC2 role, and tested user data.
17. Create `ritual-roast-asg` across both Web subnets with min/desired/max set to `2`.
18. Wait for both registered targets to become healthy.
19. Open the ALB DNS name and validate recipe submission and retrieval.
20. Perform EC2 replacement testing, capture evidence, and clean up.

## Artifact configuration

The application configuration references:

- Region: `eu-west-2`
- Secret: `ritual-roast-rds-db-secret`
- S3 bucket: `rr-capstone-source-code-025`

Only identifiers belong in configuration. Passwords and secret values do not.

## Source-code boundary

The course-provided application and user-data source are not included in this public repository. This document records the deployment behavior and learner-owned implementation decisions.

