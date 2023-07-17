# Solving a quadratic equation ax^2 + bx + c = 0
print("ax^2 + bx + c = 0 is a general quadratic equation.")
print("Enter the values of a, b, and c below.")

# Get input for a, b, and c
a = eval(input("Enter the value of a: "))
b = eval(input("Enter the value of b: "))
c = eval(input("Enter the value of c: "))

# Calculate the discriminant
discriminant = b**2 - 4*a*c

# Check the number of roots based on the discriminant
if discriminant > 0:
    print("The equation has two distinct real roots.")
    print("Discriminant:", discriminant)
elif discriminant == 0:
    print("The equation has one real root.")
    print("Discriminant:", discriminant)
else:
    print("The equation has no real roots.")
    print("Discriminant:", discriminant)
