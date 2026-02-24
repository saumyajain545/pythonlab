# Read a number from standard input
num = int(input("Enter a number: "))

# Initialize factorial result as 1
fact = 1

# Store original number for display
temp = num

# Calculate factorial using while loop
while num > 0:
    fact = fact * num      # Multiply current number
    num = num - 1          # Decrease the number

# Print the factorial
print("Factorial of", temp, "is:", fact)

#output
#Enter a number: 5
#Factorial of 5 is: 120
