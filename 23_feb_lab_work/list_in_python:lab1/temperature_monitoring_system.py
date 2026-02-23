# Daily temperatures
temps = [38, 42, 46, 35, 49]

# Find hottest and coldest day
print("Hottest:", max(temps))
print("Coldest:", min(temps))

# Replace temperature above 45 with Heat Alert
for i in range(len(temps)):
    if temps[i] > 45:
        temps[i] = "Heat Alert"

# Count extreme days (>40 but not Heat Alert)
count = 0
for t in temps:
    if t != "Heat Alert" and t > 40:
        count += 1

# Display results
print("Updated Temps:", temps)
print("Extreme Days:", count)

#output
#Hottest: 49
#Coldest: 35
#Updated Temps: [38, 42, 'Heat Alert', 35, 'Heat Alert']
#Extreme Days: 1
