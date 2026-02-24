# Program to check whether a key exists in a dictionary

student = {"name": "Rahul", "age": 20}     # Create dictionary

key = input("Enter key to check: ")        # Take key input from user

if key in student:                         # Check if key exists
    print("Key exists")                    # Print if found
else:                                      # Otherwise
    print("Key does not exist")            # Print if not found

# Output Example
# Enter key to check: age
# Key exists
