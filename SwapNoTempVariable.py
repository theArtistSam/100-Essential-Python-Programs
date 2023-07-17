# Prompt the user to enter the value of x
x = eval(input("Enter the value of X: "))

# Prompt the user to enter the value of y
y = eval(input("Enter the value of Y: "))

# Swap the values of x and y using a temporary variable
# Add the values of x and y and assign the result to x
x = x + y

# Subtract the original value of y from the new value of x and assign the result to y
y = x - y

# Subtract the original value of x from the new value of x and assign the result to x
x = x - y

# Print the updated values of x and y
print(x)
print(y)
