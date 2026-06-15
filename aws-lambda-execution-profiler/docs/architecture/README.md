# 🏗 AWS Lambda Execution Profiler – Architecture Overview

This project uses the AWS Lambda Power Tuning state machine to benchmark a Lambda function across multiple memory configurations.
The goal is to identify the optimal memory setting that provides the best balance between performance and cost.


There are two main flows:

- **User flow (application path)** – how a normal user invokes the Lambda.
- **Developer flow (profiling path)** – how a developer profiles and optimizes the Lambda.

---

## Architecture diagram

Below is a simplified view of how the components interact

![Architecture Diagram](../diagrams//high-level-architecture.png)

---

## ☁️ AWS Services Used

- **Amazon API Gateway** 
    - Receives HTTP requests from the user and triggers the Lambda function.
- **AWS Lambda**
    - Executes the business logic and is the function being profiled.
- **Amazon DynamoDB**
    - Stores or retrieves data during Lambda execution.
- **AWS Step Functions**
    - Runs the Lambda Power Tuning state machine to test multiple memory configurations.
- **AWS Lambda Power Tuning**
    - An open‑source Step Functions workflow that benchmarks Lambda performance.

---

## 🔁 End‑to‑End Flow
- User Flow (Application Path)
    - A user sends a request to API Gateway.
    - API Gateway triggers the Lambda function.
    - The Lambda function interacts with DynamoDB to read/write data.

- Developer Flow (Profiling Path)
    - A developer triggers the Lambda Power Tuning workflow.
    - Step Functions invokes the Lambda function with multiple memory sizes:
        - 128 MB
        - 256 MB
        - 512 MB
        - 1024 MB
    - Step Functions aggregates results into a JSON output.
    - A visualization is generated (chart).
    - The profiler recommends the optimal memory configuration (X MB).

---
## ⭐ Key Architecture Benefits

**1. Data‑Driven Optimization:** 
- No more guessing — memory settings are chosen based on real execution metrics.

**2. Cost Efficiency:** 
- Higher memory can reduce total cost by reducing execution time. The profiler identifies the sweet spot.

**3. Performance Insights:**
- You gain visibility into:
    - Execution duration
    - Cost per invocation

**4. Repeatable & Automated:**
- The Step Functions workflow makes profiling:
    - Consistent
    - Reproducible
    - Easy to re-run when workloads change
