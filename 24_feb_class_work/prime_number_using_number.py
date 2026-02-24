# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Read a number from standard input
n = int(input("Enter a number: "))

# Call the function and print result
if is_prime(n):
    print(n, "is a Prime number")
else:
    print(n, "is Not a Prime number")

#output
#Enter a number: 17
#17 is a Prime number
