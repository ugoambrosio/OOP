class account:
    def __init__(self):
        self.user_account = ''
        self.password_account = ''
        self.number_account = ''
        self.email_account = ''
        self.id_person = ''
        self.age_person = ''
        self.gender_person = ''
class patient:
    def __init__(self):
        self.diagnosis_patient = ''
class doctor:
    def __init__(self):
        self.specialty_doctor = ''
        self.experience_doctor = ''
class nurse:
    def __init__(self):
        self.certificacions_nurse = ''
        self.specialty_nurse = ''
        self.experience_nurse = ''
class administrative:
    def __init__(self):
        self.staff_administrative = ''
        self.schedule = ''
class hospital:
    def __init__(self):
        self.locations = ''
        self.size = ''
        self.trauma_level = ''
        self.specialized_equipment = ''
class billing:
    def __init__(self):
        self.billing_records = []