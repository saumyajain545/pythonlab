# Function to remove duplicates from a list
def remove_duplicates(lst):
    unique_list = []  # Initialize empty list for unique elements
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)  # Add only if item not already present
    return unique_list

# Read list elements from the user
elements = input("Enter list elements separated by spaces: ").split()
# Convert input to integers
elements = [int(x) for x in elements]

# Call the function and print the list without duplicates
print("List after removing duplicates:", remove_duplicates(elements))

#output
#Enter list elements separated by spaces: 1 2 2 3 4 3 5
#List after removing duplicates: [1, 2, 3, 4, 5]
