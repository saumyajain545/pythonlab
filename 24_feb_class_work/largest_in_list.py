# Function to find the largest element in a list
def largest_element(lst):
    largest = lst[0]  # Assume first element is largest initially
    for item in lst:
        if item > largest:
            largest = item  # Update largest if current item is greater
    return largest

# Read list elements from the user
elements = input("Enter list elements separated by spaces: ").split()
# Convert input to integers
elements = [int(x) for x in elements]

# Call the function and print the largest element
print("Largest element in the list is:", largest_element(elements))

#output
#Enter list elements separated by spaces: 10 25 5 70 30
#Largest element in the list is: 70
