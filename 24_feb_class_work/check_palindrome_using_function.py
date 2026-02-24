# Function to check if a string is a palindrome
def is_palindrome(s):
    # Compare original string with its reverse
    return s == s[::-1]

# Read a string from standard input
string = input("Enter a string: ")

# Call the function and print the result
if is_palindrome(string):
    print(string, "is a Palindrome")
else:
    print(string, "is Not a Palindrome")

#output
#Enter a string: madam
#madam is a Palindrome
