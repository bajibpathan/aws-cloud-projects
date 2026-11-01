# Screenshot Evidence

Evidence is grouped by implementation phase, matching the structure of the previous project. Keep your existing numbered filenames; only place them in the indicated folders. No screenshot files were supplied with this package, so this index does not assert that captures exist.

| Original # | Destination path | Evidence |
| --- | --- | --- |
| 01 | `02-networking/01-vpc-resource-map.png` | VPC resource map: six subnets, AZs, routes, internet gateway and NAT |
| 02 | `02-networking/02-nat-gateway.png` | rr-nat-gw Available, public subnet, public connectivity and Elastic IP |
| 03 | `02-networking/03-main-route-table.png` | ritual-roast-main-rt local route and active 0.0.0.0/0 NAT route |
| 04 | `03-security/04-web-app-sg-inbound.png` | Web-App-SG ports 3000 and 5000 from ALB SG |
| 05 | `03-security/05-database-sg-inbound.png` | Database-SG port 3306 from application SG and itself |
| 06 | `04-rds/06-rds-configuration.png` | recipedb Available, engine/version, class, initial DB, storage, Single-AZ |
| 07 | `04-rds/07-rds-connectivity.png` | VPC, DB subnet group/subnets, Database-SG, public access No, endpoint/3306 |
| 08 | `04-rds/08-rds-backup-retention.png` | Automated backup retention of one day |
| 09 | `05-secrets-manager/09-secret-overview.png` | Secret name, encryption key and database; values hidden |
| 10 | `05-secrets-manager/10-secret-rotation-configuration.png` | Enabled rotation, seven-day schedule, Lambda and successful rotation time |
| 11 | `05-secrets-manager/11-rotation-lambda-networking.png` | Rotation Lambda VPC, data subnets and Database-SG |
| 12 | `03-security/12-ec2-role-permissions.png` | Docker EC2 role with AmazonSSMManagedInstanceCore |
| 13 | `03-security/13-ecs-role-permissions.png` | Custom task role managed policy and inline secret policy |
| 14 | `03-security/14-secret-access-policy.png` | GetSecretValue limited to the application secret ARN |
| 15 | `06-docker-server/15-docker-server-configuration.png` | EC2 name, running/status checks, type, subnet, SG and role |
| 16 | `06-docker-server/16-docker-installation-validation.png` | whoami, docker --version and docker images without sudo |
| 17 | `07-ecr/17-ecr-private-repositories.png` | Both private repository names and London region |
| 18 | `07-ecr/18-docker-role-ecr-permissions.png` | Updated Docker EC2 role with SSM and ECR build permissions |
| 19 | `07-ecr/19-nextjs-ecr-image.png` | Frontend latest image, digest and push time |
| 20 | `07-ecr/20-flask-ecr-image.png` | Backend latest image, digest and push time |
| 21 | `08-load-balancing/21-flask-target-group.png` | IP / HTTP 5000 / VPC / health path /api/health |
| 22 | `08-load-balancing/22-nextjs-target-group.png` | IP / HTTP 3000 / VPC / health path / |
| 23 | `08-load-balancing/23-alb-configuration.png` | Active, internet-facing ALB, VPC, two public subnets and SG |
| 24 | `08-load-balancing/24-alb-listener-rules.png` | HTTP 80, priority 1 /api/* to Flask and default to Next.js |
| 25 | `09-ecs/25-flask-task-definition.png` | Family/revision, CPU/memory, both roles, image, container and port 5000 |
| 26 | `09-ecs/26-nextjs-task-definition.png` | Family/revision, CPU/memory, both roles, image, container and port 3000 |
| 27 | `09-ecs/27-ecs-cluster.png` | Cluster name, Active status, Fargate and monitoring configuration |
| 28 | `09-ecs/28-ecs-services-running.png` | Both services at two desired / two running tasks |
| 29 | `09-ecs/29-ecs-service-networking.png` | Each service: both web subnets, SG, public IP disabled and target group |
| 30 | `09-ecs/30-ecs-task-az-placement.png` | Four running tasks and actual AZ/subnet placement |
| 31 | `10-validation/31-target-groups-healthy.png` | Two healthy IP targets in each target group |
| 32 | `10-validation/32-alb-resource-map.png` | Listener rules, both target groups and healthy targets |
| 33 | `10-validation/33-application-homepage.png` | Next.js application through ALB address |
| 34 | `10-validation/34-recipe-submission-result.png` | Dummy test recipe in gallery; success message if available |
| 35 | `11-rolling-update/35-frontend-updated-image.png` | Updated frontend latest tag, new digest and push time |
| 36 | `11-rolling-update/36-frontend-rolling-deployment.png` | New tasks replacing old tasks during frontend release |
| 37 | `11-rolling-update/37-countdown-working.png` | Application showing the running countdown after deployment |


Use a/b suffixes where separate tabs are needed. Publish your clearest evidence; all 38 entries are not mandatory. Redact credentials/personal data and keep secret values hidden. Preserve any task-definition exports after reviewing them. Do not recreate deleted resources solely to capture missing evidence.
