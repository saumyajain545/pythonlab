# Read an integer from standard input
num = int(input("Enter a number: "))

# Using bitwise AND to check even or odd
# If last bit is 0 → even, if last bit is 1 → odd
if num & 1 == 0:
    print("Even")
else:
    print("Odd")

#output
#Enter a number: 14
#Even
