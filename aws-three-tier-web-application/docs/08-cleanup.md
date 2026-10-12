# Cleanup Guide

## Warning

Capture required evidence before cleanup. Verify names and dependencies carefully. Database and secret deletion can be irreversible.

## Recommended order

1. Set the Auto Scaling group desired and minimum capacity to zero if needed for controlled shutdown.
2. Delete `ritual-roast-asg` and confirm its instances terminate.
3. Delete `ritual-roast-launch-template`.
4. Delete `ritual-roast-app-alb`.
5. Delete `ritual-roast-app-tg`.
6. Delete `ritual-roast-db` after deciding whether a final snapshot is required.
7. Delete `ritual-roast-rds-db-secret` and its rotation resources when no longer needed.
8. Empty and delete the versioned S3 bucket, including object versions and delete markers, if the bucket is not being retained.
9. Delete `ritual-roast-ngw` and wait for deletion to finish.
10. Release `ritual-roast-eip`.
11. Delete the DB subnet group.
12. Delete the three security groups after dependent resources are gone.
13. Detach and delete the Internet Gateway.
14. Delete the custom route table and subnets.
15. Delete `ritual-roast-vpc`.
16. Delete the EC2 IAM role and custom policy if they are not reused.

## Verification checklist

- [ ] No Auto Scaling group or EC2 instances remain.
- [ ] No ALB or target group remains.
- [ ] The RDS database is deleted.
- [ ] The NAT Gateway is deleted.
- [ ] The Elastic IP is released.
- [ ] The secret and rotation Lambda are deleted or intentionally retained.
- [ ] The S3 bucket is deleted or intentionally retained.
- [ ] The custom VPC is deleted.
- [ ] Billing and Cost Explorer show no unexpected active resources.

