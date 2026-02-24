# Function to find the second largest element in a list
def second_largest(lst):
    # Remove duplicate elements
    unique_list = list(set(lst))
    
    # Check if there are at least two unique elements
    if len(unique_list) < 2:
        return None
    
    # Find the largest element
    largest = unique_list[0]
    for item in unique_list:
        if item > largest:
            largest = item
    
    # Find the second largest element
    second = None
    for item in unique_list:
        if item != largest:
            if second is None or item > second:
                second = item
    
    return second

# Read list elements from the user
elements = input("Enter list elements separated by spaces: ").split()
# Convert input to integers
elements = [int(x) for x in elements]

# Call the function and print the second largest element
result = second_largest(elements)
if result is not None:
    print("Second largest element is:", result)
else:
    print("Second largest element does not exist")

#output
#Enter list elements separated by spaces: 10 20 30 40 50
#Second largest element is: 40
