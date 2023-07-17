temp = eval(input("Enter the temprature in fahrenheit"))
wind = eval(input("Enter wind speed in mph"))
if temp>= -58 and temp<= 41 and wind>=2:
    print("Wind Chill temprature is ", temp - (wind * 0.7))
else:
    print("Your input is false")