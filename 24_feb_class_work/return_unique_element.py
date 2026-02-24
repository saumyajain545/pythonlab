# Function to return unique elements from a list
def unique_elements(lst):
    unique_lst = []  # Initialize empty list to store unique elements
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)  # Add item if not already in unique_lst
    return unique_lst

# Read list elements from the user
elements = input("Enter list elements separated by spaces: ").split()
# Convert input to integers
elements = [int(x) for x in elements]

# Call the function and print unique elements
print("Unique elements:", unique_elements(elements))

#output
#Enter list elements separated by spaces: 1 2 2 3 4 3 5
#Unique elements: [1, 2, 3, 4, 5]
