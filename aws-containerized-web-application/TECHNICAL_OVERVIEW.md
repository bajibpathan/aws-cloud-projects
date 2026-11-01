# Technical Overview

These settings describe the completed lab before cleanup. Names explicitly supplied by the author are reproduced exactly. Course settings are identified where the exact deployed value was not separately recorded.

## Network

| Resource | Value |
| --- | --- |
| Region | `eu-west-2` — London |
| VPC CIDR | `10.16.0.0/16` |
| NAT gateway | `rr-nat-gw`, in `PublicSubnet-01-2a` |
| Private/main route table | `ritual-roast-main-rt` |
| Outbound route | `0.0.0.0/0` → NAT gateway |

| Subnet name as supplied | CIDR | AZ | Purpose |
| --- | --- | --- | --- |
| Public Subnet-01-2a / PublicSubnet-01-2a | `10.16.0.0/20` | eu-west-2a | ALB, NAT, temporary build instance |
| Public Subnet-02-2b | `10.16.16.0/20` | eu-west-2b | ALB |
| Websubnet-01-2a | `10.16.64.0/20` | eu-west-2a | Frontend/backend Fargate tasks |
| Websubnet-02-2b | `10.16.80.0/20` | eu-west-2b | Frontend/backend Fargate tasks |
| DataSubnet-01-2a | `10.16.192.0/20` | eu-west-2a | RDS subnet group and rotation Lambda |
| Datasunet-02-2b | `10.16.208.0/20` | eu-west-2b | RDS subnet group and rotation Lambda |

The final data-subnet spelling reflects the author's supplied label. CIDRs do not overlap. Public subnet routing uses the internet gateway; private outbound access uses the NAT route.

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

## Build server and ECR

| Resource | Value |
| --- | --- |
| EC2 name | `ritual-roast-docker-name` |
| Subnet / SG | `PublicSubnet-01-2a` / `rr-bastion-host-sg` |
| OS / size | Amazon Linux 2023 / t3.micro, course configuration |
| Access | Session Manager |
| Frontend repository | `ritual-roast-nextjs-app` |
| Backend repository | `ritual-roast-flask-app` |
| Repository visibility | Private |
| Tag mutability / encryption | Mutable / AES-256 |
| Course deployment tag | `latest` |

## ECS

Cluster: `ritual-roast-web-app-cluster`.

| Setting | Flask | Next.js |
| --- | --- | --- |
| Task definition family | `ritual-roast-flask-task-def` | `ritual-roast-nextjs-frontend-task-def` |
| Container | `ritual-roast-flask-container` | `ritual-roast-nextjs-container` |
| Service | `ritual-roast-flask-backend-service` | `ritual-roast-nextjs-frontend-service` |
| Task resources | 1 vCPU / 2 GiB | 1 vCPU / 2 GiB |
| Port | TCP 5000 | TCP 3000 |
| Launch / network | Fargate / awsvpc | Fargate / awsvpc |
| OS / CPU architecture | Linux / x86_64, course setting | Linux / x86_64, course setting |
| Desired tasks | 2 | 2 |
| Subnets | Both web subnets | Both web subnets |
| Public IP | Disabled | Disabled |
| SG | `Web-App-SG` | `Web-App-SG` |
| Logging | CloudWatch, course defaults | CloudWatch, course defaults |

Container Insights was skipped in the course for cost control. Actual task-definition revision numbers, log-group names, image digests, and platform version numbers were not supplied.

## ALB and target groups

| Setting | Configuration |
| --- | --- |
| ALB | Internet-facing, IPv4, both public subnets |
| Listener | HTTP 80 |
| Priority 1 | `/api/*` → Flask target group |
| Default | Forward to Next.js target group |
| Flask targets | IP / HTTP 5000 / health path `/api/health` |
| Next.js targets | IP / HTTP 3000 / health path `/` |
| Registration | ECS-managed task IP registration and deregistration |

Exact ALB, target-group, and Load Balancer SG names were not supplied. Functional labels are used throughout this repository so these omissions do not require placeholder edits.
