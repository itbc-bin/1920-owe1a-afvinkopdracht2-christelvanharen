# Christel van Haren, geschreven op 14-9-2019.
# Boek opdracht 2 'Sales Prediction', bladzijde 127.
# This program gets an item's original price and
# calculates its sale price, with a 23% discount.

# Get the item's orignal price.
original_price = float(input("Enter the item's original price: "))

# Calculate the amount of the discount.
discount = original_price * 0.23

# Calculate the sale price.
sale_price = original_price - discount

# Display the sale price.
print("The sale price is", sale_price)
