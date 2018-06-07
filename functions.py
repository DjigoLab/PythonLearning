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

def save_into_file(student):
    try:
        f = open("./students.txt", "a")
        f.write(student + "\n")
        f.close()
    except Exception:
        print ("Can not save the file")

def read_file():
    try:
        f = open("students.txt", "r")
        for student in f.readlines():
            print (student)
        f.close()
    except Exception:
        print ("Can not read the file")

read_file()

while True:
    student_name = input("Enter student name, or say No to exit :")
    if student_name.lower() == "no":
        print("Bye!")
        break
    student_id = input("Enter student id: ")
    add_student(student_name, student_id)
    save_into_file(student_name)
