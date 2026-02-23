# Step 1: Given list of employee salaries
salaries = [18000, 25000, 60000, 52000, 40000, 75000]

# Step 2: Remove salaries below minimum wage (20,000)
valid_salaries = []
for s in salaries:
    if s >= 20000:
        valid_salaries.append(s)

# Step 3: Add 5% bonus to salaries greater than 50,000
for i in range(len(valid_salaries)):
    if valid_salaries[i] > 50000:
        valid_salaries[i] = valid_salaries[i] + valid_salaries[i] * 0.05

# Step 4: Sort salaries in descending order
valid_salaries.sort(reverse=True)

# Step 5: Display top 3 highest salaries
print("Top 3 highest salaries:", valid_salaries[:3])

#output
#Top 3 highest salaries: [78750.0, 63000.0, 54600.0]
