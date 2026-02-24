# Read list elements from input
numbers = input("Enter numbers separated by spaces: ").split()

# Convert input values to integers
numbers = [int(num) for num in numbers]

# Create empty lists for even and odd numbers
even_list = []
odd_list = []

# Loop through each number in the list
for num in numbers:
    if num % 2 == 0:
        even_list.append(num)   # Add even number
    else:
        odd_list.append(num)    # Add odd number

# Print the results
print("Even numbers:", even_list)
print("Odd numbers:", odd_list)

#output
#Enter numbers separated by spaces: 1 2 3 4 5 6 7 8
#Even numbers: [2, 4, 6, 8]
#Odd numbers: [1, 3, 5, 7]
