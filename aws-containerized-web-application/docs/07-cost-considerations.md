# Cost Considerations

## Cost considerations

Primary lab cost drivers were Fargate task runtime, ALB, RDS/storage, NAT gateway and traffic, public IPv4 addresses, EC2/EBS, ECR storage, Secrets Manager, and CloudWatch logs. No current price estimate, free-tier eligibility, measured spend, or zero-charge guarantee is asserted.

Stopping an application browser session does not stop AWS resources. Scaling ECS services to zero removes their tasks, but does not remove the database, ALB, NAT gateway, images, logs, or retained storage. Check the account's resource inventory and billing after cleanup.

