# Troubleshooting

## Incident: ALB targets remained unhealthy

### Symptom

The Auto Scaling group launched two instances and registered them with the target group, but health checks failed.

### Diagnostic approach

1. Reviewed the target-health status details.
2. Connected to a private instance through Session Manager.
3. Inspected `/var/log/user-data.log` and `/var/log/flask-app.log`.
4. Checked the port with `ss -lntp` and tested the local endpoint with `curl`.
5. Reviewed the application's external dependencies.

### Root cause

`ritual-roast.py` referenced an incorrect Secrets Manager secret name. The application could not retrieve the RDS credentials and did not become a healthy target.

### Resolution

The secret name was corrected, the application file was uploaded as a new S3 version, and Auto Scaling instances were replaced so they downloaded the corrected artifact.

### Validation

Both replacement targets became healthy, the ALB served the application, and recipe submission and retrieval worked.

## Useful commands

```bash
sudo tail -n 200 /var/log/user-data.log
sudo tail -n 200 /var/log/flask-app.log
sudo ss -lntp | grep :5000
curl -i http://127.0.0.1:5000/
```

## Lesson

Healthy infrastructure does not guarantee a healthy application. Target-health failures require checking the full dependency chain: bootstrap, artifact delivery, process startup, network rules, secrets, and database connectivity.

