# Program to demonstrate filter function

numbers = [1, 2, 3, 4, 5, 6]            # Create list

even = list(filter(lambda x: x % 2 == 0, numbers))  # Filter even numbers

print("Even numbers:", even)            # Display result

# Output Example
# Even numbers: [2, 4, 6]
