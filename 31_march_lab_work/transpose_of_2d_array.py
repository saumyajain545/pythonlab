import numpy as np

# Input 2D array
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])

# Transpose the matrix
transposed = matrix.T  # or np.transpose(matrix)

# Output
print("Transposed Matrix:\n", transposed)

'''
output
Transposed Matrix:
 [[1 4]
 [2 5]
 [3 6]]
 '''
