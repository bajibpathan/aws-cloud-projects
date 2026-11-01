# Lessons Learned

## Engineering conclusions

- Separate ECS services allow the UI and API to be released independently.
- Fargate removes host administration; container, IAM, network and deployment responsibilities remain.
- Task roles provide application credentials, while execution roles support image pulls and logging. A role name alone does not establish its assignment.
- ALB IP targets and separate health paths connect each service to its own application checks.
- Reusing a mutable tag requires an explicit deployment to replace running tasks.
- Successful secret rotation does not by itself validate application credential refresh.
- Two-AZ task placement does not remove Single-AZ database or single-NAT dependencies.
- Cleanup must include storage and network resources, not just running tasks.

## Scope and improvements

| Area | Lab scope | Future improvement |
| --- | --- | --- |
| Availability | Two tasks per service; Single-AZ database; one NAT | RDS Multi-AZ, resilient egress, explicit failure testing |
| Scaling | Separate services and fixed desired counts | Independent target-tracking policies and load tests |
| Transport | HTTP 80 | HTTPS with ACM and HTTP redirect |
| IAM / network isolation | Shared app SG and task role | Backend-only secret access and DB ingress |
| Secrets | Rotation setup and initial success verified | Validate application credential refresh after rotation |
| Delivery | Manual build/push and forced frontend deployment | Versioned images, CI/CD, rollback validation |
| Observability | Course CloudWatch logging configuration | Confirm log retention, alarms, dashboards, and service-level indicators |
| Application | Course MVP and countdown update | Complete remaining placeholder button actions and input/security review |

There was no reported task-stop recovery test, AZ outage test, RDS failover test, load test, rollback test, or verified runtime credential-refresh test. These are future exercises, not completed outcomes.
