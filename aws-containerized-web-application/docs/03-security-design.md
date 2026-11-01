# Security Design

## Security groups

| Destination SG | Inbound port | Source | Purpose |
| --- | --- | --- | --- |
| Load Balancer SG | TCP 80 | Internet, per course design | Public HTTP entry point |
| `Web-App-SG` | TCP 3000 | Load Balancer SG | Next.js traffic |
| `Web-App-SG` | TCP 5000 | Load Balancer SG | Flask traffic |
| `Database-SG` | TCP 3306 | `Web-App-SG` | Database connection |
| `Database-SG` | TCP 3306 | `Database-SG` itself | Rotation Lambda database connection |

Build-instance SG: `rr-bastion-host-sg`. Session Manager was used rather than SSH/key-pair login; the exact SG rules for that instance were not supplied. Outbound rules must support the required database and AWS service connectivity.

## RDS and Secrets Manager

| Setting | Value / evidence scope |
| --- | --- |
| DB identifier | `recipedb` — confirmed |
| Initial database name | `recipedb` — confirmed |
| Instance class | `db.t3.micro` — confirmed |
| Engine / deployment | MySQL / Single-AZ, course configuration |
| Public access | No, course configuration |
| Storage | 20 GiB; autoscaling disabled, course configuration |
| Backup retention | One day, course configuration |
| Master username | `admin`, course configuration |
| Database SG | `Database-SG` |
| Secret name | `ritualroast-recipe-secret` |
| Rotation Lambda | `SecretsManager-ritual-roast-db-secret` |
| Rotation | Enabled, seven-day single-user course schedule; initial success confirmed |
| Secret encryption | Default key selected in course; exact key ARN not recorded |

The database endpoint, MySQL engine version, subnet-group name, and exact storage type were not recorded. They are deliberately omitted rather than inferred. Secret values are excluded.

## IAM roles

| Role | Assignment / permission |
| --- | --- |
| `ritual-roast-docker-ec2-role` | EC2 instance profile; `AmazonSSMManagedInstanceCore` for Session Manager |
| Same EC2 role | Additional ECR build/push permissions covered by the course; exact attached managed-policy name not confirmed |
| `ritual-roast-ecs-task-execution-role` | **Task role** on both task definitions; managed ECS execution policy plus inline secret access policy |
| `ecsTaskExecutionRole` | **Task execution role** for ECR image pulls and CloudWatch log delivery |
| `ritual-roast-secrets-manager-policy` | Inline policy on the custom task role: `secretsmanager:GetSecretValue` scoped to this application's secret ARN |

The custom role's name includes “execution,” but its actual task-definition assignment is **Task role**. Flask uses this role for AWS SDK calls. The lab also assigns this role to Next.js; a tighter design would omit backend secret permissions from the frontend.


## Lab boundaries

The shared application SG and task role simplify the guided exercise. Production isolation should restrict database and secret access to the backend. Public application access uses HTTP in the lab; HTTPS with ACM is a future improvement. No passwords or secret values belong in repository files or screenshots.
