
# Python Project [A Shopping Store]

# Welcome message
print("HEY!")
print("WELCOME TO OUR CLOTHING STORE")
print("PLEASE SIGNUP YOUR ACCOUNT FOR FURTHER PROCESSING")

# User selection
admin_customer = input("Are you an admin or customer? (Enter 'admin' or 'customer'): ")

# Admin flow
if admin_customer.lower() == "admin":
    admin_name = "Admin"
    admin_password = "1234"
    name = input("Enter your name: ")
    password = input("Enter your password: ")

    if name.lower() == admin_name and password.lower() == admin_password:
        print("HEY USER, YOU ARE WELCOME!")
        print("YOU CAN MODIFY INFORMATION")
        print("U have given items of retail in stock")
        print('''  
              a = "lwan pure duppata"
              b = "lwan sheffon duppataa"
              c = "lawn chicken kari"
              d = "digital print lawn 3p"
              e = "Bonenza"
              f = "Zara suiting"
              g = "Rana arts"
              h = "Gul Ahmad arts"
              i = "Grace suiting"
              j = "cotton plane"
              k = "designing cotton"
              l = "matching cotton"
              ''')
        print("U have wholesale items at this time")
        print('''
              W1 = ["lwan pure duppata"]
              W2 = ["lwan sheffon duppataa"]
              W3 = ["lawn chicken kari"]
              W4 = ["digital print lawn 3p"]
              W5 = ["Grace suiting"]
              W6 = ["cotton plane"]
              W7 = ["designing cotton"]
              W8 = ["matching cotton"]
              ''')
        exit()

# Customer flow
elif admin_customer.lower() == "customer":
    print("Dear respectful user, you are welcome to AHSAN FASHION.COM")
    account_check = input("Do you already have an account? (Enter 'Y' for Yes or 'N' for No): ")
    customer_name = input("Enter your username: ")
    customer_password = input("Enter your password: ")
    
    user_name = '';
    user_password = ''
    if account_check.upper() == "N":
        print("Signup successful!")
        print("Enter your credentials to login to AHSAN FASHION.COM")
        user_name = input("Enter your username: ")
        user_password = input("Enter your password: ")

        if user_name.lower() == customer_name and user_password.lower() == customer_password:
            print("YOUR LOGIN IS SUCCESSFUL")
        else:
            print("Login failed, try with correct credentials")

    elif account_check.upper() == "Y":
        if user_name.lower() == customer_name and user_password.lower() == customer_password:
            print("YOUR LOGIN IS SUCCESSFUL")
        else:
            print("Login failed, try with correct credentials")

# Retail and wholesale items code
print("WELCOME TO OUR ONLINE STORE")
print("PLEASE SELECT YOUR CATEGORY")
print("(Wholesale items) OR (Retail items)")

while True:
    choice = input("Enter your choice: ")

    if choice.lower() == "retail items":
        print("Here is the list of retail items, please select your desired category:")
        print('''
              S1 = ["lwan pure duppata", "lwan sheffon duppataa", "lawn chicken kari", "digital print lawn 3p"]
              S2 = ["Bonenza", "Zara suiting", "Rana arts", "Gul Ahmad arts"]
              S3 = ["Grace suiting", "cotton plane", "designing cotton", "matching cotton"]
              ''')
        category = input("Enter the category name: ")

        if category.upper() == "S1":
            print(list(enumerate(S1)))
        elif category.upper() == "S2":
            print(list(enumerate(S2)))
        elif category.upper() == "S3":
            print(list(enumerate(S3)))
        else:
            print("Invalid category")

        user_choice = input("Enter the number according to your desired item: ")

        if user_choice in globals():
            print("Here is your desired item:")
            print(globals()[user_choice])
            print("Price is Rs.", globals()[user_choice])
        else:
            print("Invalid item choice")

    elif choice.lower() == "wholesale items":
        print("Here are the wholesale items:")
        print('''
              W1 = "lwan pure duppata"
              W2 = "lwan sheffon duppataa"
              W3 = "lawn chicken kari"
              W4 = "digital print lawn 3p"
              W5 = "Grace suiting"
              W6 = "cotton plane"
              W7 = "designing cotton"
              W8 = "matching cotton"
              ''')
        wholesaler_choice = input("Enter the number according to your desired category: ")

        if wholesaler_choice in globals():
            print("Here is your desired item:", globals()[wholesaler_choice])
            print("Price is Rs. ", globals()[wholesaler_choice])
        else:
            print("Invalid category")

    else:
        print("Invalid choice")

    other_purchase = input("Would you like to purchase more stuff? (Enter 'yes' to continue or 'no' to quit): ")

    if other_purchase.lower() == "no":
        break

print("Here is the receipt of your purchase")
receipt = {
    "a": "lwan pure duppata\nPrice is Rs. 2000",
    "b": "lwan sheffon duppataa\nPrice is Rs. 1800",
    "c": "lawn chicken kari\nPrice is Rs. 3500",
    "d": "digital print lawn 3p\nPrice is Rs. 1500",
    "e": "Bonenza\nPrice is Rs. 3500",
    "f": "Zara suiting\nPrice is Rs. 4500",
    "g": "Rana arts\nPrice is Rs. 6000",
    "h": "Gul Ahmad arts\nPrice is Rs. 2500",
    "i": "Grace suiting\nPrice is Rs. 2000",
    "j": "cotton plane\nPrice is Rs. 2000",
    "k": "designing cotton\nPrice is Rs. 2800",
    "l": "matching cotton\nPrice is Rs. 1800",
    "W1": "lwan pure duppata\nPrice is Rs. 1600",
    "W2": "lwan sheffon duppataa\nPrice is Rs. 800",
    "W3": "lawn chicken kari\nPrice is Rs. 2000",
    "W4": "digital print lawn 3p\nPrice is Rs. 1500",
    "W5": "Grace suiting\nPrice is Rs. 1500",
    "W6": "cotton plane\nPrice is Rs. 1100",
    "W7": "designing cotton\nPrice is Rs. 2200",
    "W8": "matching cotton\nPrice is Rs. 1500"
}

choice1 = input("Confirm your first purchase: ")
choice2 = input("Confirm your second purchase: ")
choice3 = input("Confirm your third purchase: ")
choice4 = input("Confirm your last purchase: ")

print("Here is your receipt:")
print("1 =", receipt.get(choice1))
print("2 =", receipt.get(choice2))
print("3 =", receipt.get(choice3))
print("4 =", receipt.get(choice4))

print("\nThanks for purchasing from Ahsan Fashion.com")

# Payment method
print("Select your payment method")
print("Which method suits you?")
print("1 = Jazz cash")
print("2 = Easy paisa")
print("3 = Bank account")
print("4 = Cash on delivery")

payment = eval(input("Enter the number accordingly: "))

if payment == 1:
    print("Here is the Jaz cash no: XXXXXXXXXXXX")
elif payment == 2:
    print("Here is the EasyPaisa no: XXXXXXXXXXXX")
elif payment == 3:
    print("Here is the Bank account no: 12345678")
elif payment == 4:
    print("Cash on delivery")

print("\n----------------------------------")
print("Thanks for visiting our website")
