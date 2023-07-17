# Receive the number of students as input
numberOfStudents = eval(input("Enter the number of students: "))

# Initialize the counter for number of scores
numberOfScores = 0

# Create an empty list to store the scores
scores = []

# Loop to input the scores for each student
while numberOfScores < numberOfStudents:
    score = eval(input("\nEnter the student scores: "))
    scores.append(score)
    numberOfScores += 1

# Print the maximum score
print("\nThe maximum score is " + str(max(scores)))

# Remove the last entered score from the list
scores.pop(numberOfStudents - 1)

# Print the second highest score
print("\nThe second highest is " + str(max(scores)))
