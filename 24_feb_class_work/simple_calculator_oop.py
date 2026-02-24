# Program to create a simple calculator using OOP

class Calculator:                       # Define Calculator class
    def add(self, a, b):                # Addition method
        return a + b                    # Return sum

    def subtract(self, a, b):           # Subtraction method
        return a - b                    # Return difference

    def multiply(self, a, b):           # Multiplication method
        return a * b                    # Return product

    def divide(self, a, b):             # Division method
        return a / b                    # Return division result


calc = Calculator()                     # Create object

print("Addition:", calc.add(10, 5))     # Call add method
print("Subtraction:", calc.subtract(10, 5))  # Call subtract method
print("Multiplication:", calc.multiply(10, 5))  # Call multiply method
print("Division:", calc.divide(10, 5))  # Call divide method

# Output Example
# Addition: 15
# Subtraction: 5
# Multiplication: 50
# Division: 2.0
