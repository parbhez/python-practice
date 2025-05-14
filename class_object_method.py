class Student:
    def __init__(self, name, age, company):
        self.name = name
        self.age = age
        self.company = company

    def __str__(self):
        return f"Student Name:{self.name}, Age:{self.age}, company:{self.company}"
    
    def getStudentInfo(self, department):
        return f"My name is {self.name} and I am {self.age} years old. I work at {self.company} and I am in the {department} department."


s1 = Student('Nexus', 27, 'DevsZone')
print(s1.getStudentInfo('development'))
