# Python program to rotate list members

# Create a list of numbers from 0 to 9
list = [x for x in range(10)]

# Store the first element in a temporary variable
temp = list[0]

# Shift each element to the previous position
for i in range(1, len(list)):
    list[i - 1] = list[i]

# Assign the temporary variable to the last element
list[len(list) - 1] = temp

# Print the rotated list
print(list)
