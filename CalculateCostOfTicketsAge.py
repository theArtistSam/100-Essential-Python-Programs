# Python program to calculate the total cost for a group based on the ages of the guests.
print('Enter ages of the guests')
print('Enter a blank line to indicate the end')

total = 0
a = ''

while True:
    a = input()
    
    # Break the loop if the input is a blank line
    if a == '':
        break
    
    age = int(a)
    
    if age <= 2:
        total = total + 0
    elif age >= 3 and age <= 12:
        total = total + 14
    elif age >= 65:
        total = total + 18
    else:
        total = total + 23

print("The cost for the group is %.2f" % total)
