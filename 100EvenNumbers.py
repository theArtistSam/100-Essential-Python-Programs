# Write a python program to print 100 Even numbers
num = 100

# Iterate over numbers from 1 to num (inclusive)
for i in range(1, num + 1):
    # Check if the number is divisible by 2 (i.e., even)
    if (i % 2) == 0:
        # Print the even number
        print(i)
