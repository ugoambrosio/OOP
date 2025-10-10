from ridimit import Course


class Book_class:
    def __init__(self):
        self.book_id = ''
        self.book_title = ''
        self.author_id = ''
        self.publisher = ''
        self.year_of_publication = ''
    def addabook(self):
        self.book_id = input('Write the book ID\n')
        self.book_title = input('Write the book title\n')
        self.author_id = input('Write the author ID\n')
        self.publisher = input('Write the publisher\n')
        self.year_of_publication = input('Write the year of publication')
class Author_class:
    def __init__(self):
        self.author_id = ''
        self.author_name = ''
        self.affiliation = ''
        self.country = ''
        self.phone = ''
        self.email = ''
    def addanauthor(self):
        self.author_id = input('Write the author ID\n')
        self.author_name = input('Write the author name\n')
        self.affiliation = input('Write the affiliation\n')
        self.country = input('Write the country\n')
        self.phone = input('Write the phone\n')
        self.email = input('Write email\n')
class User_class:
    def __init__(self):
        self.user_id = ''
        self.name = ''
        self.address = ''
        self.phone = ''
        self.emailed = ''
        self.booksborrowed = []
    def addauser(self):
        self.user_id = input('Write the user ID\n')
        self.name = input('Write the name\n')
        self.address = input('Write the address\n')
        self.phone = input('Write the phone\n')
        self.emailed = input('Write the email\n')
        borrowedbok = input('Write the books borrowed\n')
        self.booksborrowed.append(borrowedbok)

    def booksborrowuser(bb1):
        print('Write the book you want to borrow')
        booksborrowed.append(bb1)


#maincode
def display():
    print(Book_class)
    print(Author_class)
    print(User_class)
lop = 2
boks = []
authors = []
ucers = []

while lop == 2:
    print('1. Create objects')
    print('2. Display classes')
    print('3. Borrow books')
    menu1 = int(input())
    if menu1 == 1:
        print('Choose an option to create object for a class')
        print('1. Book Class')
        print('2. Author Class')
        print('3. User Class')
        menu2 = int(input())
        if menu2 == 1:
            bok = Book_class()
            bok.addabook()
            boks.append(bok)
        if menu2 == 2:
            ator = Author_class()
            ator.addanauthor()
            authors.append(ator)
        if menu2 == 3:
            userob = User_class()
            userob.addauser()
            ucers.append(userob)
    elif menu1 == 2:
        print('Want to display the classes?')
        print('Y for yes N for no')
        menu = input()
        if menu == 'Y':
            display()
        elif menu == 'N':
            print('Chao')
            lop = 1
        else:
            print('Otra cosa')
    elif menu1 == 3:
            booksborrowuser()






