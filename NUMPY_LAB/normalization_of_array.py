# Program to normalize an array between 0 and 1

import numpy as np

# Generate 10 random numbers between 0 and 1
arr = np.random.rand(10)

# Normalize array
normalized = (arr - arr.min()) / (arr.max() - arr.min())

# Print arrays
print("Original Array:")
print(arr)

print("Normalized Array:")
print(normalized)

# Output (Example)
# Original Array:
# [0.54 0.21 0.87 0.12 0.63 ...]
#
# Normalized Array:
# [0.56 0.12 0.95 0.00 0.67 ...]
