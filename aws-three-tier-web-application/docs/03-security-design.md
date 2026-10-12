# Security Design

## Security groups

| Security group | Rule | Source |
|---|---|---|
| `ritual-roast-alb-sg` | TCP `80` | `0.0.0.0/0` |
| `ritual-roast-web-sg` | TCP `5000` | `ritual-roast-alb-sg` |
| `ritual-roast-db-sg` | TCP `3306` | `ritual-roast-web-sg` |
| `ritual-roast-db-sg` | TCP `3306` | `ritual-roast-db-sg` |

The self-reference supports the credential-rotation Lambda configuration. No public SSH or public MySQL rule is used.

## EC2 role

`ritual-roast-master-ec2-iam-role` trusts EC2 and includes:

| Policy | Purpose |
|---|---|
| `AmazonSSMManagedInstanceCore` | Systems Manager registration and Session Manager |
| `AmazonS3FullAccess` | Guided-lab artifact access |
| `ritual-roast-rds-db-secret-policy` | `secretsmanager:GetSecretValue` for the DB secret |

`AmazonS3FullAccess` is broader than required. A production role should use the example in `policies/ec2-s3-read-example.json` and substitute the real bucket name.

## Secret handling

`ritual-roast-rds-db-secret` stores the RDS master credentials. Seven-day single-user rotation is configured. Source, user data, screenshots, and public documentation must never contain the secret value.

## Least-privilege example

The application needs only `s3:ListBucket`, `s3:GetObject`, and `secretsmanager:GetSecretValue` for named resources. Example policies use placeholders so public documentation does not expose account-specific ARNs.

## Validation

- [x] Tier rules use security-group references.
- [x] RDS is not publicly accessible.
- [x] EC2 uses Session Manager rather than SSH.
- [x] The EC2 role is attached through the launch template.
- [x] Secrets Manager rotation is configured.
- [ ] Replace broad S3 access in a future hardening iteration.

