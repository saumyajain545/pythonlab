# Read an integer from standard input
num = int(input("Enter a number: "))

# Variable to store sum of digits
sum_digits = 0

# Loop until the number becomes 0
while num > 0:
    # Get the last digit of the number
    digit = num % 10

    # Add the digit to sum
    sum_digits = sum_digits + digit

    # Remove the last digit from the number
    num = num // 10

# Print the sum of digits
print("Sum of digits:", sum_digits)


#output
#Enter a number: 1234
#Sum of digits: 10
