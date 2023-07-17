# Python program to concatenate two strings character by character if their lengths are equal.

string1 = input("Enter the 1st string: ")  # Prompt the user to enter the first string
string2 = input("Enter the 2nd string: ")  # Prompt the user to enter the second string
new = ""  # Initialize an empty string to store the concatenated result

if len(string1) == len(string2):  # Check if the lengths of the strings are equal
    for i in range(0, len(string1)):  # Iterate over the indices of either string
        new += string1[i]  # Append the character from string1 to the new string
        new += string2[i]  # Append the character from string2 to the new string
    print(new)  # Print the concatenated string
else:
    print("Sorry! The length of the strings does not match.")  # Print an error message if the lengths don't match
