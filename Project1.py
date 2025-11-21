import tkinter as tk
from tkinter import *
from tkinter import messagebox
#LOGIN-------------------------------------------------------------------------
class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        self.username_entry = tk.Entry(
            self.root,
            width=25,
        )
        self.username_entry.place(x=145, y=90)

        self.login_button = tk.Button()


        self.valid_username = "Admin"
        self.valid_password = "12345"


        label1 = Label(width=20, height=2, text='Username')
        label1.place(x=145, y=50)



        label2 = Label(width=20, height=2, text='Password')
        label2.place(x=145, y=140)


        self.error_label = tk.Label(
            self.root,
            text="Incorrect username or password",
            font=("Arial", 9),
            bg='#f0f0f0',
            fg='red'

        )
        self.password_entry = tk.Entry(
            self.root,
            width=20,
            show="*"

        )
        self.password_entry.place(x=145, y=180)
        self.password_entry.bind('<Return>', lambda event: self.login())
        login_button = tk.Button(
            self.root,
            text="Login",
            command=self.login,
            bg='#4CAF50',
            fg='white',
            font=("Arial", 10, "bold"),
            width=15,
            height=1,
            relief="flat",
            cursor="hand2"
        )
        login_button.place(x=140, y=230)
#Login------------------------------------------------------------------------------*-----------------
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        self.error_label.place_forget()

        if username == self.valid_username and password == self.valid_password:
            messagebox.showinfo("Login Successful", f"Welcome, {username}!")
            self.root.destroy()
            root_main = tk.Tk()
            app_main = Administration(root_main)
            root_main.mainloop()

        else:

            self.error_label.place(x=50, y=210)

            self.password_entry.delete(0, tk.END)
#ADMINISTRATION MENU----------------------------------------------------------------------------------------------------------------
class Administration:
    def __init__(self, root):
        self.root = root
        self.root.title("Main System")
        self.root.geometry("800x600")

        label = tk.Label(self.root, text="Administrative Menu", font=("Arial", 16))
        label.pack(pady=20)
        Schedule_button = tk.Button(
            self.root,
            text="Patients Schedule",
            command= self.patients_information,
            bg='#A15AA1',
            fg='white',
            font=("Arial", 10, "bold"),
            width=35,
            height=4,
            relief="flat",
            cursor="hand2"
        )
        Schedule_button.place(x=240, y=130)
        Billing_information = tk.Button(
            self.root,
            text="Billing information",
            command=self.billing_menu,
            bg='#4CAF50',
            fg='white',
            font=("Arial", 10, "bold"),
            width=35,
            height=4,
            relief="flat",
            cursor="hand2"
        )
        Billing_information.place(x=240, y=230)
        Accounts_information = tk.Button(
            self.root,
            text="Accounts Schedule",
            command=self.accounts_information,
            bg='#A15AA1',
            fg='white',
            font=("Arial", 10, "bold"),
            width=35,
            height=4,
            relief="flat",
            cursor="hand2"
        )
        Accounts_information.place(x=240, y=330)

    def patients_information(self):
        self.root.destroy()
        root_main = tk.Tk()
        app_main = Patients_information(root_main)
        root_main.mainloop()
    def accounts_information(self):
        self.root.destroy()
        root_main = tk.Tk()
        app_main = Accounts_information(root_main)
        root_main.mainloop()

    def billing_menu(self):
        self.root.destroy()
        root_main = tk.Tk()
        app_main = Billing(root_main)
        root_main.mainloop()

#PATIENTS MENU-----------------------------------------------------------------------------------------------------
class Patients_information:
    def __init__(self,root):
        self.root = root
        self.root.title("Patient System")
        self.root.geometry("800x600")

        label = tk.Label(self.root, text="Patients Information", font=("Arial", 16))
        label.pack(pady=20)

        Return_button = tk.Button(
            self.root,
            text="Return to menu",
            command= self.return_to_menu,
            bg='#A15AA1',
            fg='white',
            font=("Arial", 10, "bold"),
            width=35,
            height=4,
            relief="flat",
            cursor="hand2"
        )
        Return_button.place(x=240, y=330)

    def return_to_menu(self):
        self.root.destroy()
        root_main = tk.Tk()
        app_main = Administration(root_main)
        root_main.mainloop()


#BILLING MENU-------------------------------------------------------------------------------------------------------------
class Billing():
    def __init__(self,root):
        self.root = root
        self.root.title("Billing System")
        self.root.geometry("800x600")

        label = tk.Label(self.root, text="Billing Information", font=("Arial", 16))
        label.pack(pady=20)

        Return_button = tk.Button(
            self.root,
            text="Return to menu",
            command= self.return_to_menu,
            bg='#A15AA1',
            fg='white',
            font=("Arial", 10, "bold"),
            width=35,
            height=4,
            relief="flat",
            cursor="hand2"
        )
        Return_button.place(x=240, y=330)

    def return_to_menu(self):
        self.root.destroy()
        root_main = tk.Tk()
        app_main = Administration(root_main)
        root_main.mainloop()

#ACCOUNTS MENU------------------------------------------------------------------------------------------------
class Accounts_information():
    def __init__(self,root):
        self.root = root
        self.root.title("Accounts System")
        self.root.geometry("800x600")

        label = tk.Label(self.root, text="Accounts Information", font=("Arial", 16))
        label.pack(pady=20)

        Return_button = tk.Button(
            self.root,
            text="Return to menu",
            command= self.return_to_menu,
            bg='#A15AA1',
            fg='white',
            font=("Arial", 10, "bold"),
            width=35,
            height=4,
            relief="flat",
            cursor="hand2"
        )
        Return_button.place(x=240, y=330)

    def return_to_menu(self):
        self.root.destroy()
        root_main = tk.Tk()
        app_main = Administration(root_main)
        root_main.mainloop()

#CLASSES-------------------------------------------------------------------------------------------------
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
        print('Type: ',self.staff_administrative)
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
    def add_billing_record(self, billing_record):
        self.billing_records.append(billing_record)
#Main Code-----------------




if __name__ == "__main__":
    root = tk.Tk()
    app = Login(root)
    root.mainloop()

