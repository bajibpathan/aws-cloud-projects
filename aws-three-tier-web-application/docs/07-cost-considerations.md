# Cost Considerations

## Cost-aware choices

- Single-AZ, free-tier-eligible RDS was selected for the rebuild.
- EC2 uses small development instances.
- One NAT Gateway is used instead of one per AZ.
- Detailed monitoring and optional services are minimized.
- Resources are intended to exist only for the practice and evidence window.

## Chargeable services to watch

- NAT Gateway hourly and data-processing charges
- Application Load Balancer hours and capacity units
- EC2 usage beyond available free-tier hours or credits
- RDS usage or storage beyond the eligible allowance
- Secrets Manager secrets and rotation invocations
- Elastic IP charges when not attached to a qualifying resource

## Trade-offs

The cost-controlled choices intentionally reduce database and outbound-path resilience. They must be described as lab constraints, not production-ready high availability.

## Controls

- Use an AWS Budget and billing alerts.
- Record resource creation time.
- Complete testing in one planned window.
- Follow the dependency-aware cleanup guide.
- Recheck the console and billing dashboard after teardown.

