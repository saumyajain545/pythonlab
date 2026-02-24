# Function to find GCD using Euclid's algorithm
def gcd(a, b):
    while b != 0:
        a, b = b, a % b  # Update a to b and b to remainder of a/b
    return a

# Read two numbers from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Call the function and print the GCD
print("GCD of", num1, "and", num2, "is:", gcd(num1, num2))

#output
#Enter first number: 36
#Enter second number: 60
#GCD of 36 and 60 is: 12
