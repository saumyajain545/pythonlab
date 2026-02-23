# Remove lowest two scores
scores.pop(0)
scores.pop(0)

# Add grace marks of 5 for scores between 30 and 35
for i in range(len(scores)):
    if 30 <= scores[i] <= 35:
        scores[i] += 5

# Count passed students (marks >= 40)
passed = 0
for s in scores:
    if s >= 40:
        passed += 1

# Display results
print("Final Scores:", scores)
print("Passed Students:", passed)
#output
#Final Scores: [40, 78, 90]
#Passed Students: 3
