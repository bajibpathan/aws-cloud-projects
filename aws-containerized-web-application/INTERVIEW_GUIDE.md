# Interview Guide

## Project introduction

“I deployed a containerized recipe application using Next.js and Flask as separate ECS Fargate services. An ALB routes UI and API requests to different target groups, and Flask uses Secrets Manager to connect to private RDS MySQL. I validated the recipe workflow, released a frontend update through rolling deployment, and cleaned up the environment.”

## Questions and talking points

| Question | Answer grounded in this project |
| --- | --- |
| Why Fargate? | The team wanted less EC2 host administration; Fargate runs the application tasks on managed compute. |
| Why two services? | UI and API deployments and desired counts can change independently. Scaling policies were not implemented. |
| Why IP targets? | awsvpc tasks have ENIs/private IPs; target groups register task IPs rather than EC2 instances. |
| How does routing work? | Priority 1 /api/* goes to Flask on 5000; default traffic goes to Next.js on 3000. |
| Task role versus execution role? | Task role grants Flask GetSecretValue; execution role supports ECR pulls and CloudWatch logging. |
| How did you update the frontend? | Change countdown date, rebuild/push latest, force new deployment, verify new tasks and the countdown. |
| Does latest update tasks automatically? | No. A deployment is needed; new task-definition revisions also require a service update. |
| What did you test? | Healthy services/targets, homepage, recipe submission/gallery/refresh, rotation success and frontend release. |
| Is this fully highly available? | No. Application design spans two AZs, but RDS is Single-AZ and outbound access uses one NAT gateway. |
| What would you improve? | HTTPS, separate SGs/roles, versioned images, IaC/CI-CD, alarms, scaling policies and failure tests. |
| Did you prove credential refresh? | No. Initial rotation succeeded, but runtime application refresh after rotation was not separately tested. |
| How did you control cost? | Short-lived resources, Single-AZ RDS, one NAT, and dependency-aware cleanup. |

## Keep claims precise

The application source came from the course. Describe the AWS deployment and validation as your hands-on work. Do not claim measured zero downtime, automatic scaling, AZ failover or a production rollout.
