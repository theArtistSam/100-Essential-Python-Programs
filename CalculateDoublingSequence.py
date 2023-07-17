# Python program to calculate "doubling sequence"

add = eval(input("Enter a number: "))  # Prompt the user to enter a number and store it in the variable 'add'

for add in range(add, 11):  # Iterate over the range starting from the input number up to 10 (inclusive)
    print(add + add)  # Print the sum of 'add' and 'add', which is 'add' doubled
