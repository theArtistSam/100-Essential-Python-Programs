# A simple guess game in Python

import random

# Generate a random number between 0 and 100
num = random.randint(0, 100)

# Initialize the guess variable
guess = -1

# Start the guessing loop
while guess != num:
    guess = eval(input("Enter your guess: "))

    if guess == num:
        print("You guessed the right number, mate")
    elif guess > num:
        print("Your guess is high")
    else:
        print("Your guess is low")
