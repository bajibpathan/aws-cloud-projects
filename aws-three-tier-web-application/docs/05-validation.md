# Validation Guide

## Completed functional validation

- [x] ALB state is `Active`.
- [x] Two EC2 instances are running.
- [x] Both targets are healthy on port `5000`.
- [x] The application opens through the ALB DNS name.
- [x] A test recipe can be submitted.
- [x] The recipe is retrieved from MySQL and displayed.
- [x] The email address is not shown in the public gallery.
- [x] Instances are manageable through Systems Manager.

## Pending recovery validation

1. Keep the application open through the ALB.
2. Stop one Auto Scaling instance.
3. Observe the target become unhealthy and deregister.
4. Observe the Auto Scaling activity history launch a replacement.
5. Refresh the application during replacement.
6. Confirm the application remains available through the other target.
7. Wait for the replacement to complete initialization.
8. Confirm the new target becomes healthy.
9. Confirm desired capacity returns to two.

## Evidence

Recommended evidence includes the application page, successful recipe result, healthy targets, ASG activity history, replacement instance, Systems Manager managed-node view, and final target health. Do not expose credentials, secret values, account IDs, or personal information.

## Database scope

RDS failover testing is not applicable to the Single-AZ rebuild. It should be added only after converting the database to Multi-AZ.

