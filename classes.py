students = []
class Student:

    def __init__(self, name, student_id = 0):
        self.name = name.capitalize()
        self.student_id = student_id
        students.append(self)
        print("Student {0} added".format(name))

    def __str__(self):
        return "Student: " + self.name +", ID:" + str(self.student_id)

tonio = Student("tonio")

print(tonio)
