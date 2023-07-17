# Python program to generate a right triangle pattern

# Initialize the value of i to 1
i = 1

# Iterate while i is less than 7
while i < 7:
    # Iterate over the range from 1 to i (exclusive) with a step of 1
    for j in range(1, i, 1):
        # Print the value of j followed by a space
        print(j, end=" ")
    
    # Print the value of i on a new line
    print(i)
    
    # Increment the value of i by 1
    i += 1
