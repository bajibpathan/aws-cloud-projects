# Lessons Learned

1. Deployment order matters because networking, identity, secrets, load balancing, and compute have explicit dependencies.
2. Security-group references are safer and more maintainable than fixed private IP rules.
3. Private instances remain manageable through Session Manager when IAM and outbound connectivity are correct.
4. Auto Scaling creates repeatable infrastructure only when user data and external artifacts are correct.
5. An ALB health failure can originate in application dependencies such as Secrets Manager or RDS, not only networking.
6. S3 versioning makes artifact corrections recoverable, but artifact changes require instance replacement or redeployment.
7. High availability must be evaluated end to end. Two EC2 instances do not make a Single-AZ database highly available.
8. Cost optimization changes architecture. Single-AZ RDS and one NAT Gateway are valid lab trade-offs only when documented honestly.
9. Broad managed policies simplify labs but should be replaced with resource-scoped permissions.
10. Evidence collection and cleanup are part of the engineering work, not afterthoughts.

