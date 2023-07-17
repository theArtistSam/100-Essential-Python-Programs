tax = eval(input("Enter the value of Tax"))
if tax>15000 and tax<60000:
    print("Pay Indivisual Tax")
if tax<=15000:
    print("Pay Student Tax")
if tax>60000:
    print("Pay Bussiness Tax")