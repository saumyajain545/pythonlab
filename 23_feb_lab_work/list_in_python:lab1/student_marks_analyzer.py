# List of student marks (some are invalid)
marks = [45, 78, 90, -5, 105, 60]

# List to store valid marks
valid = []

# Remove invalid marks
for m in marks:
    if 0 <= m <= 100:
        valid.append(m)

# Calculate average of valid marks
avg = sum(valid) / len(valid)

# Find highest marks (topper)
topper = max(valid)

# Display results
print("Valid Marks:", valid)
print("Average:", avg)
print("Topper:", topper)

#output
#Valid Marks: [45, 78, 90, 60]
#Average: 68.25
#Topper: 90
