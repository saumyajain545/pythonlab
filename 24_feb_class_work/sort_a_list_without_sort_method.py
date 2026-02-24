# Function to sort a list without using sort()
def sort_list(lst):
    n = len(lst)
    
    # Loop through all elements
    for i in range(n):
        # Assume the current index has the smallest element
        min_index = i
        
        # Find the smallest element in remaining list
        for j in range(i + 1, n):
            if lst[j] < lst[min_index]:
                min_index = j
        
        # Swap the found smallest element with current element
        lst[i], lst[min_index] = lst[min_index], lst[i]
    
    return lst

# Read list elements from standard input
elements = input("Enter list elements separated by spaces: ").split()
# Convert input strings to integers
elements = [int(x) for x in elements]

# Call the function and print sorted list
print("Sorted list:", sort_list(elements))

#output
#Enter list elements separated by spaces: 5 2 9 1 3
#Sorted list: [1, 2, 3, 5, 9]
