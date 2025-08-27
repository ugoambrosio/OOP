# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


print('welcome')
name = str(input('Write your name\n'))
wage = int(input('Enter your wage\n'))
hour = int(input('Enter how many hours you work per day\n'))
days = int(input('Enter how many days work per week\n'))

total = wage*hour*days
print(name,'your salary is:',total)
