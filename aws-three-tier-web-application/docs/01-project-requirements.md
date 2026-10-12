# Project Requirements

## 1. Project Overview

This project implements a highly available three-tier recipe contest application on AWS.

Members of the public access the application through an Application Load Balancer and submit recipes using a web form. The application processes each submission and stores the recipe information in an Amazon RDS MySQL database. Submitted recipes are displayed in a public gallery.

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
- View approved recipes in a public gallery

The user’s email address must be stored but must not be displayed publicly.

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
- Allow recipes to be filtered by category, if supported by the supplied application

## 4. Technical Requirements

The solution must include:

- A custom Amazon VPC
- Resources distributed across two Availability Zones
- Public subnets for the Application Load Balancer
- Private application subnets for the EC2 instances
- Private database subnets for Amazon RDS
- An internet-facing Application Load Balancer
- An Auto Scaling group containing EC2 application servers
- A launch template for repeatable EC2 provisioning
- A target group forwarding requests to the application
- An Amazon RDS MySQL Multi-AZ database
- An Amazon S3 bucket for application source files
- AWS Secrets Manager for database credentials
- IAM roles following least-privilege principles
- AWS Systems Manager Session Manager for administrative access
- Security groups that restrict traffic between tiers

## 5. Availability Requirements

The application must remain available when one application server becomes unhealthy.

The solution must:

- Run application instances across two Availability Zones
- Maintain the required number of instances through Auto Scaling
- Replace unhealthy EC2 instances automatically
- Distribute requests across healthy application instances
- Use an RDS Multi-AZ deployment for database availability
- Support database failover to a standby Availability Zone

## 6. Security Requirements

- Only the Application Load Balancer may receive public web traffic.
- EC2 application servers must not be directly accessible from the internet.
- The application security group must accept application traffic only from the load balancer security group.
- The database security group must accept MySQL traffic only from the application security group.
- The RDS database must not be publicly accessible.
- Database credentials must not be embedded directly in the application or user-data script.
- EC2 instances must retrieve credentials from AWS Secrets Manager.
- Administrative access should use Session Manager instead of public SSH access.
- S3 permissions should be restricted to the application artifact bucket.
- Secret values and credentials must never appear in screenshots or GitHub documentation.

## 7. Validation Requirements

The completed solution must be validated by:

1. Opening the application using the ALB DNS name
2. Submitting a recipe through the application form
3. Confirming that the recipe appears in the gallery
4. Verifying that all registered targets are healthy
5. Stopping one EC2 instance
6. Confirming that Auto Scaling launches a replacement instance
7. Confirming that the application remains accessible
8. Initiating an RDS Multi-AZ failover
9. Confirming that the application reconnects to the database
10. Submitting or retrieving a recipe after the failover

## 8. Cost Constraints

This is a temporary learning environment.

To control costs:

- Use appropriately sized development resources
- Use one NAT Gateway for the learning implementation
- Avoid leaving RDS, NAT Gateway and load-balancing resources running unnecessarily
- Complete deployment and testing within a planned practice window
- Delete resources after collecting validation evidence
- Confirm that no chargeable resources remain after cleanup

A production implementation would normally consider one NAT Gateway per Availability Zone to eliminate the single-AZ dependency.

## 9. Project Scope

### Included

- AWS networking
- Application load balancing
- EC2 Auto Scaling
- Flask application deployment
- MySQL database integration
- Secrets management
- IAM permissions
- High-availability validation
- Technical documentation
- Resource cleanup

### Not included in this version

- Custom domain registration
- HTTPS certificate configuration
- Web Application Firewall
- CI/CD automation
- Infrastructure as Code
- Containerization
- Kubernetes
- Advanced observability
- Application code redesign

These capabilities may be added as future enhancements.

## 10. Attribution

This project was completed as part of the IaaS Academy training program. The application scenario and application source code were provided through the course.

The AWS deployment, configuration, validation, troubleshooting, architectural analysis and portfolio documentation represent my hands-on implementation and learning.

Course-provided application source code and proprietary course materials will not be redistributed unless permission or an applicable license explicitly allows it.