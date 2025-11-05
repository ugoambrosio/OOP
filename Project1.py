class account:
    def __init__(self):
        self.user_account = ''
        self.password_account = ''
        self.number_account = ''
        self.email_account = ''
        self.id_person = ''
        self.age_person = 0
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
class patient(account):
    def __init__(self):
        super().__init__()
        self.diagnosis_patient = ''
        self.medication_patient = ''
    def add_a_patient(self):
        account.add_an_account(self)
        self.diagnosis_patient = input('Write the diagnosis of the patient\n')
        self.medication_patient = input('Write the medication of the patient\n')
    def print_information_patient(self):
        pass

class doctor(account):
    def __init__(self):
        super().__init__()
        self.specialty_doctor = ''
        self.experience_doctor = ''
    def add_a_doctor(self):
        account.add_an_account(self)
        self.specialty_doctor = input('Write the specialty of the doctor\n')
        self.experience_doctor = input('Write the experience of the doctor\n')
    def print_information_doctor(self):
        account.print_user_information(self)
        print('Specialty: ', self.specialty_doctor)
        print('Experince: ',self.experience_doctor)
class nurse(account):
    def __init__(self):
        super().__init__()
        self.certificacions_nurse = ''
        self.specialty_nurse = ''
        self.experience_nurse = ''
    def add_a_nurse(self):
        account.add_an_account(self)
        self.certificacions_nurse = input('Write the certificacions of the nurse\n')
        self.specialty_nurse = input('Write the specialty of the nurse\n')
        self.experience_nurse = input('Write the experience of the nurse\n')
    def print_information_nurse(self):
        account.print_user_information(self)
        print('Certificacions: ',self.certificacions_nurse)
        print('Specialty: ',self.specialty_nurse)
        print('Experience: ',self.experience_nurse)
class administrative(account):
    def __init__(self):
        super().__init__()
        self.staff_administrative = ''
        self.schedule = ''
    def add_an_administrative(self):
        account.add_an_account(self)
        self.staff_administrative = input('Write the type of staff\n')
        self.schedule = input('Write the schedule\n')
    def print_information_administrative(self):
        account.print_user_information(self)
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

c1 = administrative()
c1.add_an_administrative()
c1.print_information_administrative()
