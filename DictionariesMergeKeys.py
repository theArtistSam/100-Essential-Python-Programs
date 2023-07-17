# Define two dictionaries
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
d3 = {}

# Merge the dictionaries by summing values for matching keys
for i, j in d1.items():
    for x, y in d2.items():
        if i == x:
            d3[i] = (j + y)

# Print the merged dictionary
print(d3)

print("\n")
