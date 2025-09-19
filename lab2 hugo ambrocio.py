mystudents = {
    '1':{
        'Name':'rodrigo',
        'Lab 1':52,
        'Lab 2': 75,
        'Lab 3': 86,
        'Lab 4': 75,
        'Lab 5': 100,
        'total': 388,
        'Percent':77.6,
        'Average':77.6
    },
    '2':{
        'Name': 'Chompipe',
        'Lab 1': 100,
        'Lab 2': 98,
        'Lab 3': 78,
        'Lab 4': 63,
        'Lab 5': 75,
        'Total': 414,
        'Percent':82.8,
        'Average':82.8

    },



}
numstudent = 2

lop = 3
while lop == 3:
    print('Welcome to students points')
    print('1. Add a student')
    print('2. Delete a student')
    print('3. Modify a student')
    print('4. Show students')
    print('5. Exit')
    menu = int(input('Choose an option\n'))
    if  menu == 1:
        name = input('Write the name of the student you want to add\n')
        lab1 = int(input('Write the points for the first lab\n'))
        lab2 = int(input('Write the points for the second lab\n'))
        lab3 = int(input('Write the points for the third lab\n'))
        lab4 = int(input('Write the points for the fourth lab\n'))
        lab5 = int(input('Write the points for the fifth lab\n'))
        numstudent = numstudent + 1
        mystudents.update({str(numstudent):{
        'Name': name,
        'Lab 1': lab1,
        'Lab 2': lab2,
        'Lab 3': lab3,
        'Lab 4': lab4,
        'Lab 5': lab5,
        'Total': lab1+lab2+lab3+lab4+lab5,
        'Percent': ((lab1+lab2+lab3+lab4+lab5)*100)/500,
        'Average': (lab1+lab2+lab3+lab4+lab5)/5
        }})

    elif menu == 2:
        delete = input('Write the number of the student you want to eliminate\n')
        found = False
        for i in mystudents:
            if delete == i:
                del mystudents[delete]
                print('Student removed')
                found = True
                break

            else:
                found = False
        if not found:
            print('Student not found')


    elif menu == 3:

        modify = input('Write the number of the student you want to modify\n')
        found = False
        for i in mystudents:
            if modify == i:
                name = input('Write the name of the student\n')
                lab1 = int(input('Write the points for the first lab\n'))
                lab2 = int(input('Write the points for the second lab\n'))
                lab3 = int(input('Write the points for the third lab\n'))
                lab4 = int(input('Write the points for the fourth lab\n'))
                lab5 = int(input('Write the points for the fifth lab\n'))

                mystudents.update({str(modify): {
                    'Name': name,
                    'Lab 1': lab1,
                    'Lab 2': lab2,
                    'Lab 3': lab3,
                    'Lab 4': lab4,
                    'Lab 5': lab5,
                    'Total': lab1 + lab2 + lab3 + lab4 + lab5,
                    'Percent': ((lab1 + lab2 + lab3 + lab4 + lab5) * 100) / 500,
                    'Average': (lab1 + lab2 + lab3 + lab4 + lab5) / 5
                }})
                print('Student modified')
                found = True
            else:
                found = False
        if not found:
            print('Student not found')




    elif menu == 4:
        print(mystudents)
    elif menu == 5:
        lop = 6