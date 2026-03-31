import numpy as np

# Input matrices
A = np.array([[1, 2, 3],
              [4, 5, 6]])

B = np.array([[7, 8],
              [9, 10],
              [11, 12]])

# Matrix multiplication
C = np.dot(A, B)  # or A @ B

# Output
print("Resultant Matrix:\n", C)

'''
output
Resultant Matrix:
 [[ 58  64]
 [139 154]]
 '''
