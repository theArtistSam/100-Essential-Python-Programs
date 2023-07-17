# Receive a list of prices as input
prices = list(map(int, input("Enter price of different products in cart: ").split()))

# Initialize the sum variable
sum = 0

# Iterate over each price and add it to the sum
for price in prices:
    sum += price

# Print the total sum of items in the cart
print("The total sum of items in the cart is:", sum)
