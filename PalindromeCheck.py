# Python program to check if a number is palindrome or not

# Receive input string
s = input("Enter a string:")
# Remove leading and trailing whitespace from the string
s = s.strip()

# Initialize low and high indices for comparison
low = 0
high = len(s) - 1

# Iterate until low is less than high
while low < high:
    # Print the current indices for debugging
    print(low, "    ", high)
    # Compare characters at low and high indices
    if s[low] == s[high]:
        # Move to the next pair of characters
        low += 1
        high -= 1
    else:
        # If characters don't match, print "Not Palindrome" and break the loop
        print("Not Palindrome")
        break

# Check if low is greater than or equal to high, indicating that all characters matched
if low >= high:
    print("Is Palindrome")
