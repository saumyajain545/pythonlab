# Program to read data from a file

file = open("sample.txt", "r")        # Open file in read mode
content = file.read()                 # Read file content
file.close()                          # Close file

print("File content:", content)       # Display file content

# Output Example
# File content: Hello Python
