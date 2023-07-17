while True:
    # Prompt the user to enter the phone number
    phoneNum = input("ENTER THE NUMBER IN THIS FORMAT XXX-XXX-XXXX: ")
    
    # Initialize a new string to store the converted phone number
    new_phone_num = ""
    
    # Iterate over each character in the input phone number
    for character in phoneNum:
        # Convert letters to digits according to the phone keypad
        if character.upper() == 'A' or character.upper() == 'B' or character.upper() == 'C':
            character = '2'
        elif character.upper() == 'D' or character.upper() == 'E' or character.upper() == 'F':
            character = '3'
        elif character.upper() == 'G' or character.upper() == 'H' or character.upper() == 'I':
            character = '4'
        elif character.upper() == 'J' or character.upper() == 'K' or character.upper() == 'L':
            character = '5'
        elif character.upper() == 'M' or character.upper() == 'N' or character.upper() == 'O':
            character = '6'
        elif character.upper() == 'P' or character.upper() == 'Q' or character.upper() == 'R' or character.upper() == 'S':
            character = '7'
        elif character.upper() == 'T' or character.upper() == 'U' or character.upper() == 'V':
            character = '8'
        elif character.upper() == 'W' or character.upper() == 'X' or character.upper() == 'Y' or character.upper() == 'Z':
            character = '9'
        
        # Append the converted character to the new phone number
        new_phone_num += character
    
    # Print the converted phone number
    print('EQUIVALENT PHONE NUMBER WOULD BE:', new_phone_num)

    # Ask the user if they want to continue or exit the program
    if input("WOULD YOU LIKE TO PROCEED? YES 'Y' OR NO 'N'").upper() == "N":
        break
