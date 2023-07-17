# Python Program that uses conditional statement

# Receive an input from the user
number = eval(input("Enter an integer: "))

# Check if the number is divisible by 2 and 3
if number % 2 and number % 3:
    print(number, "is divisible by 2 and 3")

# Check if the number is divisible by 2 or 3
if number % 2 == 0 or number % 3 == 0:
    print(number, "is divisible by 2 or 3")

# Check if the number is divisible by 2 or 3, but not both
if (number % 2 == 0 and number % 3 == 0) and not (number % 2 == 0 and number % 3 == 0):
    print(number, "is divisible by 2 or 3, but not both")
