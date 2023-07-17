tuition = 10000  # Initial tuition fee
years = 0
total = 10000  # Initial total fees

for years in range(0, 10 + 1):  # Loop for 10 years
    tuition = tuition * 1.05  # Increase the tuition fee by 5% each year
    while years < 4:  # Loop for the first 4 years
        total = tuition
        total += tuition
        years += 1

print("Tuition at the tenth year will be", tuition)
print("The total fees after 4 years is", total)
