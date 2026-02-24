# Read the value of N from standard input
N = int(input("Enter a positive integer N: "))

# Initialize sum variable
total = 0

# Loop through numbers from 1 to N
for i in range(1, N + 1):
    total += i   # Add each number to total

# Print the sum
print("Sum of first", N, "natural numbers is:", total)

#output
#Enter a positive integer N: 10
#Sum of first 10 natural numbers is: 55
