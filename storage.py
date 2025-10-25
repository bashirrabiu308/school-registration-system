import csv
import os

FILE_NAME = "students.csv"

def read_students():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)

def write_students(students):
    with open(FILE_NAME, "w", newline="") as file:
        fieldnames = ["name", "password", "level", "faculty", "department", "year", "reg_number"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)
