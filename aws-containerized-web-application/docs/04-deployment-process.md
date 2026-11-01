# Deployment and Frontend Release

This is a concise record of the console-led workflow, not a replacement for the course walkthrough. The environment was subsequently cleaned up.

## 1. Prepare networking

Reuse the VPC and six subnets documented in [Configuration](../TECHNICAL_OVERVIEW.md). Create `rr-nat-gw` in the first public subnet, allocate its Elastic IP, and configure `ritual-roast-main-rt` with an IPv4 default route through it. Confirm private subnet associations and public routing through the internet gateway.

Allow ports 3000 and 5000 from the ALB SG into `Web-App-SG`. Allow MySQL 3306 from `Web-App-SG` and the database SG itself into `Database-SG`.

## 2. Deploy the database and secret

Create private RDS MySQL `recipedb` with initial database `recipedb` and class `db.t3.micro`. Use the existing DB subnet group and `Database-SG`. The course uses Single-AZ, 20 GiB storage, and one-day backup retention.

Create `ritualroast-recipe-secret` for the database using its initial credentials. Enable seven-day single-user rotation with `SecretsManager-ritual-roast-db-secret`. Confirm the rotation Lambda's data-subnet and SG assignments and verify initial rotation success.

## 3. Prepare IAM and Docker

Create the EC2 role for SSM access, then add permissions to authenticate to ECR and push images. Create the custom ECS task role with secret-specific `GetSecretValue` access. Keep the execution-role assignment separate, as recorded in Configuration.

Launch `ritual-roast-docker-name` and connect with Session Manager. The course's Docker setup is equivalent to:

```bash
sudo su - ec2-user
sudo yum update -y
sudo yum install -y docker
sudo systemctl start docker
sudo usermod -aG docker ec2-user
```

End the session, reconnect, and switch back to `ec2-user` before verifying:

```bash
whoami
docker --version
docker images
```

For reuse after a server reboot, enable the Docker service or start it again. The course demonstrated starting Docker; persistent enablement was not separately confirmed.

## 4. Build and publish the images

Download and extract the two course archives from the [source folder](https://github.com/iaasacademy/aws-solutions-architect-associate/tree/main/section11). If a download URL redirects, use `curl -L -o filename.zip 'URL'`; lowercase `-o` supplies the output filename.

Before building Flask, edit `app.py` to use region `eu-west-2` and secret `ritualroast-recipe-secret`. Do not insert the database password into code or the image.

Create both private ECR repositories with mutable tags and AES-256 encryption. In each source directory, build/tag its image and push it using that repository's **View push commands**. The commands below are reusable examples; set the actual registry first:

```bash
# Set this to your account's ECR registry, without a repository path.
export ECR_REGISTRY='YOUR_ACCOUNT_ID.dkr.ecr.eu-west-2.amazonaws.com'
aws ecr get-login-password --region eu-west-2   | docker login --username AWS --password-stdin "$ECR_REGISTRY"

# Run from the extracted Next.js directory.
docker build -t "$ECR_REGISTRY/ritual-roast-nextjs-app:latest" .
docker push "$ECR_REGISTRY/ritual-roast-nextjs-app:latest"

# Run these from the extracted Flask directory.
docker build -t "$ECR_REGISTRY/ritual-roast-flask-app:latest" .
docker push "$ECR_REGISTRY/ritual-roast-flask-app:latest"
```

`latest` is a tag, not automatic selection of the newest image. Inspect ECR to verify the image push and digest. Original application archives and Dockerfiles are not bundled here.

## 5. Configure ingress

Create IP target groups: frontend HTTP 3000 with `/` health checks; backend HTTP 5000 with `/api/health` health checks. Leave targets empty initially.

Create an internet-facing ALB in both public subnets. Its HTTP 80 listener defaults to the frontend target group. Add priority 1 path condition `/api/*` forwarding to the backend target group. ECS registers the targets when services launch.

## 6. Create task definitions and services

Create the two Fargate definitions listed in Configuration, using 1 vCPU / 2 GiB, awsvpc networking, the matching ECR images and ports, essential containers, and CloudWatch logs.

Assign `ritual-roast-ecs-task-execution-role` as **Task role** and `ecsTaskExecutionRole` as **Task execution role**.

Create `ritual-roast-web-app-cluster`, then both services with Fargate, replica scheduling, two desired tasks each, both private web subnets, `Web-App-SG`, and public IP disabled. Associate each container with its own target group on the existing ALB.

Wait for each service to reach 2/2 running and its target group to show two healthy IPs. Inspect actual AZ placement; selecting two subnets alone is not evidence of the observed distribution. Validate the application through the ALB DNS address.

## 7. Release the countdown update

1. On the Docker server, open the countdown component under `src/app/components/`.
2. Change its expired target date to a future date and save it.
3. Rebuild the frontend image and push the updated `latest` tag using the commands above.
4. Select `ritual-roast-nextjs-frontend-service` and **Force new deployment**.
5. Observe replacement tasks, target health, and deployment completion.
6. Refresh the application and verify the countdown runs.

The course rolling settings are minimum healthy **100%** and maximum **200%**. With two desired tasks, this allows up to four frontend tasks during replacement. Actual scheduling and ALB health checks determine the sequence.

The author confirmed successful completion. The exact component filename, chosen target date, deployment duration, and continuous availability measurements were not recorded. This is not a measured zero-downtime claim.

A forced deployment can refresh the image behind the same tag without changing the task-definition revision. Selecting “latest revision” when creating a service does not automatically adopt future task-definition revisions.
