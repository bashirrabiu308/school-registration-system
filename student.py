from utils import generate_reg_number
from storage import read_students, write_students

def register_student():
    name = input("Enter full name: ")
    password = input("Enter password (min 6 characters): ")
    level = input("Enter level: ")
    faculty = input("Enter faculty: ")
    department = input("Enter department: ")
    year = input("Enter year of admission (e.g., 2024): ")

    if len(password) < 6:
        print("Password too short. Must be at least 6 characters.")
        return

    students = read_students()
    serial = len(students) + 1

    reg_number = generate_reg_number(faculty, department, year, serial)

    student = {
        "name": name,
        "password": password,
        "level": level,
        "faculty": faculty,
        "department": department,
        "year": year,
        "reg_number": reg_number
    }

    students.append(student)
    write_students(students)

    print(f"\nStudent registered successfully!")
    print(f"Your Registration Number: {reg_number}\n")

def view_profile(reg_number):
    students = read_students()
    for s in students:
        if s['reg_number'] == reg_number:
            print("\n--- STUDENT PROFILE ---")
            print(f"Name: {s['name']}")
            print(f"Reg Number: {s['reg_number']}")
            print(f"Faculty: {s['faculty']}")
            print(f"Department: {s['department']}")
            print(f"Level: {s['level']}")
            print(f"Year: {s['year']}\n")
            return
    print("Profile not found.")
