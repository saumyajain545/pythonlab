import numpy as np

# Input array
arr = np.array([10, 20, 30, 40, 50])

# Min and Max
arr_min = arr.min()
arr_max = arr.max()

# Normalize array
normalized = (arr - arr_min) / (arr_max - arr_min)

# Output
print("Normalized Array:", normalized)

#output
#Normalized Array: [0.   0.25 0.5  0.75 1.  ]
