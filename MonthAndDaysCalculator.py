# Python prgram for month and days calculation

# Receive the month as input
month = eval(input("Enter your month from 1-12: "))

# Receive the year as input
year = eval(input("Enter your year: "))

# Check the month and year combination to determine the number of days
if month == 1:
    print("January", year, "has 31 days")
elif month == 2:
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print("February", year, "has 29 days")  # Leap year
    else:
        print("February", year, "has 28 days")  # Non-leap year
elif month == 3:
    print("March", year, "has 31 days")
elif month == 4:
    print("April", year, "has 30 days")
elif month == 5:
    print("May", year, "has 31 days")
elif month == 6:
    print("June", year, "has 30 days")
elif month == 7:
    print("July", year, "has 31 days")
elif month == 8:
    print("August", year, "has 31 days")
elif month == 9:
    print("September", year, "has 30 days")
elif month == 10:
    print("October", year, "has 31 days")
elif month == 11:
    print("November", year, "has 30 days")
elif month == 12:
    print("December", year, "has 31 days")
