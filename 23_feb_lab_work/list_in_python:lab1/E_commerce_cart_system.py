# List of product prices in cart
cart = [1000, 2000, 1000, 3000]

# Remove duplicate items
unique_cart = []
for item in cart:
    if item not in unique_cart:
        unique_cart.append(item)

# Calculate total price
total = sum(unique_cart)

# Apply 10% discount if total > 5000
if total > 5000:
    total = total - total * 0.10

# Add 18% GST
total = total + total * 0.18

# Display final amount
print("Final Amount:", total)

#output
#Final Amount: 6372.0
