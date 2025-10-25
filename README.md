```markdown
# 🏫 School Registration System

A **console-based Python application** that manages student registration, account creation, and administrative operations for a school environment.  
This project allows **students** to register, view profiles, and manage passwords — while **admins** can view, search, delete, and reset student accounts.

---

## 🚀 Features

### 🎓 Student Features
- **Create Account:** Register by providing name, faculty, department, level, and admission year.
- **Auto-Generated Registration Number:** Automatically generated from faculty and department initials (excluding words like *of* and *and*).  
  Example:  
```

Faculty of Computing → fcp
Department of Cyber Security → ccs
Registration No: fcp/ccs/25/0001

```
- **View Profile:** Displays full student information and registration number.
- **Update Password:** Securely change or reset your password.
- **Login System:** Students must log in before accessing their dashboard.

### 🧑‍💼 Admin Features
- **Login System:** Admins log in separately to manage students.
- **View All Students:** Display a list of all registered students.
- **Search Student:** Search by name or registration number.
- **Delete Student:** Remove a student record from the system.
- **Reset Password:** Manually reset a student’s password.

---

## 🔐 Default Login Details

### 👨‍💼 Admin Account
Use the following credentials to access the admin dashboard:

```

Username: admin
Password: admin123

```

> 🔒 Tip: You can modify these credentials in the `auth.py` file for security purposes.

---

## 🛠️ Technical Details

- **Language:** Python 3
- **Architecture:** Modular (split into multiple files for clarity)
- **Data Storage:** CSV file (`students.csv`) for persistent storage
- **Modules:**
  - `main.py` → Entry point for the application
  - `student.py` → Handles student operations
  - `admin.py` → Handles admin features
  - `auth.py` → Manages authentication (login and password)
  - `storage.py` → Reads/writes data to files

---

## 📂 Project Structure

```

SchoolRegistrationSystem/
│
├── main.py           # Main entry point and menu navigation
├── student.py        # Student features (register, view, update)
├── admin.py          # Admin features (view, search, delete, reset)
├── auth.py           # Authentication system for login
├── storage.py        # File handling (save/load data)
├── students.csv      # Data storage file
└── README.md         # Project documentation

````

---

## ⚙️ Installation & Usage

1. **Clone the Repository**
   ```bash
   git clone https://github.com/bashirrabiu308/school-registration-system.git
   cd school-registration-system
````

2. **Run the Application**

   ```bash
   python main.py
   ```

3. **Follow On-Screen Instructions**

   * Choose **Student** or **Admin** login
   * Access respective menus and features

---

## 🧩 Example Output

```
=== School Registration System ===
1. Student Login
2. Admin Login
3. Exit

Enter choice: 1
Enter full name: Bashir Rabiu
Create password: ********
Enter faculty: Faculty of Computing
Enter department: Cyber Security
Enter level: 200
Enter admission year (e.g., 25): 25

Registration successful!
Your registration number: fcp/ccs/25/0001
```

---

## 🔒 Security Notes

* Passwords are stored in encrypted form (hashed).
* Invalid input is handled gracefully to avoid crashes.
* Faculty and department codes are auto-generated using smart string parsing.

---

## 👨‍💻 Author

**Bashir Rabiu**
🎓 Computer Science Student, University of Jos
💡 Passionate about Python, Web Development, and Data Science
📧 [Contact Me](mailto:bashirrabiu308@gmail.com)

---

## 🌟 Future Improvements

* Add GUI version using Tkinter or PyQt.
* Migrate storage to SQLite or MySQL.
* Include email verification system.
* Add export/import student data to Excel.

---

## 🪪 License

This project is open-source and available under the [MIT License](LICENSE).

```

