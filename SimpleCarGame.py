# Python program to make a Simple Car Game

count = 0
Started = False

# Iterate three times to get user input
while count < 3:
    string = input(">")  # Prompt the user for input
    count += 1

    if string.upper() == "START":
        if Started:
            print("Car has already started")
        else:
            Started = True
            print("Car Started ... Ready to go!")
    elif string.upper() == "STOP":
        if not Started:
            print("The car is already stopped")
        else:
            Started = False
            print("Car stopped")
    elif string.upper() == "QUIT":
        print("Quit")
    else:
        print("I don't understand that!")

