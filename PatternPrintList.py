# Python pattern printing program usnig lists. 
number = [2, 2, 2, 2, 2, 5]

# Iterate through each element in the list
for X in number:
    output = ""
    
    # Repeat 'X' based on the value of X
    for y in range(X):
        output += "X"
    
    # Print the generated output
    print(output)
