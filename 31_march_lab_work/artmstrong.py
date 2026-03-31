# Input number
n = int(input("Enter a number: "))

# Store original number
original = n

# Count number of digits
num_digits = len(str(n))

# Initialize sum
total = 0

# Calculate sum of powers of digits
while n > 0:
    digit = n % 10
    total += digit ** num_digits
    n //= 10

# Check Armstrong
if total == original:
    print(True)
else:
    print(False)

#output
#Enter a number: 153
#True
