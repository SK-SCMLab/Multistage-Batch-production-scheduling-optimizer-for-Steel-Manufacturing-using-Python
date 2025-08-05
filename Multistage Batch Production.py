import pulp

# Define stages and products with parameters
stages = ['CRD', 'HRD', 'SPD']

products = {
    'A': {'demand': 1000, 'proc_time': 10, 'min_campaign': 2, 'max_campaign': 10},
    'B': {'demand': 800, 'proc_time': 8, 'min_campaign': 3, 'max_campaign': 12},
    'C': {'demand': 600, 'proc_time': 10, 'min_campaign': 1, 'max_campaign': 5},
}
prod_stage = {'A': 'HRD', 'B': 'CRD', 'C': 'SPD'}

clean_time = {
'CRD': {('A', 'A'):0, ('A', 'B'):2, ('A', 'C'):3, ('B', 'A'):2, ('B', 'B'):0, ('B', 'C'):2, ('C', 'A'):3, ('C', 'B'):2, ('C', 'C'):0},
'HRD': {('A', 'A'):0, ('A', 'B'):3, ('A', 'C'):2, ('B', 'A'):3, ('B', 'B'):0, ('B', 'C'):2, ('C', 'A'):2, ('C', 'B'):3, ('C', 'C'):0},
'SPD': {('A', 'A'):0, ('A', 'B'):1, ('A', 'C'):2, ('B', 'A'):1, ('B', 'B'):0, ('B', 'C'):2, ('C', 'A'):2, ('C', 'B'):2, ('C', 'C'):0},
}

max_batches = 15
H = 2000

prob = pulp.LpProblem("Steel_Multistage_Batch_Scheduling", pulp.LpMinimize)

assign = pulp.LpVariable.dicts("assign", ((p,b) for p in products for b in range(max_batches)), 0, 1, pulp.LpBinary)
batch_size = pulp.LpVariable.dicts("batch_size", (b for b in range(max_batches)), lowBound=0)
start_time = pulp.LpVariable.dicts("start_time", (b for b in range(max_batches)), lowBound=0)
sequence = pulp.LpVariable.dicts("sequence", ((i,j) for i in range(nax_batches) for j in range(max_batches) if i != j), 0, 1, pulp.LpBinary)
makespan = pulp.LpVariable("makespa", lowBound=0)

# Objective function: minimize makespan
prob += makespan, "Minimize Makespan"

# Constraints
for b in range(max_batches):
    prob += pulp.lpSum(assign[p, b] for p in products) <= 1

for p in products:
    prob += pulp.lpSum(batch_size[b]*assign[p,b]
    for b in range(max_batches)) >= products[p]['demand']

for p in products:
    for b in range(max_batches):
            prob += batch_size[b] >= products[p]
    ['min_campaign'] * assign[p,b]
            prob += batch_size[b] <= products[p]
    ['max_canmpaign'] * assign[p,b]

for i in range(max_batches):
      for j in range(max_batches):
            if i !=j:
                  for p_i in products:
                        for p_j in products:
                              if prod_stage[p_i] == prod_stage[p_j]:
                                    prob += (start_time[i] + products[p_i]['proc_time'] * batch_size[i] + clean_time[prod_stage[p_i][(p_i, p_j)] <= start_time[j] + H * (3 - assign[p_i, i] - assign[p_j, j] - sequence[(i, j)]))
                                    prob += sequence[(i, j)] + sequence[(j, i)] <= 1

for b in range(max_batches):
    for p in products:
          prob += makespan >= start_time[b] + products[p]['proc_time'] * batch_size[b] - H *(1-assign[p,b])

# Solve
solver = pulp.PULP_CBC_CMD(msg=True)
result = prob.solve(solver)

print("Status:", pulp.LpStatus[prob.status])
print(f"Minimum makespan: {pulp.value(makespan):.2f}hours\n")

print("Batch assignments and schedule:")
for b in range(max_batches):
      assigned_prods = [p for p in products if pulp.value(assign[p,b]) > 0.5]
      if assigned_prods:
            p = assigned_prods[0]
            print(f" Batch {b}: Product {p}, Start time={pulp.value(start_time[b]):.2f},
                  Size={pulp.value(batch_size[b]):.2f}")
