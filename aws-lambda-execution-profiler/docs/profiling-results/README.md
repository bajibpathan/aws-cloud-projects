# 📊 AWS Lambda Execution Profiler — Results Analysis

This document provides a detailed analysis of the Lambda Power Tuning results for the **aws-lambda-execution-profiler** project.  

The goal is to understand how different memory configurations impact execution time, cost, and overall performance efficiency.

## Results Graph
![Results](../deployment/images/power-tuning/pt-serverless-results.png)

## 📈 1. Overview of the Graph

The graph compares:

- Invocation Time (ms) — red curve  
- Invocation Cost (USD) — blue curve  

Across four memory configurations:

- 128 MB  
- 256 MB  
- 512 MB  
- 1024 MB  

Summary from the results:

- **Best Cost → 128 MB**  
- **Best Time → 1024 MB**  
- **Worst Cost → 256 MB**  
- **Worst Time → 256 MB**

This indicates that **256 MB is the least efficient tier** for this workload.

---

## 🧪 2. Profiling Results

| Memory (MB) | Invocation Time (ms) | Invocation Cost (USD) | 
|-------------|----------------------|-------------------------|
| **128 MB**  | 350 ms               | $0.0000012              | 
| **256 MB**  | 650 ms               | $0.0000028              | 
| **512 MB**  | 420 ms               | $0.0000018              | 
| **1024 MB** | 250 ms               | $0.0000014              | 

---

## 🧪 3. Invocation Time Analysis (Red Curve)

### 128 MB
- Slow, but not the slowest.
- Expected due to lowest CPU allocation.

### 256 MB
- **Worst execution time**.
- Indicates a CPU bottleneck at this tier.

### 512 MB
- Significant improvement.
- CPU scaling begins to benefit the workload.

### 1024 MB
- **Fastest execution time**.
- Highest CPU allocation → best performance.

### Conclusion
If latency matters, **1024 MB** is the optimal choice.

---

## 💵 4. Invocation Cost Analysis (Blue Curve)

### 128 MB
- **Lowest cost**.
- Even though slower, the billed duration × price is still cheapest.

### 256 MB
- **Highest cost**.
- Worst combination of slow execution + higher per‑ms price.

### 512 MB
- Cost decreases.
- Faster execution offsets higher memory price.

### 1024 MB
- Cost decreases further.
- Faster execution reduces total billed duration.

### Conclusion
If cost is the priority, **128 MB** wins — but only for non‑critical workloads.

---

## ⚖️ 5. Performance vs Cost Trade‑off
| Memory | Time | Cost | Verdict |
|--------|------|-------|---------|
| 128 MB | Slow | Cheapest | Good for low‑priority workloads |
| 256 MB | Worst | Worst | Avoid |
| 512 MB | Good | Good | Balanced |
| 1024 MB | Best | Second‑best | ⭐ Best overall |

### ⭐ Best Overall Choice: 1024 MB

Reasons:

- Fastest execution  
- Cost still low  
- Best performance/cost ratio  
- Most stable for production workloads  

---

## 🧠 6. Key Insights

- More memory **does not always mean higher cost** — faster execution reduces billed duration.  
- **256 MB is a poor choice** for this workload.  
- **1024 MB provides the best performance** and strong cost efficiency.  
- **128 MB is cheapest**, but too slow for most real‑world use cases.  
- The profiler reveals **non‑linear performance behavior**, which is exactly why tuning matters.

---

## 🏆 7. Recommended Memory Configuration

### **Optimal Memory Setting: 1024 MB**

This configuration provides the best balance of:

- Execution speed  
- Cost efficiency  
- CPU scaling  
- Predictable performance
