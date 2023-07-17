# Python program to calculate reversed triangular pattern

# Initialize the value of i to 6
i = 6

# Iterate while i is greater than 0
while i > 0:
    # Iterate over the range from 1 to i (exclusive) with a step of 1
    for j in range(1, i, 1):
        # Print the value of j followed by a space
        print(j, end=" ")
    
    # Print the value of i on a new line
    print(i)
    
    # Decrement the value of i by 1
    i -= 1
