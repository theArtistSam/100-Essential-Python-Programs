# Python Currency conversion Program

num = eval(input("Enter a number (0 or 1 to exchange currency)"))
Exchange_rate_DtoRMB = 6.81  # Exchange rate from USD to RMB
Exchange_rate_RMBtoD = 0.15  # Exchange rate from RMB to USD
money = eval(input("Enter the amount of money to be converted"))

if num == 0:
    # Convert from USD to RMB
    print("RMB", money * Exchange_rate_DtoRMB)
elif num == 1:
    # Convert from RMB to USD
    print("$", Exchange_rate_RMBtoD * money)
