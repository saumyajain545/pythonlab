# Input list and target
nums = [1, 2, 3, 4, 5, 6]
target = 7

# Empty list to store pairs
pairs = []

# Find pairs
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            pairs.append((nums[i], nums[j]))

# Output result
print("Pairs with sum", target, ":", pairs)

#output
#Pairs with sum 7 : [(1, 6), (2, 5), (3, 4)]
