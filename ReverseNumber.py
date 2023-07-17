# Python program to reverse a four-digit number

# Receive input for the four-digit number
number = eval(input("Enter any four-digit number"))

# Initialize a variable to store the reversed number
reverse = 0

# Reverse the number using a while loop
while number > 0:
    # Extract the last digit of the number
    rem = number % 10
    
    # Build the reversed number by appending the last digit
    reverse = reverse * 10 + rem
    
    # Remove the last digit from the number
    number = number // 10

# Print the reversed number
print(reverse)
