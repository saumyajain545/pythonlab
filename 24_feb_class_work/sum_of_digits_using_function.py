# Function to calculate sum of digits of a number
def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10   # Add last digit to total
        n = n // 10       # Remove last digit
    return total

# Read a number from standard input
num = int(input("Enter a number: "))

# Call the function and print the sum of digits
print("Sum of digits of", num, "is:", sum_of_digits(num))

#output
#Enter a number: 12345
#Sum of digits of 12345 is: 15
