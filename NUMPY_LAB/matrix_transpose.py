# Program to find transpose of a matrix

import numpy as np

# Create matrix
matrix = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])

# Find transpose
transpose_matrix = matrix.T

# Print transpose
print("Transpose Matrix:")
print(transpose_matrix)

# Output
# [[1 4 7]
#  [2 5 8]
#  [3 6 9]]
