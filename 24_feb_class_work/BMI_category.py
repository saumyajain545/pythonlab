# Read weight in kilograms from standard input
weight = float(input("Enter weight in kg: "))

# Read height in meters from standard input
height = float(input("Enter height in meters: "))

# Calculate BMI using the formula
bmi = weight / (height * height)

# Display BMI value
print("BMI:", round(bmi, 2))

# Determine BMI category
if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 25:
    print("Category: Normal")
elif bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obese")

#output
#Enter weight in kg: 60
#Enter height in meters: 1.65
#BMI: 22.04
#Category: Normal
