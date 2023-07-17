# Python program to Check Divisibility

no_of_line = 0  # Counter for the number of lines printed

# Iterate through the range of numbers from 100 to 999
for num in range(100, 1000):
    # Check if the number is divisible by 5 or 6, but not both
    if num % 5 == 0 or num % 6 == 0 and not (num % 5 == 0 and num % 6 == 0):
        no_of_line += 1  # Increment the line counter

        # Print the number, followed by a space or a newline based on the line counter
        print(num, end=(" " if no_of_line < 10 else "\n"))

        # Reset the line counter if it reaches 10
        if no_of_line == 10:
            no_of_line = 0
