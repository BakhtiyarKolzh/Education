import logging

logger = logging.getLogger(__name__)


class Student:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.experience = 0

    def print_student(self):
        print(f"A student with name {self.name} of age {self.age}")

    def grow(self):
        self.age += 1

    def work(self, hours: int):
        self.experience += hours

    def __repr__(self):
        return f"A student with name {self.name} of age {self.age} has experience {self.experience}"


students: list[Student] = list()

students.append(Student(name="Bill", age=18))
students.append(Student(name="Volodya", age=50))

for student in students:
    for i in range(5):
        student.work(10)

print(students)
