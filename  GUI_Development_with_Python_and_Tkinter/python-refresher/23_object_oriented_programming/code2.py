class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)

student = Student("Bob", (90, 90, 93, 78, 90))
student2 = Student("Rolf", (60, 80, 93, 98, 90))

print(student.name)
print((student.grades))
print(Student.average(student))
print(student.average())
print(student2.average())
