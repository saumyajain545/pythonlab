units = int(input("Enter units consumed: "))
senior = input("Is senior citizen? (yes/no): ").lower()

if units <= 100:
    bill = units * 5
elif units <= 300:
    bill = (100 * 5) + (units - 100) * 7
else:
    bill = (100 * 5) + (200 * 7) + (units - 300) * 10

if senior == "yes":
    bill *= 0.9

print("Total electricity bill: ₹", bill)
