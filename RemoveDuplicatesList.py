# Remove duplicates from a list of numbers
numbers = [1, 2, 4, 5, 6, 7, 1, 2, 3, 4]
numbers.sort()  # Sort the numbers in ascending order
for num in numbers:
    if numbers.count(num) > 1:  # Check if the number has duplicates
        numbers.remove(num)  # Remove the duplicate number
    print(num, end=" ")  # Print the number

print("\n")

# Remove duplicates from a list of words
words = ["apple", "banana", "cake", "ice cream", "lemonade", "apple", "cake"]
words.sort()  # Sort the words alphabetically
for word in words:
    if words.count(word) > 1:  # Check if the word has duplicates
        words.remove(word)  # Remove the duplicate word
    print(word, end=" ")  # Print the word
print()
