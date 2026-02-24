# Read two numbers from standard input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Store original values for display
x = a
y = b

# Find GCD using Euclidean algorithm with while loop
while b != 0:
    remainder = a % b   # Find remainder
    a = b               # Update a
    b = remainder       # Update b

# When b becomes 0, a contains the GCD
print("GCD of", x, "and", y, "is:", a)

#output
#Enter first number: 36
#Enter second number: 24
#GCD of 36 and 24 is: 12
