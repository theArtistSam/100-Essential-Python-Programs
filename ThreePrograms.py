number = eval(input("Enter any four digit number"))
reverse = 0
while number > 0:
    rem = number % 10
    reverse = reverse * 10 + rem
    number = number // 10
print(reverse)


reversedNumber = []

def reverse(number):
    n = 0
    while number > 10:

        reverse = number % 10
        reversedNumber.append(reverse)
        number //= 10
        print(reverse, end= '')
    print(number)

def main():

    number = eval(input("Enter a number: "))
    reverse(number)

main()


def displaySortedNumbers(num1, num2, num3):
    print(max(num1, num2, num3), end=", ")

    if num1 != (max(num1, num2, num3) and min(num1, num2, num3)):
        print(num1, end=", ")

    elif num2 != (max(num1, num2, num3) and min(num1, num2, num3)):
        print(num2, end=", ")

    elif num3 != (max(num1, num2, num3) and min(num1, num2, num3)):
        print(num3, end=", ")

    print(min(num1, num2, num3))


def main():
    num1, num2, num3 = eval(input("Enter three numbers seprated by a comma: "))
    displaySortedNumbers(num1, num2, num3)


main()