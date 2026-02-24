# Read four numbers from standard input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

# Assume the first number is the greatest
greatest = a

# Compare with the second number
if b > greatest:
    greatest = b

# Compare with the third number
if c > greatest:
    greatest = c

# Compare with the fourth number
if d > greatest:
    greatest = d

# Print the greatest number
print("Greatest number is:", greatest)

#output
#Enter first number: 10
#Enter second number: 45
#Enter third number: 23
#Enter fourth number: 18
#Greatest number is: 45
