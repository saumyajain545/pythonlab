# Recursive function to calculate power
def power(base, exponent):
    if exponent == 0:
        return 1       # Base case: any number to the power 0 is 1
    else:
        return base * power(base, exponent - 1)  # Multiply base with power(base, exponent-1)

# Read base and exponent from the user
base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))

# Call the recursive function and print the result
print(base, "raised to the power", exponent, "is:", power(base, exponent))

#output
#Enter the base: 2
#Enter the exponent: 5
