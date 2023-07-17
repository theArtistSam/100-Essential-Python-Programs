# Python program to convert into Emoji

# Receive user input
message = input(">")

# Split the input into individual words
words = message.split(" ")

# Define a dictionary for emoticon replacements
define = {
    ":)": "😀",
    ":(": "😌",
    "<3": "❤",
}

# Initialize the output string
output = ""

# Iterate through each word in the input
for word in words:
    # Replace the word with its corresponding emoticon if available, otherwise keep the word as it is
    output += define.get(word, word) + " "

# Print the final output
print(output)