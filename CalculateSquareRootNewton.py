# Python program that calculates the square root of a number using the Newton's method and generates combinations of pairs from a list of integers.

def sq(n):
    # Function to calculate the square root using the Newton's method

    lastGuess = 1
    nextGuess = (lastGuess + (n / lastGuess)) / 2

    # Loop until the difference between nextGuess and lastGuess is less than 0.0001
    while abs(nextGuess - lastGuess) < 0.0001:
        lastGuess = nextGuess
        nextGuess = (lastGuess + (n / lastGuess)) / 2

    return nextGuess


def main():
    # Main function to get input and call the sq function

    value = eval(input('Enter the number you want to get the square root of: '))
    print('The approximate square root of', value, 'is', sq(value))


# Call the main function
main()

# Get input for a list of 10 integers separated by commas
numbers = list(eval(input('Enter 10 integers separated by commas: ')))

# Create a list of all combinations of pairs where the first number is less than the second number
combinations = [[x, y] for x in numbers for y in numbers if x < y]

print('All Combinations are: ')
for pairs in combinations:
    # Print each pair of numbers
    print(pairs[0], ',', pairs[1], sep='')
