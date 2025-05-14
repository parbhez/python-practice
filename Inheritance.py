#parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def showInfo(self):
        return f"Student name:{self.name}, Age:{self.age}"
    
#child class
class Student(Person): ## Inheriting from Person
    def __init__(self, name, age, school):
        super().__init__(name, age) #calling parent class constructor
        self.school = school

    def showStudentInfo(self):
        return f"{self.showInfo()}, His School name was: {self.school}"


#Child class
class Employee(Person):
    def __init__(self, name, age, company): #Inheriting from Person
        super().__init__(name, age) #calling from parent class constructor
        self.company = company

    
    def showEmployeeInfo(self):
        return f"{self.showInfo()}, His company name is : {self.company}"



if __name__ == "__main__":
    s1 = Student("Jony", 20, "ABC School")
    e1 = Employee("Jony", 27, "DevsZone")


    print(s1.showStudentInfo())
    print(e1.showEmployeeInfo())