# Source and Attribution

## Application source

The original Next.js frontend and Flask backend are provided by **IaaS Academy** for its AWS Solutions Architect Associate course:

https://github.com/iaasacademy/aws-solutions-architect-associate/tree/main/section11

This documentation package does not redistribute those archives or application source files. Obtain them from the original repository and follow the course's applicable usage terms. This package does not assign a license to upstream code.

## Work completed by Baji Pathan

- Console deployment of the documented AWS infrastructure.
- Docker image builds and publication to private ECR repositories.
- Backend environment changes for region `eu-west-2` and secret `ritualroast-recipe-secret`.
- ECS services, ALB routing, health validation, and recipe workflow testing.
- Countdown date update and frontend rolling deployment.
- Lab resource cleanup.

The application itself is course-provided. The portfolio documents hands-on implementation and operational learning rather than claiming authorship of the original application.

## Evidence scope

The documentation combines supplied course transcripts with the author's explicit configuration and result confirmations. Exact deployed settings that were not separately supplied are labeled as course settings or omitted. No credentials, account IDs, actual secret values, or fabricated image digests are included.

## Optional source folders

If application redistribution is permitted and desired, place the actual modified source under `frontend/` and `backend/`, preserving upstream notices. Include their Dockerfiles and dependency manifests. Exclude node_modules, build caches, downloaded ZIPs, credentials, and local AWS configuration.
