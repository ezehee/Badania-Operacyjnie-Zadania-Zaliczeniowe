from pulp import LpProblem, LpMinimize, LpVariable, lpSum

# Zadanie z Kolokwium 2024 Wersja 4
#      | 25 | 25 | 40 | 30
#   ----------------------
#   30 | 5  | 5  | 6  | 2
#   35 | 1  | 7  | 4  | 2
#   60 | 6  | 3  | 2  | 1
# Dane problemu
supply = [30, 35, 60]  # Dostępność z magazynów

demand = [25, 25, 40, 30]  # Zapotrzebowanie odbiorców

# Koszty transportu
costs = [
    [5, 5, 6, 2],
    [1, 7, 4, 2],
    [6, 3, 2, 1]
]

# Tworzenie problemu minimalizacyjnego
problem = LpProblem("Zagadnienie_Transportowe", LpMinimize)

# Zmienne decyzyjne
decision_variables = [
    [LpVariable(f"x_{i}_{j}", lowBound=0) for j in range(len(demand))]
    for i in range(len(supply))
]

# Funkcja celu (minimalizacja kosztów)
problem += lpSum(
    decision_variables[i][j] * costs[i][j]
    for i in range(len(supply))
    for j in range(len(demand))
), "Koszty Transportu"

# Ograniczenia podaży
for i in range(len(supply)):
    problem += lpSum(decision_variables[i][j] for j in range(len(demand))) <= supply[i], f"Ograniczenie_podazy_{i}"

# Ograniczenia popytu
for j in range(len(demand)):
    problem += lpSum(decision_variables[i][j] for i in range(len(supply))) == demand[j], f"Ograniczenie_popytu_{j}"

# Rozwiązywanie problemu
problem.solve()

# Wyniki
print("Status:", problem.status)
print("Minimalny koszt transportu:", problem.objective.value())
for i in range(len(supply)):
    for j in range(len(demand)):
        print(f"Transport z magazynu {i} do odbiorcy {j}: {decision_variables[i][j].varValue}")
