# Troubleshooting

## Troubleshooting reference

These checks are reference guidance, not a record of failures in this build.

| Symptom | Check |
| --- | --- |
| Cannot push image | EC2 instance-profile ECR permissions, correct region/registry, Docker login, local image tag |
| Task cannot pull image | Execution role, image URI/tag, private subnet route, ECR/S3 connectivity |
| Secret access denied | Application task role and secret-specific GetSecretValue permission; distinguish task role from execution role |
| Database connection failure | app.py region/secret name, secret DB name/host, RDS availability, SG 3306, credentials |
| Unhealthy target | Container listener, application logs, matching target port, ALB-to-task SG rules, correct health path |
| API request reaches frontend | Listener priority and `/api/*` condition; backend target-group assignment |
| Frontend change not visible | New ECR digest, successful forced deployment, running task image digest, browser refresh |
| Rotation failure | Rotation stack/function, data subnets, Database-SG self-reference, outbound service connectivity, Lambda logs |

