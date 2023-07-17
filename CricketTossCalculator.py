# Toss (Heads and Tails) in Python

import random

# Generate a random number between 0 and 1 (0 represents heads, 1 represents tails)
num = random.randint(0, 1)
print(num)

# Prompt the user to enter their guess (0 or 1)
guess = eval(input("Enter your guess number (0 or 1): "))

# Check if the guess matches the generated number and print the result
if num == 0 and guess == 0:
    print("The coin is heads and you guessed right")
elif num == 1 and guess == 1:
    print("The coin is tails and you guessed right")
else:
    print("Your guess is wrong")
