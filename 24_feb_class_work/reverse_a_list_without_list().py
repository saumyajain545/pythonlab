# Function to reverse a list without using reverse()
def reverse_list(lst):
    reversed_list = []   # Empty list to store reversed elements
    
    # Traverse the list from last index to first
    for i in range(len(lst) - 1, -1, -1):
        reversed_list.append(lst[i])
    
    return reversed_list

# Read list elements from standard input
elements = input("Enter list elements separated by spaces: ").split()

# Convert input elements to integers
elements = [int(x) for x in elements]

# Call the function
result = reverse_list(elements)

# Print the reversed list
print("Reversed list:")
print(result)

#output
#Enter list elements separated by spaces: 10 20 30 40 50
#Reversed list:
#[50, 40, 30, 20, 10]
