# Program to create and raise a custom exception

age = int(input("Enter your age: "))    # Take age input

if age < 18:                            # Check if age is less than 18
    raise Exception("Not eligible")     # Raise custom exception

print("Eligible")                       # Display eligible message

# Output Example
# Enter your age: 16
# Exception: Not eligible
