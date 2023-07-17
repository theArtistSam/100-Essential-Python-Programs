# Python Program to Calcuate Result of Five Subjects

# Get the obtained marks of 5 subjects from the user
ObtainedMarks = eval(input("Enter obtained marks of 5 subjects"))

# Total marks for all subjects
TotalMarks = 500

# Calculate the percentage
Precentage = (ObtainedMarks / TotalMarks) * 100

# Check the division based on the percentage
if Precentage >= 60:
    print("First Division")
if Precentage >= 50 and Precentage <= 59:
    print("Second Division")
if Precentage >= 40 and Precentage <= 49:
    print("Third Division")
else:
    print("You failed miserably")
