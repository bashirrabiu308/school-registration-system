from storage import read_students, write_students

def view_all_students():
    students = read_students()
    if not students:
        print("No students registered yet.\n")
        return

    print("\n--- All Registered Students ---")
    for s in students:
        print(f"{s['name']} | {s['reg_number']} | {s['faculty']} | {s['department']}")
    print()

def search_student():
    students = read_students()
    keyword = input("Enter name or registration number: ").lower()
    found = [s for s in students if keyword in s['name'].lower() or keyword in s['reg_number'].lower()]

    if found:
        print("\n--- Search Results ---")
        for s in found:
            print(f"{s['name']} | {s['reg_number']} | {s['faculty']} | {s['department']}")
        print()
    else:
        print("Student not found.\n")

def delete_student():
    students = read_students()
    reg_number = input("Enter registration number to delete: ").lower()
    updated = [s for s in students if s['reg_number'].lower() != reg_number]

    if len(updated) == len(students):
        print("Student not found.\n")
    else:
        write_students(updated)
        print("Student deleted successfully.\n")

def reset_student_password():
    students = read_students()
    reg_number = input("Enter student registration number: ").lower()

    for s in students:
        if s['reg_number'].lower() == reg_number:
            new_password = input("Enter new password: ")
            s['password'] = new_password
            write_students(students)
            print("Password reset successfully.\n")
            return
    print("Student not found.\n")
