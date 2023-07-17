# Python program to Generate Random Character 
import random

num = random.randint(0, 127)  # Generate a random integer between 0 and 127 (inclusive) and store it in 'num'
print("The Character is", chr(num))  # Convert the integer to its corresponding ASCII character and print it
