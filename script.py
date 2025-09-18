# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


print('Welcome to calculator')
lop = 1
while lop == 1:
    print('Select an operation')
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    print('5.Quit')
    menu = int(input('Enter your choice: '))
    if menu == 1:
        num1 = int(input('Enter first number: '))
        num2 = int(input('Enter second number: '))
        result = num1 + num2
        print(num1, '+', num2, '=', result)
    if menu == 2:
        num1 = int(input('Enter first number: '))
        num2 = int(input('Enter second number: '))
        result = num1 - num2
        print(num1, '-', num2, '=', result)
    if menu == 3:
        num1 = int(input('Enter first number: '))
        num2 = int(input('Enter second number: '))
        result = num1 * num2
        print(num1, '*', num2, '=', result)
    if menu == 4:
        num1 = int(input('Enter first number: '))
        num2 = int(input('Enter second number: '))
        result = num1 / num2
        print(num1, '/', num2, '=', result)
    if menu == 5:
        lop = 3

