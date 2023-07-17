# # Python program to calculate Right triangular pattern


# Iterate over the range from 1 to 7 (exclusive) with a step of 1
for i in range(1, 7, 1):
    num = 6
    # Iterate over the range from 6 to 0 (exclusive) with a step of -1
    for j in range(6, 0, -1):
        # Check if the current value of j is greater than i
        if j > i:
            # Print a space to maintain the triangular shape
            print(" ", end=' ')
        else:
            # Print the current value of num and decrement it by 1
            print(num, end=' ')
            num = num - 1
    # Print a new line to move to the next row
    print("")
