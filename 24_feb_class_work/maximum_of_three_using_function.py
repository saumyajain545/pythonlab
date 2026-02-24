# Function to find maximum of three numbers
def maximum(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Read three numbers from standard input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

# Call the function and print the maximum
print("Maximum number is:", maximum(num1, num2, num3))

#output
#Enter first number: 10
#Enter second number: 25
#Enter third number: 15
#Maximum number is: 25
