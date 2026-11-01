# Validation

## Validation record

| Test | Observed / reported outcome |
| --- | --- |
| Docker access as ec2-user | Completed successfully |
| Initial secret rotation | Enabled and successful |
| Frontend service | 2/2 tasks running; two healthy targets |
| Backend service | 2/2 tasks running; two healthy targets |
| Homepage through ALB | Working as expected |
| Submit recipe | Working as expected |
| Recipe gallery | Submitted recipe displayed |
| Refresh persistence | Working as expected |
| Countdown release | Update and rolling deployment confirmed completed |
| Cleanup | Confirmed completed |

The course shows two-AZ placement; the author's task-level placement screenshots were not supplied for independent inspection. A healthy API endpoint alone is not proof of all database operations, which is why submission and refresh were checked separately.

No project-specific failure or corrective action was reported. The instructor's transient target-registration issue is not represented as an issue encountered by the author.

