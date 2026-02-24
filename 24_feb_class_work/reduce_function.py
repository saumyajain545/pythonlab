# Program to demonstrate reduce function

from functools import reduce            # Import reduce

numbers = [1, 2, 3, 4]                  # Create list

result = reduce(lambda x, y: x + y, numbers)  # Sum all elements

print("Sum using reduce:", result)      # Display result

# Output Example
# Sum using reduce: 10
