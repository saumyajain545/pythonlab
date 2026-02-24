# Program to count number of lines in a file

file = open("sample.txt", "r")        # Open file in read mode
lines = file.readlines()              # Read all lines into list
file.close()                          # Close file

print("Total lines:", len(lines))     # Display number of lines

# Output Example
# Total lines: 2
