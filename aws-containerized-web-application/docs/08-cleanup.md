# Cleanup Guide

## Cleanup record and procedure

The author confirmed cleanup completion. The sequence below is the course procedure; individual deletion receipts and a final billing audit were not supplied.

1. Scale both ECS services to zero and wait for tasks to stop.
2. Delete services, deregister task-definition revisions, and delete the cluster.
3. Delete both ECR repositories and their images.
4. Delete the parent CloudFormation rotation stack, allowing its nested resources to be removed, and verify removal of the rotation Lambda.
5. Schedule deletion of the database secret with the seven-day recovery window. Scheduled deletion is distinct from immediate permanent removal.
6. Delete the lab RDS database without a final snapshot or retained automated backups, as chosen in the course exercise.
7. Terminate the temporary Docker build instance.
8. Delete the ALB, then both target groups.
9. Delete the NAT gateway, remove the resulting blackhole default route, and release its unused Elastic IP.
10. Retain reusable VPC infrastructure if needed for subsequent labs. The exact final retained-resource inventory was not separately supplied.

Before deleting data or images in a reused environment, preserve anything needed for another project. Review remaining manual snapshots, unattached volumes, log groups, and lab-only IAM policies/roles. The course cleanup does not establish that every such retained item has been removed.

