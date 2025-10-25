from storage import read_students, write_students
from student import view_profile

# Simple hardcoded admin account
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

def admin_login():
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")

    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        print("\nAdmin login successful!\n")
        return True
    else:
        print("Invalid admin credentials.\n")
        return False

def student_login():
    reg_number = input("Enter registration number: ")
    password = input("Enter password: ")

    students = read_students()
    for s in students:
        if s['reg_number'] == reg_number and s['password'] == password:
            print(f"\nWelcome, {s['name']}!")
            view_profile(reg_number)
            return s  # Return student data after successful login
    print("Invalid login credentials.\n")
    return None

def update_password(student):
    students = read_students()
    for s in students:
        if s['reg_number'] == student['reg_number']:
            new_password = input("Enter new password: ")
            if len(new_password) < 6:
                print("Password too short.")
                return
            s['password'] = new_password
            write_students(students)
            print("Password updated successfully!\n")
            return
