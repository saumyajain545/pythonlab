# Input nested list
nested_list = [[1, 2], [3, 4, 5], [6]]

# Empty list to store flattened result
flat_list = []

# Flatten the list
for sublist in nested_list:
    for item in sublist:
        flat_list.append(item)

# Output
print("Flattened list:", flat_list)

#output
#Flattened list: [1, 2, 3, 4, 5, 6]
