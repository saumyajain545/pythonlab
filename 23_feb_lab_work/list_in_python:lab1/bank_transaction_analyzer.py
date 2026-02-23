# List of transactions (+ deposit, - withdrawal)
transactions = [10000, -5000, 20000, -3000]

# Calculate total balance
balance = sum(transactions)

# Find largest withdrawal
largest_withdrawal = min(transactions)

# Count deposits greater than 10000
count = 0
for t in transactions:
    if t > 10000:
        count += 1

# Display results
print("Balance:", balance)
print("Largest Withdrawal:", largest_withdrawal)
print("Deposits > 10000:", count)

#output
#Balance: 22000
#Largest Withdrawal: -5000
#Deposits > 10000: 1
