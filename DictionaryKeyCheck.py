# Define a dictionary
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# Define a function to check key presence in the dictionary
def is_key_present(x):
    if x in d:
        print('Key is present in the dictionary')
    else:
        print('Key is not present in the dictionary')

# Call the function to check key presence
is_key_present(5)
is_key_present(9)

print("\n")
