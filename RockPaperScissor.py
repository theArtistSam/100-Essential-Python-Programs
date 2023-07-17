import random

# Generate a random number between 0 and 2
num = random.randint(0, 2)
print(num)

# Get user's guess
guess = eval(input("Enter your guess number between 0 and 2: "))

# Assign meanings to numbers: 0 - Scissor, 1 - Rock, 2 - Paper
# Compare the computer's choice (num) with the user's guess

# Cases when the computer chooses Scissor (num == 0)
if num == 0 and guess == 1:
    print("Scissor cannot cut the Rock. You won!")
elif num == 0 and guess == 2:
    print("Scissor can cut Paper. You lost!")
elif num == 0 and guess == 0:
    print("Same! Try again.")

# Cases when the computer chooses Rock (num == 1)
elif num == 1 and guess == 0:
    print("Rock can smash the Scissor. You lost!")
elif num == 1 and guess == 2:
    print("Paper can wrap Rock. You won!")
elif num == 1 and guess == 1:
    print("Same! Try again.")

# Cases when the computer chooses Paper (num == 2)
elif num == 2 and guess == 0:
    print("Scissor can cut Paper. You lost!")
elif num == 2 and guess == 1:
    print("Paper can wrap Rock. You lost!")
elif num == 2 and guess == 2:
    print("Same! Try again.")
