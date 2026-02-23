# Movie ratings list
ratings = [5, 4, 6, 3, 0, 5]

# Remove invalid ratings
valid = []
for r in ratings:
    if 1 <= r <= 5:
        valid.append(r)

# Calculate average rating
avg = sum(valid) / len(valid)

# Display rating details
print("Average Rating:", avg)
print("5 Star Count:", valid.count(5))

# Sort ratings in ascending order
valid.sort()
print("Sorted Ratings:", valid)

#output
#Average Rating: 4.25
#5 Star Count: 2
#Sorted Ratings: [3, 4, 5, 5]
