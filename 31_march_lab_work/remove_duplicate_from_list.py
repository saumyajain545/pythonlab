# Input list
nums = [1, 2, 2, 3, 4, 3, 5]

# Empty list to store result
unique = []

# Remove duplicates while keeping order
for num in nums:
    if num not in unique:
        unique.append(num)

# Output result
print("List without duplicates:", unique)

#output
#List without duplicates: [1, 2, 3, 4, 5]
