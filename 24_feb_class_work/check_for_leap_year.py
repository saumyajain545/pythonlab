# Read year from standard input
year = int(input("Enter a year: "))

# Check leap year conditions
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

#output
#Enter a year:2024
#Leap Year
