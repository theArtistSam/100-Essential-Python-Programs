# Python program to calculate the Body Mass Index 

# Prompt the user to enter weight in kilograms and height in feet
weight = eval(input("Enter the weight in kilograms: "))
height = eval(input("Enter the height in feet: "))

# Convert height from feet to meters
heightMeters = height * 0.3048

# Calculate the Body Mass Index (BMI) using the weight and converted height
BMI = weight / (heightMeters * heightMeters)

# Print the calculated BMI
print("The BMI is:", BMI)
