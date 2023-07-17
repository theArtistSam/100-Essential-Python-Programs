name = str(input("Enter your name"))
age = eval(input("Enter your Age"))
nationality = str(input("Enter your nationality"))
print("*****Welcome to Bus Station Website*****")
print()
total_seats = 20
yes = "Y"
no = "N"
for times in range(3):
    print("[Press Y for seat reservation] \n[Press N to go back to the main page]")
    reservation = str.upper(input("Y/N"))
    print("Total seats are: ",total_seats)
    if reservation == yes:
        seats = int(input("Enter the number of seats you want to get reserved"))
        if seats > total_seats:
            print("Sir! The bus doesn't contain that much of seats")
        elif seats < total_seats:
            print(seats, "seats have been booked for: ","\nMr./Mrs.: ",name,"\nAge: ",age,"\nNationality: ",nationality)
            print("Thanks for your reservation")
            rem_seats = total_seats - seats
            break

    elif reservation == no:
        print()
        print("*****Going back to main page*****")