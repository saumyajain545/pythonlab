# Read the number from standard input
num = int(input("Enter the number: "))

# Read the lower limit of the range
lower = int(input("Enter the lower limit: "))

# Read the upper limit of the range
upper = int(input("Enter the upper limit: "))

# Check if the number lies within the given range (inclusive)
if lower <= num <= upper:
    print("The number lies within the range")
else:
    print("The number does not lie within the range")

#output
#Enter the number: 15
#Enter the lower limit: 10
#Enter the upper limit: 20
#The number lies within the range
