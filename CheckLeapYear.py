# Python program to check leap year

year = eval(input("Enter the year to check if it is leap or not"))

# Check if the year is a leap year
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Year is leap")
else:
    print("Year is not leap")
