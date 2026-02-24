# Read a string from standard input
string = input("Enter a string: ")

# Initialize an empty string to store the reversed string
reversed_string = ""

# Loop through the original string in reverse order
for i in range(len(string)-1, -1, -1):
    reversed_string += string[i]  # Add each character to reversed_string

# Print the reversed string
print("Reversed string:", reversed_string)

#output
#Enter a string: Hello
#Enter a string: Hello
