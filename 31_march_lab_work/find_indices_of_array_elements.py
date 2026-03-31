import numpy as np

# Input array
arr = np.array([10, 20, 30, 40, 50])

# Value to compare
val = 25

# Find indices
indices = np.where(arr > val)[0]

# Output
print("Indices of elements greater than", val, ":", indices)

#output
#Indices of elements greater than 25 : [2 3 4]
