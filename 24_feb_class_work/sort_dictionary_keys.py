# Program to sort dictionary by keys

student = {"b": 2, "a": 1, "c": 3}    # Create dictionary

for key in sorted(student):           # Loop through sorted keys
    print(key, ":", student[key])     # Print sorted key-value pairs

# Output Example
# a : 1
# b : 2
# c : 3
