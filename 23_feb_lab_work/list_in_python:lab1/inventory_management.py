# Stock quantities of products
stock = [0, 5, 12, 8, 0, 20]

# Remove items with zero stock
new_stock = []
for s in stock:
    if s != 0:
        new_stock.append(s)

# Add restock of 50 units to items below 10
for i in range(len(new_stock)):
    if new_stock[i] < 10:
        new_stock[i] += 50

# Display inventory details
print("Updated Stock:", new_stock)
print("Total Inventory:", sum(new_stock))

#output
#Updated Stock: [55, 12, 58, 20]
#Total Inventory: 145
