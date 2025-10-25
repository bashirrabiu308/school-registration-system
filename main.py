from auth import admin_login, student_login, update_password
from student import register_student
from admin import view_all_students, search_student, delete_student, reset_student_password

def admin_menu():
    while True:
        print("""
===== ADMIN MENU =====
1. View All Students
2. Search Student
3. Delete Student
4. Reset Student Password
5. Logout
""")
        choice = input("Enter choice: ")
        if choice == "1":
            view_all_students()
        elif choice == "2":
            search_student()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            reset_student_password()
        elif choice == "5":
            print("Logging out...\n")
            break
        else:
            print("Invalid choice.\n")

def student_menu(student):
    while True:
        print("""
===== STUDENT MENU =====
1. View Profile
2. Update Password
3. Logout
""")
        choice = input("Enter choice: ")
        if choice == "1":
            from student import view_profile
            view_profile(student["reg_number"])
        elif choice == "2":
            update_password(student)
        elif choice == "3":
            print("Logging out...\n")
            break
        else:
            print("Invalid choice.\n")

def main_menu():
    while True:
        print("""
===== SCHOOL REGISTRATION SYSTEM =====
1. Register Student
2. Admin Login
3. Student Login
4. Exit
""")
        choice = input("Enter choice: ")

        if choice == "1":
            register_student()
        elif choice == "2":
            if admin_login():
                admin_menu()
        elif choice == "3":
            student = student_login()
            if student:
                student_menu(student)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.\n")

if __name__ == "__main__":
    main_menu()
