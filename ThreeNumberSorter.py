num1 = eval(input("Enter the first number"))
num2 = eval(input("Enter the second number"))
num3 = eval(input("Enter the third number"))
if num1<num2 and num1<num3:
    smallest = num1
elif num2<num1 and num2<num3:
    smallest = num2
elif num3<num1 and num3<num2:
    smallest = num3
if num1>num2 and num1>num3:
    largest = num1
elif num2>num1 and num2>num3:
    largest = num2
elif num3>num1 and num3>num2:
    largest = num3
middle = (num1+num2+num3)-largest-smallest
print(smallest, ",", middle, ",", largest)
