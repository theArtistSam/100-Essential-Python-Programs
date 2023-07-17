# Python program to calcuate Distance between two points

import math

# Prompt the user to enter the coordinates
x1 = eval(input("Enter the x-coordinate of the first point: "))
x2 = eval(input("Enter the x-coordinate of the second point: "))
y1 = eval(input("Enter the y-coordinate of the first point: "))
y2 = eval(input("Enter the y-coordinate of the second point: "))

# Calculate the distance using the distance formula
Distance = (x2 - x1) ** 2 + (y2 - y1) ** 2

# Compute the square root of the distance to get the actual distance
print("The distance between the points is:", math.sqrt(Distance))
