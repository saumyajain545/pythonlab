percentage = float(input("Enter 12th percentage: "))
maths = input("Studied Mathematics? (yes/no): ").lower()
entrance = int(input("Enter entrance exam score: "))

if percentage < 75:
    print("Rejected: Less than 75% in 12th.")
elif maths != "yes":
    print("Rejected: Mathematics not studied.")
elif entrance < 80:
    print("Rejected: Entrance score below 80.")
else:
    print("Eligible for admission.")
