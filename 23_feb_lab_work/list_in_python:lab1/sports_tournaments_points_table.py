# Points of teams
points = [50, -10, 70, 30]

# Replace negative points with 0
for i in range(len(points)):
    if points[i] < 0:
        points[i] = 0

# Sort points in descending order
points.sort(reverse=True)

# Display winner and runner-up
print("Winner:", points[0])
print("Runner-up:", points[1])
print("Leaderboard:", points)

#output
Winner: 70
Runner-up: 50
Leaderboard: [70, 50, 30, 0]
