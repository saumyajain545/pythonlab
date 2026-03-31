# Input dictionary
original = {'a': 1, 'b': 2, 'c': 3}

# Swap keys and values using dictionary comprehension
swapped = {value: key for key, value in original.items()}

# Output result
print("Swapped Dictionary:", swapped)

#output
#Swapped Dictionary: {1: 'a', 2: 'b', 3: 'c'}
