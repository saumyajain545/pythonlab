# Function to count frequency of elements in a list
def count_frequency(lst):
    freq = {}  # Dictionary to store frequency of elements
    
    for item in lst:
        if item in freq:
            freq[item] += 1   # Increment count if item already exists
        else:
            freq[item] = 1    # Initialize count to 1 if item appears first time
    
    return freq

# Read list elements from standard input
elements = input("Enter list elements separated by spaces: ").split()
# Convert input elements to integers
elements = [int(x) for x in elements]

# Call the function and print the frequency
result = count_frequency(elements)
print("Frequency of elements:")
print(result)

#output
#nter list elements separated by spaces: 1 2 2 3 3 3 4
#Frequency of elements:
#{1: 1, 2: 2, 3: 3, 4: 1}
