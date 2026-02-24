# Program to count characters in a string (excluding spaces)

text = input("Enter a string: ")         # Take string input from user

count = 0                                # Initialize character counter

for char in text:                        # Loop through each character
    if char != " ":                      # Check if character is not space
        count = count + 1                # Increase counter

print("Total characters (without spaces):", count)  # Display result

# Output Example
# Enter a string: Hello World
# Total characters (without spaces): 10
