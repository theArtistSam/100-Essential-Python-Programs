# Import the random module
import random

# Generate a random number between 0 and 100
Random1 = random.randint(0, 100)
print(Random1)

# Generate another random number between 0 and 100
Random2 = random.randint(0, 100)
print(Random2)

# Calculate the sum of the two random numbers
Sum = Random1 + Random2

# Prompt the user to enter their guess for the sum
User_Guess = eval(input("Enter your guess of the sum of the two random numbers: "))

# Compare the user's guess with the actual sum and print the result
if Sum == User_Guess:
    print("Your answer is correct")
else:
    print("Your answer is false")
