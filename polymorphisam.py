# ✅ Base Class
class Person:
    def show_profile(self):
        return "Generic Person Profile"


# ✅ Subclasses
class Student(Person):
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def show_profile(self):
        return f"Student Name: {self.name}, Grade: {self.grade}"


class Teacher(Person):
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def show_profile(self):
        return f"Teacher Name: {self.name}, Subject: {self.subject}"


class Staff(Person):
    def __init__(self, name, department):
        self.name = name
        self.department = department

    def show_profile(self):
        return f"Staff Name: {self.name}, Department: {self.department}"

def print_profile(person: Person):
    print(person.show_profile())


# ✅ Object গুলো তৈরি করছি
people = [
    Student("Masud", "Class 10"),
    Teacher("Rahim", "Physics"),
    Staff("Karim", "Admin")
]

# ✅ Polymorphic ভাবে ব্যবহার
for p in people:
    print_profile(p)
