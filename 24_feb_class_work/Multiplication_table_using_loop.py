# Read the number for which the multiplication table is required
num = int(input("Enter a number: "))

# Initialize counter
i = 1

# Print multiplication table using while loop
while i <= 10:
    print(num, "x", i, "=", num * i)
    i = i + 1    # Increment the counter

#output
#Enter a number: 5
#5 x 1 = 5
#5 x 2 = 10
#5 x 3 = 15
#5 x 4 = 20
#5 x 5 = 25
#5 x 6 = 30
#5 x 7 = 35
#5 x 8 = 40
#5 x 9 = 45
#5 x 10 = 50
