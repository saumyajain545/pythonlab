# Program to replace all even numbers with 0 in a NumPy array

import numpy as np

# Create array from 1 to 10
arr = np.arange(1, 11)

# Replace even numbers with 0
arr[arr % 2 == 0] = 0

# Print result
print(arr)

# Output
# [1 0 3 0 5 0 7 0 9 0]
