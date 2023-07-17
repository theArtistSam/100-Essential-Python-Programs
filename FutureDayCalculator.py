# Print the mapping of day numbers to day names
print("Sunday is 0, Monday is 1, Tuesday is 2, Wednesday is 3, Thursday is 4, Friday is 5 and Saturday is 6")

# Get input for current day number and number of days to calculate the future day
num1 = eval(input("Enter today's day number (0-6): "))
num2 = eval(input("Enter the number of days after today: "))

# Calculate the future day number using modulo 7 to ensure it stays within the range of 0-6
future = (num1 + num2) % 7

# Determine the name of the current day based on the input
if num1 == 0:
    today = "Sunday"
elif num1 == 1:
    today = "Monday"
elif num1 == 2:
    today = "Tuesday"
elif num1 == 3:
    today = "Wednesday"
elif num1 == 4:
    today = "Thursday"
elif num1 == 5:
    today = "Friday"
elif num1 == 6:
    today = "Saturday"
else:
    print("Error")

# Determine the name of the future day based on the calculated future day number
if future == 0:
    future_day = "Sunday"
elif future == 1:
    future_day = "Monday"
elif future == 2:
    future_day = "Tuesday"
elif future == 3:
    future_day = "Wednesday"
elif future == 4:
    future_day = "Thursday"
elif future == 5:
    future_day = "Friday"
elif future == 6:
    future_day = "Saturday"
else:
    print("Error")

# Print the current day and the future day
print("Today is", today, "and the future day is", future_day)
