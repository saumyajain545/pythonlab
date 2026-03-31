# Input list
numbers = [12, 35, 1, 10, 34, 1]

# Assume first value as largest
largest = numbers[0]
second_largest = numbers[0]

# Find the largest element
for num in numbers:
    if num > largest:
        largest = num

# Find the second largest element
for num in numbers:
    # Check number is not equal to largest and is greater than second_largest
    if num != largest and num > second_largest:
        second_largest = num

# Print result
print("Second largest element is:", second_largest)

#output
#Second largest element is: 34
