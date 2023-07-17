# Python program to check if a number is +ve, -ve or 0


# Receive the number as input
num = eval(input("Enter a number: "))

# Check the sign of the number and print the corresponding message
if num == 0:
    print("Number is zero")
if num < 0:
    print("Number is negative")
if num > 0:
    print("Number is positive")
