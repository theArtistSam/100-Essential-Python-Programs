# Python program to display largest number among three 

num1 = eval(input("Enter the first number"))
num2 = eval(input("Enter the second number"))
num3 = eval(input("Enter the third number"))

# Compare the numbers to find the largest
if num1 > num2 and num1 > num3:
    print("num1 is the largest")
if num2 > num1 and num2 > num3:
    print("num2 is the largest")
if num3 > num1 and num3 > num2:
    print("num3 is the largest")
