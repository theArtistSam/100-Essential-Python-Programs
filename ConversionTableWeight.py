# Conversion Table KG into Pounds

kilogram = 1
pound = 20

# Print the table header
print("Kilogram", "\t     ", "Pounds", "\t","|","      ","Pounds","\t    ","Kilograms")

# Calculate and print the conversion table
while kilogram in range(1, 200) or pound in range(20, 520):
    pounds = kilogram * 2.2
    kilograms = pound / 2.2
    print(str(format(kilogram, "<4.0f")) + str(format(pounds, "20.1f"))
          + " \t |"
          + str(format(pound, "10.0f")) + str(format(kilograms, "20.1f")))

    kilogram += 2
    pound += 5
