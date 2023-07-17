# Python program to convert number into words

# Receive input numbers as a string
numbers = input("Enter numbers")

# Define a dictionary to map digits to word representations
define = {
    "1": 'one',
    "2": 'two',
    "3": 'three',
    "4": "Four"
}

# Initialize an empty string for the output
output = ""

# Iterate over each character in the input numbers
for character in numbers:
    # Get the word representation from the dictionary, or "N/A" if not found
    word = define.get(character, "N/A")
    # Append the word representation to the output string
    output += word + " "

# Print the final output
print(output)
