# Read base and exponent from standard input
base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))

# Initialize result
result = 1

# Calculate power using for loop
for _ in range(exponent):
    result = result * base   # Multiply base exponent times

# Print the result
print(base, "raised to the power", exponent, "is:", result

#output
#Enter the base: 2
#Enter the exponent: 5
#2 raised to the power 5 is: 32
