# Define the capitalize function
def captalize(word):
    # Use the title() method to capitalize the word
    output = word.title()
    # Print the capitalized word
    print(output)

# Define the main function
def main():
    # Prompt the user to enter a word or sentence
    word = input("Enter any sentence or word: ")
    # Call the capitalize function with the input word
    captalize(word)

# Call the main function to start the program
main()
