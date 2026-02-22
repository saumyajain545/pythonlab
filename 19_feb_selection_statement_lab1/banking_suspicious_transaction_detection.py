amount = float(input("Enter transaction amount: "))
account_months = int(input("Enter account age in months: "))
international = input("Is the transaction international? (yes/no): ").lower()

if amount > 200000 and account_months < 6 and international == "yes":
    print("Transaction flagged for manual verification.")
else:
    print("Transaction is safe.")

#output
#Enter transaction amount: 250000
#Enter account age in months: 3
#Is the transaction international? (yes/no): yes
#Transaction flagged for manual verification.
