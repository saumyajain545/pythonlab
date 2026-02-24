# Read first list elements from input
list1 = input("Enter elements of first list separated by spaces: ").split()

# Read second list elements from input
list2 = input("Enter elements of second list separated by spaces: ").split()

# Convert input values to integers
list1 = [int(x) for x in list1]
list2 = [int(x) for x in list2]

# Create an empty list to store common elements
common_elements = []

# Loop through first list
for item in list1:
    # Check if element is present in second list
    if item in list2 and item not in common_elements:
        common_elements.append(item)

# Print the result
print("Common elements:", common_elements)

#output
#Enter elements of first list separated by spaces: 1 2 3 4 5
#Enter elements of second list separated by spaces: 3 4 5 6 7
#Common elements: [3, 4, 5]
