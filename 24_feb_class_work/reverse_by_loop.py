# Read an integer from standard input
num = int(input("Enter a number: "))

# Variable to store the reversed number
reverse = 0

# Store original number for display
temp = num

# Reverse the number using while loop
while num > 0:
    digit = num % 10          # Get the last digit
    reverse = reverse * 10 + digit
    num = num // 10           # Remove the last digit

# Print the reversed number
print("Reversed number of", temp, "is:", reverse)

#output
#Enter a number: 1234
#Reversed number of 1234 is: 4321
