# Program to handle division by zero exception

try:                                   # Start try block
    num1 = int(input("Enter first number: "))   # Take first number
    num2 = int(input("Enter second number: "))  # Take second number
    result = num1 / num2                         # Perform division
    print("Result:", result)                     # Display result

except ZeroDivisionError:               # Catch division by zero error
    print("Cannot divide by zero")      # Display error message

# Output Example
# Enter first number: 10
# Enter second number: 0
# Cannot divide by zero
