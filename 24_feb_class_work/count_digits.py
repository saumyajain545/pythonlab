# Read an integer from standard input
num = int(input("Enter a number: "))

# Variable to store count of digits
count = 0

# Store original number for display
temp = num

# If the number is 0, it has one digit
if num == 0:
    count = 1
else:
    # Loop to count digits
    while num > 0:
        count = count + 1     # Increase digit count
        num = num // 10       # Remove last digit

# Print the total number of digits
print("Number of digits in", temp, "is:", count)

#output
#Enter a number: 75843
#Number of digits in 75843 is: 5
