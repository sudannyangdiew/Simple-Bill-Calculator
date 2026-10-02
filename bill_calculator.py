# Simple Bill Calculator Program

# Ask the user for the price of an item and convert the input to a float
price = float(input("Enter the price of one item: "))

# Ask the user for the quantity they want and convert the input to an integer
quantity = int(input("Enter the quantity: "))

# Calculate the total cost
total = price * quantity

# Print a friendly summary using an f-string formatted to two decimal places
print(f"\n{quantity} items at {price:.2f} each = {total:.2f}")