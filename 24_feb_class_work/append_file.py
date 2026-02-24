# Program to append data to a file

file = open("sample.txt", "a")        # Open file in append mode
file.write("\nWelcome")               # Append new line text
file.close()                          # Close file

print("Data appended successfully")   # Display success message

# Output Example
# Data appended successfully
