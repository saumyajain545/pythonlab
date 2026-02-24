# Read a number from standard input
num = int(input("Enter a number: "))

# Initialize factorial result as 1
fact = 1

# Calculate factorial using for loop
for i in range(1, num + 1):
    fact = fact * i   # Multiply each number from 1 to num

# Print the factorial
print("Factorial of", num, "is:", fact)

#output
#Enter a number: 5
#Factorial of 5 is: 120
