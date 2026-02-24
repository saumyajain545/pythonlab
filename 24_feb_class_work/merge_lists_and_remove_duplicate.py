# Function to merge two lists and remove duplicates
def merge_and_remove_duplicates(list1, list2):
    merged_list = []   # Empty list to store unique elements

    # Add elements of first list
    for item in list1:
        if item not in merged_list:
            merged_list.append(item)

    # Add elements of second list
    for item in list2:
        if item not in merged_list:
            merged_list.append(item)

    return merged_list

# Read first list from input
list1 = input("Enter elements of first list separated by spaces: ").split()

# Read second list from input
list2 = input("Enter elements of second list separated by spaces: ").split()

# Convert input values to integers
list1 = [int(x) for x in list1]
list2 = [int(x) for x in list2]

# Call the function
result = merge_and_remove_duplicates(list1, list2)

# Print the final list
print("Merged list without duplicates:")
print(result)

#output
#Enter elements of first list separated by spaces: 1 2 3 4
#Enter elements of second list separated by spaces: 3 4 5 6
#Merged list without duplicates:
[1, 2, 3, 4, 5, 6]
