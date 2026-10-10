#old path: C:\Users\USER\Downloads\learn\projects\student-analytics api\sqlalchemy_test.py

from sqlalchemy import select
from sqlalchemy.orm import Session

from database import engine
from db_models import Student

with Session(engine) as session:
    students = session.scalars(select(Student)).all()
#    students = session.execute(select(Student))

    print(students[0].__dict__)

    for student in students:
        print(f"ID: {student.id}, \tName: {student.name}, \tBranch: {student.branch}, \tCGPA: {student.cgpa}")

#    student = Student(
#        id="26CS009", # also added 26CS007, 08
#        name="Test Student",
#        branch="CSE",
#        cgpa=8.75
#   )
#    session.add(student)
#
#
#    print("Before commit:")
#   print(student.__dict__)
#
#    session.commit()
#
#    print("After commit:")
#    print(student.__dict__)
#
#    student.cgpa = 9.00
#    session.commit()
