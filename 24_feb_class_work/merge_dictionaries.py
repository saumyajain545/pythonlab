# Program to merge two dictionaries

dict1 = {"a": 1, "b": 2}          # Create first dictionary
dict2 = {"c": 3, "d": 4}          # Create second dictionary

merged = dict1.copy()             # Create copy of first dictionary
merged.update(dict2)              # Add second dictionary items

print("Merged dictionary:", merged)  # Display merged dictionary

# Output Example
# Merged dictionary: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
