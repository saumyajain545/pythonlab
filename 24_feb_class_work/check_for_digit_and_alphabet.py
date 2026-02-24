# Read a character from standard input
ch = input("Enter a character: ")

# Check if the input is a single character
if len(ch) == 1:
    # Check if the character is an alphabet
    if ch.isalpha():
        print("Alphabet")
    # Check if the character is a digit
    elif ch.isdigit():
        print("Digit")
    else:
        print("Neither alphabet nor digit")
else:
    print("Invalid input")

#output
#Enter a character: A
#Alphabet
