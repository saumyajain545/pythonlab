# Find out area and perimeter of circle

r = float(input("Enter the radius of the circle: "))

if (r <= 0):
    print("It is invalid radius")
    exit()
else:
    area = 3.14 * r * r
    print("The area is:", area)

    perimeter = 2 * 3.14 * r
    print("The perimeter is:", perimeter)
