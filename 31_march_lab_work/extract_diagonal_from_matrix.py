import numpy as np

# Input 2D matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Extract diagonal elements
diagonal = np.diag(matrix)

# Output
print("Diagonal elements:", diagonal)

#output
#Diagonal elements: [1 5 9]
