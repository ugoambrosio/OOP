class account:
    def __init__(self):
        self.user_account = ''
        self.password_account = ''
        self.number_account = ''
        self.email_account = ''
        self.id_person = ''
        self.age_person = ''
        self.gender_person = ''
    def add_an_account(self):
        self.user_account = input("Write your name\n")
        self.password_account = input("Write your password\n")
        self.number_account = input("Write your phone number\n")
        self.email_account = input("Write your email\n")
        self.id_person = input("Write your ID\n")
        self.age_person = input("Write your age\n")
        self.gender_person = input('Write your gender\n')
    def print_user_information(self):
        print('Name: ',self.user_account)
        print('Number: ',self.number_account)
        print('Email: ',self.email_account)
        print('ID: ',self.id_person)
        print('Age: ',self.age_person)
        print('Gender: ',self.gender_person)
class patient:
    def __init__(self):
        self.diagnosis_patient = ''
    def add_a_patient(self):
        pass
    def print_information_patient(self):
        pass

class doctor:
    def __init__(self):
        self.specialty_doctor = ''
        self.experience_doctor = ''
    def print_information_doctor(self):
        pass
class nurse:
    def __init__(self):
        self.certificacions_nurse = ''
        self.specialty_nurse = ''
        self.experience_nurse = ''
    def print_information_nurse(self):
        pass
class administrative(account):
    def __init__(self):
        super().__init__()
        self.staff_administrative = ''
        self.schedule = ''
    def add_an_administrative(self):
        account.add_an_account()
        self.staff_administrative = input('Write the type of staff\n')
        self.schedule = input('Write the schedule\n')
    def print_information_administrative(self):
        account.print_user_information()
        print('Type shi: ',self.staff_administrative)
        print('Schedule: ',self.schedule)

class hospital:
    def __init__(self):
        self.locations = ''
        self.size = ''
        self.trauma_level = ''
        self.specialized_equipment = ''
class billing:
    def __init__(self):
        self.billing_records = []

c1 = account()
c1.add_an_account()