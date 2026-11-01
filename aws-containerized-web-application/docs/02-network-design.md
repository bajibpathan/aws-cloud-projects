# Network Design

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


Both services use the private Web subnets. The database subnet group spans the Data subnets; the RDS instance is Single-AZ. The ALB spans both public subnets. See [Architecture](../architecture/README.md) for placement and [Technical Overview](../TECHNICAL_OVERVIEW.md) for all configuration details.
