# 📊 Observability Layer Design

## Overview

The Observability Layer provides visibility into the health and performance of the Event-Driven Image Processing application.

As images are uploaded and processed, AWS Lambda automatically publishes operational metrics to Amazon CloudWatch. These metrics, along with application logs and alarms, help monitor the system, troubleshoot issues, and detect failures before they impact users.

At this stage of the project, Amazon CloudWatch is used to collect logs, monitor Lambda performance, visualize operational metrics through dashboards, and generate alerts when errors occur.

---

# 🎯 Objectives

The Observability Layer should:

- Monitor application health.
- Capture execution logs.
- Track Lambda performance.
- Detect processing failures.
- Visualize operational metrics.
- Support troubleshooting and root cause analysis.

---

# 🏗 Architecture

```text
                    User
                      │
                Upload Image
                      │
                      ▼
               Amazon S3 Bucket
                      │
             ObjectCreated Event
                      │
                      ▼
                AWS Lambda
               /            \
              /              \
             ▼                ▼
 CloudWatch Logs      CloudWatch Metrics
                              │
                              ▼
                     CloudWatch Dashboard
                              │
                              ▼
                     CloudWatch Alarm
```

---

# 💡 Design Decision

## Design Decision #4 – Why Amazon CloudWatch?

Amazon CloudWatch was selected because it is the native monitoring and observability service for AWS.

AWS Lambda automatically publishes execution metrics such as:

- Invocations
- Errors
- Duration
- Throttles
- Concurrent Executions

CloudWatch also collects Lambda execution logs without requiring additional infrastructure.

Using CloudWatch allows the project to monitor application health, troubleshoot issues, and visualize performance from a single service.

### Alternatives Considered

| Service | Decision |
|----------|----------|
| **Amazon CloudWatch** | ✅ Selected because it integrates natively with AWS Lambda and provides logs, metrics, dashboards, and alarms. |
| **Amazon OpenSearch** | Better suited for advanced log analytics but unnecessary for the current project. |
| **Splunk** | Powerful enterprise observability platform but introduces additional infrastructure and licensing costs. |
| **Dynatrace** | Excellent full-stack observability solution but outside the scope of this serverless learning project. |

### Benefits

- Native AWS integration
- Automatic Lambda metrics
- Centralized logging
- Dashboards
- Alerting
- Fully managed service

### Trade-offs

- Basic dashboards compared to enterprise observability platforms
- Advanced analytics may require additional AWS services

These trade-offs are acceptable because CloudWatch provides all required monitoring capabilities for this project.

---

# Implementation Details

## CloudWatch Logs

AWS Lambda automatically sends execution logs to:

```text
/aws/lambda/event-image-processor
```

The log retention period was configured to **30 days** to balance troubleshooting needs with storage costs.

---

## CloudWatch Metrics

The following Lambda metrics are monitored:

| Metric | Purpose |
|---------|---------|
| Invocations | Number of Lambda executions |
| Errors | Failed Lambda executions |
| Duration | Average execution time |
| Throttles | Number of throttled requests |

These metrics provide operational visibility into the application's health and performance.

---

## CloudWatch Dashboard

A CloudWatch dashboard named:

```text
EventImageProcessingDashboard
```

was created to visualize key operational metrics.

Dashboard widgets include:

- Lambda Invocations
- Lambda Errors
- Average Duration
- Lambda Throttles
- Error Alarm Status

---

## CloudWatch Alarm

A CloudWatch Alarm was configured to monitor Lambda execution failures.

Configuration:

| Setting | Value |
|----------|-------|
| Metric | Errors |
| Threshold | ≥ 1 |
| Evaluation Period | 5 Minutes |
| Missing Data | Not Breaching |

The alarm changes state whenever one or more Lambda executions fail within the evaluation period.

SNS notifications will be added in a future enhancement.

---

# Security Decisions

## Log Retention

CloudWatch Log retention was configured for **30 days** to avoid indefinite log storage while maintaining sufficient troubleshooting history.

---

## Least Privilege

No additional IAM permissions were required for publishing Lambda metrics because AWS automatically publishes standard Lambda metrics to CloudWatch.

The Lambda Execution Role only contains permissions required for:

- CloudWatch Logs
- DynamoDB PutItem

---

# Validation

The following validations were completed successfully:

- CloudWatch Log Group verified.
- Log retention configured.
- Lambda execution logs validated.
- Lambda metrics verified.
- CloudWatch Dashboard created.
- Dashboard widgets validated.
- CloudWatch Alarm created.
- Alarm status verified.
- Successful image upload reflected in dashboard metrics.

---

# Lessons Learned

- Observability is an essential part of production-ready applications.
- CloudWatch automatically collects Lambda metrics.
- Dashboards simplify operational monitoring.
- Alarms enable proactive detection of failures.
- Log retention should be configured to control storage costs.

---

# Challenges

## Challenge

Initially, it was unclear how CloudWatch Logs, Metrics, Dashboards, and Alarms work together.

### Resolution

By implementing each component individually, it became clear that:

- Logs capture detailed execution information.
- Metrics provide aggregated performance data.
- Dashboards visualize application health.
- Alarms proactively detect failures.

Together, they provide a complete observability solution.

---

# Future Enhancements

Future improvements include:

- Amazon SNS notifications
- CloudWatch Metric Filters
- Custom CloudWatch Metrics
- CloudWatch Contributor Insights
- AWS X-Ray distributed tracing
- Centralized observability dashboards
- Log Insights queries

---

# References

- Amazon CloudWatch Documentation
- AWS Lambda Monitoring Documentation
- AWS Well-Architected Framework – Operational Excellence Pillar