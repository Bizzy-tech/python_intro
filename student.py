from datetime import date, datetime


class Student :
    def __init__(self,DOB , name,gender):
        self.name = name
        self.DOB = DOB
        self.gender = gender


    def calculate_age(self):
        birth_date =datetime.strptime(self.DOB,'%d/%m/%Y')
        today = date.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age
