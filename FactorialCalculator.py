# Python program to calculate Factorial 

# Prompt the user to enter a number
num = eval(input("Enter the value of a number"))

# Initialize the factorial variable
factorial = 1

# Check if the number is 0
if num == 0:
    print("The factorial of 0 is 1")
else:
    # Calculate the factorial using a loop
    for i in range(1, num + 1):
        factorial = factorial * i

    # Print the result
    print("The factorial of", num, "is", factorial)
