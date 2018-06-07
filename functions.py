students = []

def add_student(name, student_id = 0):
    student = {"name" : name, "student_id" : student_id}
    students.append(student)
    print("Student {0} added".format(name))

def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase = student["name"].title()
    return students_titlecase

def print_students_titleclase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)   

student_name = input("Enter student name: ")
student_id = input("Enter student id: ")
add_student(student_name, student_id)
print_students_titleclase()