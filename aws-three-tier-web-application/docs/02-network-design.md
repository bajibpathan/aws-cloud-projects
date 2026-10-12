# Network Design

## Regional configuration

| Setting | Value |
|---|---|
| Region | Europe (London), `eu-west-2` |
| Availability Zones | `eu-west-2a`, `eu-west-2b` |
| VPC | `ritual-roast-vpc` |
| VPC CIDR | `10.16.0.0/16` |
| DNS resolution and hostnames | Enabled |

## Subnet plan

| Name | AZ | CIDR | Tier |
|---|---|---|---|
| `PublicSubnet-01-2a` | `eu-west-2a` | `10.16.0.0/20` | Public |
| `PublicSubnet-02-2b` | `eu-west-2b` | `10.16.16.0/20` | Public |
| `WebSubnet-01-2a` | `eu-west-2a` | `10.16.64.0/20` | Private application |
| `WebSubnet-02-2b` | `eu-west-2b` | `10.16.80.0/20` | Private application |
| `DataSubnet-01-2a` | `eu-west-2a` | `10.16.192.0/20` | Private database |
| `DataSubnet-02-2b` | `eu-west-2b` | `10.16.208.0/20` | Private database |

Each `/20` provides 4,091 usable addresses after AWS reservations. Unused address space remains available for future subnet tiers.

## Routing

### Public route table

`ritual-roast-public-rt` is explicitly associated with both Public subnets.

| Destination | Target |
|---|---|
| `10.16.0.0/16` | Local |
| `0.0.0.0/0` | `ritual-roast-igw` |

### Main route table

The Web and Data subnets use `ritual-roast-main-rt` implicitly.

| Destination | Target |
|---|---|
| `10.16.0.0/16` | Local |
| `0.0.0.0/0` | `ritual-roast-ngw` |

This shared private route table matches the guided lab. Production should separate the Data tier and omit its default internet route.

## Key resources

| Resource | Name |
|---|---|
| Internet Gateway | `ritual-roast-igw` |
| Public route table | `ritual-roast-public-rt` |
| Main route table | `ritual-roast-main-rt` |
| NAT Gateway | `ritual-roast-ngw` |
| Elastic IP | `ritual-roast-eip` |
| DB subnet group | `ritual-roast-rds-subnet-group` |

## Validation

- [x] Six non-overlapping subnets exist across two AZs.
- [x] The Internet Gateway is attached.
- [x] Public subnets use the Internet Gateway route.
- [x] Web and Data subnets implicitly use the main route table.
- [x] The main route table uses the available NAT Gateway.

