# 🚀 Deployment Guide — AWS Lambda Execution Profiler

This guide explains how to deploy the AWS Lambda Execution Profiler, including
the Lambda function, Step Functions state machine, and required IAM roles.

---

## 📦 Prerequisites

Before deploying, ensure you have:
 
- An AWS account with access to:
  - AWS Lambda
  - AWS Step Functions
  - Amazon DynamoDB
  - Amazon API Gateway
- Complete the deployments defined in the [serverless-dynamodb-crud-api](../../../serverless-dynamodb-crud-api/docs/deployment/deployment-guide.md)

---

## 🔧 1. Deploy the Step Functions State Machine
1. Go to Serverless Application Repository
![Serverless App Repository](./images/power-tuning/pt-serverless-app-rep.png)

2. Click Available Applications,type **“power-tuning”** in the search applications by name text box, check “Show apps that create custom IAM roles or resource policies”, and click **aws-lambda-power-tuning**
![Applications](./images/power-tuning/pt-serverless-power-app.png)

3. Scroll down, keep everything as is, check “I acknowledge that this app creates custom IAM roles”, click “Deploy”
![Deploy](./images/power-tuning/pt-serverless-deploy.png)

4. Go to step functions
![Step Functions](./images/power-tuning/pt-serverless-step-functions.png)

5. Select the State machine
![Select State Machine](./images/power-tuning/pt-serverless-select-state-machine.png)

6. Click **“Start execution”**
![Start execution](./images/power-tuning/pt-serverless-start-execution.png)

7. Get your Lambda ARN and put in the below JSON. Then copy the whole JSON and put it in input

For Lambda ARN, open your Lambda and copy the ARN number
![Start execution](./images/power-tuning/pt-serverless-lambda-arn.png)

```json
{
  "lambdaARN": "YOUR LAMBDA ARN HERE",
  "powerValues": [
    128,
    256,
    512,
    1024
  ],
  "num": 10,
  "payload": {
    "operation": "list",
    "tableName": "lambda-apigateway",
    "payload": {}
  },
  "parallelInvocation": true,
  "strategy": "cost"
}
```
![Update and Start execution](./images/power-tuning/pt-serverless-update-start.png)

8. Click Execution input and output tab, Select and copy the visualization link
![Execution Output](./images/power-tuning/pt-serverless-execution-output.png)

9. Open the copied link in a new browser window
![Results](./images/power-tuning/pt-serverless-results.png)

