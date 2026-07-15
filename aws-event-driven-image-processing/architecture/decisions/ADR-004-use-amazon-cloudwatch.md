# ADR-004 – Use Amazon CloudWatch for Monitoring and Observability

## Status

**Accepted**

---

# Context

The application requires operational visibility to monitor the health and performance of the event-driven workflow.

The monitoring solution should provide:

- Application logs
- Performance metrics
- Error monitoring
- Operational dashboards
- Alerting capabilities
- Native integration with AWS services
- Minimal operational overhead

Since the application is fully serverless and runs entirely within AWS, the monitoring solution should integrate seamlessly with the AWS ecosystem.

---

# Decision

Amazon CloudWatch was selected as the primary monitoring and observability service.

CloudWatch is used to:

- Collect AWS Lambda execution logs
- Monitor Lambda performance metrics
- Create operational dashboards
- Generate alarms for application failures
- Support troubleshooting through centralized logging

The project uses the following CloudWatch features:

- CloudWatch Logs
- CloudWatch Metrics
- CloudWatch Dashboard
- CloudWatch Alarm

This provides complete operational visibility without introducing additional infrastructure.

---

# Alternatives Considered

## Dynatrace

### Pros

- End-to-end distributed tracing
- Automatic topology discovery
- AI-powered root cause analysis
- Deep application observability
- Excellent for enterprise environments

### Cons

- Additional licensing costs
- Requires integration with AWS
- More advanced than required for this learning project

---

## Splunk

### Pros

- Powerful log analytics
- Flexible search capabilities
- Centralized log management
- Supports multiple platforms

### Cons

- Additional infrastructure or licensing
- Separate log ingestion pipeline
- More operational overhead

---

## Prometheus + Grafana

### Pros

- Excellent for Kubernetes environments
- Highly customizable dashboards
- Strong open-source ecosystem

### Cons

- Requires deployment and management
- Better suited for containerized workloads
- Additional operational complexity

---

## ELK Stack (Elasticsearch, Logstash, Kibana)

### Pros

- Powerful log analysis
- Flexible visualization
- Open-source ecosystem

### Cons

- Requires infrastructure management
- Higher maintenance effort
- Additional storage requirements

---

# Consequences

## Positive

- Native integration with AWS services
- Automatic Lambda metrics
- Centralized log collection
- Built-in dashboards
- Alarming without additional infrastructure
- Minimal operational overhead
- Pay-as-you-use pricing

## Negative

- Less advanced application observability compared to enterprise platforms
- Limited distributed tracing without AWS X-Ray
- Custom metrics may increase costs
- Cross-platform monitoring requires additional integrations

These trade-offs were acceptable because the project focuses on AWS-native serverless services.

---

# Why Amazon CloudWatch Was the Best Choice

The application architecture is simple and entirely serverless.

```text
Amazon S3

↓

AWS Lambda

↓

Amazon DynamoDB

↓

Amazon CloudWatch
```

Because CloudWatch integrates natively with AWS Lambda, no additional agents, collectors, or infrastructure are required.

This reduces operational complexity while still providing sufficient monitoring for the application's requirements.

---

# Future Enhancements

As the application grows, additional observability capabilities may be introduced.

Potential enhancements include:

- AWS X-Ray for distributed tracing
- Amazon EventBridge for operational event routing
- Amazon SNS for operational notifications
- Integration with enterprise observability platforms
- Custom CloudWatch metrics
- CloudWatch Logs Insights queries

These services can extend the monitoring capabilities while preserving the existing CloudWatch foundation.

---

# References

- Amazon CloudWatch Documentation
- AWS Lambda Monitoring Documentation
- AWS Well-Architected Framework
- AWS Well-Architected Operational Excellence Pillar