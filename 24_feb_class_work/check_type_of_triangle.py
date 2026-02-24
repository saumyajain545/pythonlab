# Read the three sides of the triangle from standard input
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

# First check whether the sides can form a valid triangle
# Sum of any two sides must be greater than the third side
if a + b > c and a + c > b and b + c > a:
    
    # Check for Equilateral triangle
    if a == b == c:
        print("Equilateral Triangle")
    
    # Check for Isosceles triangle
    elif a == b or b == c or a == c:
        print("Isosceles Triangle")
    
    # Otherwise, it is a Scalene triangle
    else:
        print("Scalene Triangle")

# If sides do not form a valid triangle
else:
    print("Not a valid triangle")

#output
#Enter first side: 5
#Enter second side: 5
#Enter third side: 5
#Equilateral Triangle
