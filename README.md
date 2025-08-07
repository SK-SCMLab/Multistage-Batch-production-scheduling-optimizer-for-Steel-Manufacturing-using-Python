# 🪁 Multistage-Batch-production-scheduling-optimizer-for-Steel-Manufacturing-using-Python
This repository provides a Python-based MILP optimizer using PuLP for solving multistage batch production problems in a steel manufacturing setup with shared resources

---

## 🛷 MILP
A Mixed-Integer Linear Programming (MILP) optimizer for multistage batch production scheduling in a steel manufacturing environment, considering shared resources, cleaning changeovers, and storage limits

---

## 🎫 Problem Context
In Steel manufacturing environment, there are three major divisions:
1. CRD (Cold Rolling Division)
2. HRD (Hot Rolling Division)
3. SPD (Special Product Division)

Each product must be scheduled and processed under various constraints like:
- Batch sizes
- Campaign cleaning restrictions
- Changeover cleaning time
- Intermediate storage capacity
- Demand fulfillment
- OTIF improvement

---

## 🐞 Features
- Multi-stage production: **CRD -> HRD -> SPD**
- Max batch size = **15 units**
- **Variable batch sizes** supported (especially for last batches)
- **Campaign Logic** = Minimum and maximum runs per product before cleaning
- **Changeover times** between different product runs
- **Intermediate storage** constraints between stages
- **Demand fulfillment** for each product
- **Objective**: Minimize total processing time while meeting demand and avoiding resource conflicts

---

## 🫏 Optimization Goals
- Minimize makespan
- Maximize throughput
- Meet product demand
- Respect all campaign constraints
- Improve OTIF (On Time In Full)

---

## 🐍 Mathematical model
**Decision Variables**
- x[p][s][t] ∈ {0,1}: Whether product p is scheduled at stage s at time t
- z[p][s][t] ∈ {0,15}: Actual batch size of product p at stage s, time t (0 if not active)

---

## 🫎 Objective
-        minimize Σ(processing_time[p][s] * x[p][s][t]

---
## 🪼 Constraints
- Campaign run length between min_campaign[p] and max_campaign[p]
- Changeover time enforcement between product switches
- Storage buffer limits between stages
- Demand fulfillment using variable batch sizes
- Batch size z[p][s][t] linked to binary decision x[p][s][t]

---

