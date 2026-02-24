# Program to demonstrate map function

numbers = [1, 2, 3, 4]                  # Create list

squares = list(map(lambda x: x*x, numbers))   # Apply lambda to each element

print("Squares:", squares)              # Display result

# Output Example
# Squares: [1, 4, 9, 16]
