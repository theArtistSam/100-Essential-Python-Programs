# Python Cashier Program


# Receive the amount
amount = eval(input("Enter an amount, for example, 11.56: "))

# Convert the amount to cents
cents = int(amount * 100)

# Find the number of one dollars        #Cents
numberOfOneDollars = cents // 100
cents = cents % 100

# Display the amount of cents(Code given down there)

# Find the number of quarters in the remaining amount
numberOfQuarters = cents // 25
cents = cents % 25

# Find the number of dimes in the remaining amount
numberOfDimes = cents // 10
cents = cents % 10

# Find the number of nickels in the remaining amount
numberOfNickels = cents // 5
cents = cents % 5

# Find the number of pennies in the remaining amount
numberOfPennies = cents

# Display the results
print("Your amount", amount, "consists of\n",
"\t", numberOfOneDollars, "dollars\n",
"\t", round(amount%1*100), "Cents\n"
"\t", numberOfQuarters, "quarters\n",
"\t", numberOfDimes, "dimes\n",
"\t", numberOfNickels, "nickels\n",
"\t", numberOfPennies, "pennies")