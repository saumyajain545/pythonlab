# Read an integer from standard input
num = int(input("Enter a number: "))

# Variable to store the reversed number
reverse = 0

# Loop until the number becomes 0
while num > 0:
    # Get the last digit of the number
    digit = num % 10

    # Add digit to the reversed number
    reverse = reverse * 10 + digit

    # Remove the last digit from the number
    num = num // 10

# Print the reversed number
print("Reversed number:", reverse)

#output
#Enter a number: 12345
#Reversed number: 54321
