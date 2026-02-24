# Read a number from standard input
num = int(input("Enter a number: "))

# Store the original number
temp = num

# Find the number of digits
digits = len(str(num))

# Variable to store sum of powers of digits
sum_armstrong = 0

# Check Armstrong condition using while loop
while num > 0:
    digit = num % 10                 # Extract last digit
    sum_armstrong += digit ** digits # Raise digit to power of digits
    num = num // 10                  # Remove last digit

# Compare the sum with original number
if sum_armstrong == temp:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

#output
#Enter a number: 153
#Armstrong Number
