# Write a python program to print 100 Odd numbers
num = 100

# Check if num is equal to 0
if num == 0:
    print("Wrong")
else:
    # Iterate over numbers from 1 to num (inclusive)
    # and print the odd numbers
    for i in range(1, num + 1):
        # Check if the number is not divisible by 2 (i.e., odd)
        if (i % 2) != 0:
            # Print the odd number
            print(i)
