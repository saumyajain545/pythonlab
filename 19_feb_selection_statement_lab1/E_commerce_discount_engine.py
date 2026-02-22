cart_value = float(input("Enter cart value: "))
membership = input("Enter membership (Silver/Gold/Platinum): ").lower()
festival = input("Is it festival season? (yes/no): ").lower()

discount = 0

if membership == "silver":
    discount = 5
elif membership == "gold":
    discount = 10
elif membership == "platinum":
    discount = 15

if festival == "yes":
    discount = max(discount, 20)

final_amount = cart_value - (cart_value * discount / 100)
print("Final payable amount: ₹", final_amount)

#output
#Enter cart value: 1000
#Enter membership (Silver/Gold/Platinum): gold
#Is it festival season? (yes/no): yes
#Final payable amount: ₹ 800.0
