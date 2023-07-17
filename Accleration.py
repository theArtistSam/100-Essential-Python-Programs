# Python program to calcuate accleration

v1 = eval(input("Enter the value of velocity 1: "))  # Prompt the user to enter the value of velocity 1 and store it in v1
v2 = eval(input("Enter the value of velocity 2: "))  # Prompt the user to enter the value of velocity 2 and store it in v2
t = eval(input("Enter the value of time: "))  # Prompt the user to enter the value of time and store it in t

acceleration = (v2**2 - v1**2) / t  # Calculate the acceleration using the given formula

print(acceleration)  # Print the calculated acceleration
