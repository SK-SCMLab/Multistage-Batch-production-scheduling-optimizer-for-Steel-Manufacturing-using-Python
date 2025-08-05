from pulp import *
# ---------------------
# Sets and Time Horizon
# ---------------------
P = ['P1', 'P2']  # Products
S =  ['CRD', 'HRD', 'SPD'] # Stages
T = list(range(20)) # Time slots (Planning horizon)

# ---------------------
# Parameters
# ---------------------
processing_time = {
    'P1': {'CRD':2, 'HRD':3, 'SPD':2},
    'P2': {'CRD':3, 'HRD':2, 'SPD':4}
}

changeover_time = {
    'P1': {'P2': {'CRD':1, 'HRD':2, 'SPD':1}},
      'P2': {'P1': {'CRD':1, 'HRD':2, 'SPD':1}}
}

min_campaign = {'P1': 2, 'P2': 2}
max_campaign = {'P1': 5, 'P2': 4}
demand = {'P1': 50, 'P2': 45} # In Units
storage_capacity = {'CRD': 30, 'HRD': 30} # Between stages
max_batch_size = 15 # Max batch size

# ---------------------
# Model Initialization
# ---------------------
model = LpProblem("Steel_Campaign_Scheduling", LpMinimize)

# ---------------------
# Decision variables
# ---------------------
x = LpVariable.dicts("x", (P, S, T), cat='Binary')  # whether p is produced at s in t
z = LpVariable.dicts("z", (P, S, T), lowBound=0, upBound=max_batch_size, cat='Integer') # Actual batch size

# ---------------------
# Objective Function
# ---------------------
model += lpSum(processing_time[p][s] * x[p][s][t] for p in P for s in S for t in T), "Total_Processing_Time"

# ---------------------
# Constraints
# ---------------------

# Campaign size constraints
for p in P:
    for s in S:
        model += lpSum(x[p][s][t] for t in T) >= min_campaign[p]
        model += lpSum(x[p][s][t] for t in T) <= max_campaign[p]

# Changeover constraints
for s in S:
    for t in T[:-1]:
        for p1 in P:
            for p2 in P:
                if p1 != p2 and p2 in changeover_time.get(p1, {}):
                    model += x[p1][s][t] + x[p2][s][t+1] <= 1 + (1 if changeover_time[p1][p2][s] > 0 else 0)

# Storage capacity constraints between stages
for s_index in range(len(S) - 1):
    s = S[s_index]
    next_s = S[s_index + 1]
    for t in T:
        model += lpSum(z[p][s][t] for p in P) - lpSum(z[p][next_s][t] for p in P) <= storage_capacity[s]

# Demand satisfaction
for p in P:
    model += lpSum(z[p][s][t] for s in S for t in T) >= demand[p]

# Link x and z
for p in P:
    for s in S:
        for t in T:
            model += z[p][s][t] <= max_batch_size * x[p][s][t]
        
# -----------------------
# Solve the model
# -----------------------
model.solve()

# -----------------------
# Output
# -----------------------
print(f"Status: {LpStatus[model.status]}")
for p in P:
    for s in S:
        for t in T:
            if x[p][s][t].varValue == 1:
                print(f"{p} scheduled at {s} during time {t} with batch size {int(z[p][s][t].varValue)}")