# Project Requirements

## 1. Project Overview

This project implements a three-tier recipe contest application on AWS.

Members of the public access the application through an Application Load Balancer and submit recipes using a web form. The Flask application processes each submission and stores the recipe information in an Amazon RDS for MySQL database. Submitted recipes are then displayed in a public gallery.

The web and application tiers are distributed across two Availability Zones. A Single-AZ RDS database is used during the cost-controlled portfolio rebuild.

The original capstone architecture specified an RDS Multi-AZ deployment. Multi-AZ remains the recommended configuration for a production environment.

## 2. Business Scenario

The organization requires a minimum viable product that allows it to run an online recipe contest.

The application must allow users to:

- Access the application through a web browser
- Submit their name and email address
- Enter a recipe title
- Select a recipe category
- Provide recipe instructions or a description
- Submit the recipe
- Receive a confirmation message
- View submitted recipes in a public gallery

The user’s email address must be stored but must not be displayed publicly.

For this minimum viable product, submitted recipes are published automatically without a moderation workflow.

## 3. Functional Requirements

### Recipe submission

The application must collect:

- First and last name
- Email address
- Recipe title
- Recipe category
- Recipe description or instructions
- Submission date and time

### Recipe gallery

The application must:

- Display submitted recipes
- Display the recipe title
- Display the submitter’s name
- Display the recipe description
- Display the submission date and time
- Sort recipes with the newest submissions first
- Allow recipes to be filtered by category if supported by the supplied application

The submitter’s email address must not appear in the public gallery.

## 4. Technical Requirements

The solution must include:

- A custom Amazon VPC
- Network resources distributed across two Availability Zones
- Two public subnets for the Application Load Balancer
- Two private Web subnets for the EC2 application instances
- Two private Data subnets for Amazon RDS
- An Internet Gateway
- One NAT Gateway for the learning implementation
- An internet-facing Application Load Balancer
- A target group forwarding requests to the Flask application on port `5000`
- An EC2 Auto Scaling group
- A launch template for repeatable EC2 provisioning
- A Single-AZ Amazon RDS for MySQL database for the cost-controlled rebuild
- A DB subnet group containing Data subnets in two Availability Zones
- An Amazon S3 bucket for application source files
- S3 bucket versioning
- AWS Secrets Manager for database credentials
- An IAM role attached to the EC2 instances
- AWS Systems Manager Session Manager for administrative access
- Security groups that restrict traffic between application tiers

## 5. Availability Requirements

The web and application tiers must remain available when one application server becomes unhealthy.

The solution must:

- Deploy the Application Load Balancer across two public subnets
- Run application instances across two Availability Zones
- Maintain the required number of EC2 instances through Auto Scaling
- Replace unhealthy EC2 instances automatically
- Distribute requests across healthy application instances
- Register Auto Scaling instances with the Application Load Balancer target group
- Prevent the load balancer from forwarding traffic to unhealthy targets

### Database availability limitation

The cost-controlled rebuild uses a Single-AZ RDS database. Therefore, the current implementation does not provide automatic cross-Availability-Zone database failover.

The original capstone design specified RDS Multi-AZ. A production implementation should use Multi-AZ to maintain a synchronous standby database in another Availability Zone.

## 6. Security Requirements

- Only the Application Load Balancer may receive public application traffic.
- EC2 application servers must not be directly accessible from the internet.
- The Web security group must accept application traffic only from the ALB security group.
- The database security group must accept MySQL traffic only from the Web security group.
- The RDS database must not be publicly accessible.
- Database credentials must not be embedded directly in application source code.
- Database credentials must not be stored in EC2 user data.
- Database credentials must be stored in AWS Secrets Manager.
- EC2 instances must retrieve credentials from AWS Secrets Manager.
- Administrative access must use Systems Manager Session Manager instead of public SSH.
- Secret values and credentials must never appear in screenshots or GitHub documentation.
- The S3 application bucket must block public access.

### IAM implementation

The EC2 instances use the following IAM role:

`ritual-roast-master-ec2-iam-role`

The role contains:

- `AmazonSSMManagedInstanceCore`
- `AmazonS3FullAccess`
- `ritual-roast-rds-db-secret-policy`

`AmazonS3FullAccess` is used as part of the guided learning implementation. It grants broader access than the application requires.

A production implementation should replace it with a least-privilege policy that permits access only to the required application-artifact bucket and objects.

## 7. Validation Requirements

The completed solution must be validated by:

1. Opening the application using the ALB DNS name
2. Confirming that the application form loads successfully
3. Submitting a recipe through the form
4. Confirming that the recipe submission succeeds
5. Confirming that the submitted recipe appears in the gallery
6. Confirming that the application can write data to the RDS database
7. Confirming that the application can retrieve data from the RDS database
8. Verifying that all registered EC2 targets are healthy
9. Confirming that the EC2 instances appear as Systems Manager managed nodes
10. Stopping one EC2 application instance
11. Confirming that Auto Scaling detects and replaces the unhealthy instance
12. Confirming that the replacement instance registers with the target group
13. Confirming that the application remains accessible during EC2 recovery

### Validation excluded from the rebuild

RDS Multi-AZ failover testing is not included because the cost-controlled rebuild uses a Single-AZ database.

Database failover testing should be added when the database is upgraded to Multi-AZ.

## 8. Cost Constraints

This is a temporary learning environment and must be operated within a controlled practice window.

To control costs:

- Use a free-tier-eligible RDS configuration where available
- Use appropriately sized EC2 development resources
- Use one NAT Gateway for the learning implementation
- Avoid leaving RDS, NAT Gateway and load-balancing resources running unnecessarily
- Complete deployment and testing within a planned practice window
- Capture evidence before beginning cleanup
- Delete resources after testing
- Release the NAT Gateway Elastic IP after deleting the NAT Gateway
- Confirm that no chargeable resources remain after cleanup

The overall solution is not completely free even when a free-tier-eligible RDS instance is used. The NAT Gateway and Application Load Balancer can generate charges while provisioned.

A production implementation would normally use one NAT Gateway per Availability Zone to reduce the single-AZ dependency.

## 9. Project Scope

### Included

- AWS VPC networking
- Public and private subnet design
- Internet Gateway and NAT Gateway configuration
- Security-group configuration
- Application load balancing
- EC2 launch-template configuration
- EC2 Auto Scaling
- Flask application deployment
- Amazon S3 application-artifact storage
- RDS MySQL integration
- AWS Secrets Manager integration
- IAM permissions
- Systems Manager Session Manager
- Application-tier recovery testing
- Technical documentation
- Evidence collection
- Resource cleanup

### Not included in this version

- RDS Multi-AZ failover testing
- Custom domain registration
- HTTPS certificate configuration
- AWS Web Application Firewall
- CI/CD automation
- Infrastructure as Code
- Containerization
- Kubernetes
- Advanced observability
- Application code redesign
- Recipe moderation workflow

These capabilities may be added as future enhancements.

## 10. Success Criteria

The project is considered successful when:

- The application is accessible through the ALB DNS name.
- The ALB has healthy EC2 targets.
- A user can submit a recipe successfully.
- The recipe is stored in the RDS MySQL database.
- The submitted recipe appears in the application gallery.
- The EC2 instances are not directly exposed to the internet.
- The RDS database is not publicly accessible.
- The EC2 instances can be managed through Systems Manager.
- Auto Scaling replaces an unhealthy EC2 instance.
- The application remains available while an unhealthy EC2 instance is replaced.
- Deployment evidence is captured.
- All chargeable resources are removed after testing.

## 11. Attribution

This project was completed as part of the IaaS Academy training program. The application scenario and application source code were provided through the course.

The AWS deployment, configuration, validation, troubleshooting, architectural analysis and portfolio documentation represent my hands-on implementation and learning.

Course-provided application source code and proprietary course materials will not be redistributed unless permission or an applicable license explicitly allows it.