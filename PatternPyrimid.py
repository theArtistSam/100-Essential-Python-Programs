# Prompt the user to enter a number
num = eval(input("Enter the number"))

# Outer loop for rows
for i in range(1, num+1):
    # Print spaces before the numbers
    for j in range(1, num-i+1):
        print(end=" ")

    # Print numbers in descending order
    for j in range(i, 0, -1):
        print(j, end="")

    # Print numbers in ascending order (excluding the first digit)
    for j in range(2, i+1):
        print(j, end="")

    # Move to the next line
    print()
