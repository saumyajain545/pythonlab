# Function to calculate factorial
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i  # Multiply each number from 1 to n
    return result

# Read a number from standard input
num = int(input("Enter a number: "))

# Call the factorial function and print the result
print("Factorial of", num, "is:", factorial(num))

#output
#Enter a number: 5
#Factorial of 5 is: 120
