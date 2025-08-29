from logging import exception
print('Welcome user')
course1 = int(input('Write the grade of your first class\n'))
course2 = int(input('Write the grade of your second class\n'))
course3 = int(input('Write the grade of your third class\n'))
course4 = int(input('Write the grade of your fourth class\n'))
course5 = int(input('Write the grade of your fifth class\n'))
total = course1 + course2 + course3 + course4 + course5
total_percentage = (total / 500)*100



if total_percentage > 89:
    print('Your grade is A', total_percentage)
elif total_percentage > 79 and total_percentage < 90:
    print('Your grade is B',total_percentage)
elif total_percentage > 69 and total_percentage < 80:
    print('Your grade is C',total_percentage)
elif total_percentage >59 and total_percentage < 70:
    print('Your grade is D',total_percentage)
else:
    print('Your grade is F',total_percentage)