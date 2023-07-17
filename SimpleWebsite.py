users = [
    {
        "fname": "Usman",
        "lname": "Rehman",
        "email": "usman@outlook.com",
        "password": "usman"
    },
    {
        "fname": "Ali",
        "lname": "Rehman",
        "email": "ali@outlook.com",
        "password": "outlook"
    },
]

print("\n", "Welcome to our website","\n", "Do you already have an account?")

# Collect user information for sign up
fname = str(input("Enter your first name"))
lname = str(input("Enter your last name"))
username = str(input("Enter your username"))
email = str(input("Enter your email address"))
password_1 = str(input("Enter password"))
password_2 = str(input("Confirm password"))

print("Would you like to sign in")

def signin():
    # Collect username and password for sign in
    username = str(input("Enter your username"))
    password = str(input("Enter your password"))
    print("Please Sign In")
    # Add the user to the users list
    users.append({
        "fname": fname,
        "lname": lname,
        "email": email,
        "password": password
    })
    print(users)


def signup():
    check_3 = str(input(" Press Y for YES and N for NO"))
    if check_3.upper() == "Y":
        if password_1 == password_2:
            # Add the user to the users list
            users.append({
                "fname": fname,
                "lname": lname,
                "email": email,
                "password": password_2
            })
            print(users)
        else:
            print("Type the right password")
    else:
        exit()


def exit():
    # Exit the program
    exit()

def main():
    check = str(input(" Press Y for YES and N for NO"))
    if check.upper() == "Y":
        signin()
    elif check.upper() == "N":
        signup()
    else:
        print("Would you like to exit the website")
        check_2 = str(input("Press Y for YES and N for NO"))
        if check.upper() == "Y":
            exit()

main()
