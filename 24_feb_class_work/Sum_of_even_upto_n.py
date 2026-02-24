# Read the value of N from standard input
N = int(input("Enter the value of N: "))

# Variable to store sum of even numbers
sum_even = 0

# Initialize counter
i = 2   # first even number

# Loop through even numbers up to N
while i <= N:
    sum_even = sum_even + i   # add even number to sum
    i = i + 2                 # move to next even number

# Print the result
print("Sum of even numbers up to", N, "is:", sum_even)

#output
#Enter the value of N: 10
#Sum of even numbers up to 10 is: 30
