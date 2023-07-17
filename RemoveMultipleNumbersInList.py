numbers = [1, 2, 3, 4, 2, 5, 6, 2, 4]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)


