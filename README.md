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

## 🪸 Business Context
Steel manufacturing often involves batch operations across multiple stages with shared equipment and cleaning constraints. Improper sequencing leads to excessive downtime, batch waste, and late deliveries.

This MILP optimizer helps planners:
- Plan batches per division respecting minimum campaign sizes before cleaning is mandatory
- Sequence production runs to minimize costly changeovers
- Schedule production to meet customer demand and improve OTIF metrics

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
### Decision Variables
- x[p][s][t] ∈ {0,1}: Whether product p is scheduled at stage s at time t
- z[p][s][t] ∈ {0,15}: Actual batch size of product p at stage s, time t (0 if not active)
- start_time[b] - start time for batch 'b'
- batch_size[b] - batch size of batch 'b'
- assign[p, b] - binary variable to assign product p to batch b
- sequence[i, j]- binary variable to order batches (to model sequencing, '1' if 'b1' before 'b2')
- makespan - total time to finish all campaigns

### Parameters
- Demand per product 'D_p'
- Minimum and maximum campaign lengths per product 'min_campaign_p', 'max_campaign_p'
- Processing time per batch 'proc_time_p'
- Cleaning time for changeover from product 'i' to 'j' in a stage 'clean_time_stage[i][j]'
- Storage capacity limits between stages 'storage_max_stage'
- Batch size limits per product
- Time horizon 'H'

### Objective
-        minimize Σ(processing_time[p][s] * x[p][s][t]

### Constraints
- Campaign run length between min_campaign[p] and max_campaign[p]
- Changeover time enforcement between product switches
- Storage buffer limits between stages
- Demand fulfillment using variable batch sizes
- Batch size z[p][s][t] linked to binary decision x[p][s][t]

---

## 🪶 
