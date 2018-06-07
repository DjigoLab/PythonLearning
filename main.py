from hs_student import HighSchoolStudent
from student import Student
import functions

while True:
    student_name = input("Enter student name, or say No to exit :")
    if student_name.lower() == "no":
        print("Bye!")
        break
    student_id = input("Enter student id: ")
    student_type = input ("1)HighSchool or 2)Elementary?")
    if student_type == "1":
        tonio = HighSchoolStudent(student_name,student_id)
     #   functions.add_student(tonio.student_name, tonio.student_id, "HS")
    else:
        tonio = Student(student_name)
      #  functions.add_student(tonio.student_name, tonio.student_id, "EL")

    functions.save_into_file(student_name)

