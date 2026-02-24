# Initialize sum variable
total = 0

# Loop to accept numbers until 0 is entered
while True:
    num = int(input("Enter a number (0 to stop): "))
    
    # If input is 0, break the loop
    if num == 0:
        break
    
    # Add the number to total sum
    total += num

# Print the total sum
print("Sum of entered numbers is:", total)

#output
#Enter a number (0 to stop): 5
#Enter a number (0 to stop): 10
#Enter a number (0 to stop): 7
#Enter a number (0 to stop): 0
#Sum of entered numbers is: 22
