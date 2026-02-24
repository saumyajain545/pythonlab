# Read an integer from standard input
num = int(input("Enter a number: "))

# Check if the number is divisible by both 3 and 5
if num % 3 == 0 and num % 5 == 0:
    print("The number is divisible by both 3 and 5")
else:
    print("The number is not divisible by both 3 and 5")

#output
#Enter a number: 30
#The number is divisible by both 3 and 5
