# Read the number of terms from standard input
n = int(input("Enter the number of terms: "))

# Initialize the first two Fibonacci numbers
a = 0
b = 1

# Print the Fibonacci series using a for loop
for _ in range(n):
    print(a, end=" ")   # Print current term
    c = a + b           # Calculate next term
    a = b               # Update a to next term
    b = c               # Update b to next term

#output
#Enter the number of terms: 7
#0 1 1 2 3 5 8
