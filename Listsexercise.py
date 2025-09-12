print('Welcome')


lop = 0
mylist = []
while lop == 0:
    print('1. Add an element to the list')
    print('2. Remove an element from the list')
    print('3. Replace an element in the list')
    print('4. Sort the elements in the list')
    print('5. Reverse the elements in the list')
    print('6. Print the elements of the list')
    print('7. Exit')
    menu = int(input())

    if menu == 1:
        add = input('Write the element you want to add\n')
        mylist.append(add)
    elif menu == 2:
        remove = input('Write the element you want to remove\n')
        mylist.remove(remove)
    elif menu == 3:
        elereplace = int(input('Write the index of the element you want to remove\n'))
        newword = input('Write the new word you want to add\n')
        for i in range(0, len(mylist)):
            if elereplace == i:
                mylist[i] = newword
    elif menu == 4:
        men4 = int(input('Are you sure you want to sort the elements? (Type 1 for yes, 0 for no)\n'))
        if men4 == 1:
            mylist.sort()
        else:
            print('Returning to menu\n')
    elif menu == 5:
        men5 = int(input('Are you sure you want to reverse the elements? (Type 1 for yes, 0 for no)\n'))
        if men5 == 1:
            mylist.reverse()
        else:
            print('Returning to menu\n')
    elif menu == 6:
        for i in range(0,len(mylist)):
            print(mylist[i])
    elif menu == 7:
        lop = 4
    else:
        print('That is not an option')