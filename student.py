import sqlite3
from validation import validate_name, validate_positive_integer


DATABASE_NAME = "student_performance.db"


def add_student():
    print("\n--- Add New Student ---")

    name = input("Enter student name: ")
    class_name = input("Enter class: ")
    section = input("Enter section: ")
    semester = input("Enter semester: ")

    if not validate_name(name):
        print("Invalid name. Name cannot be empty.")
        return

    if not validate_name(class_name):
        print("Invalid class. Class cannot be empty.")
        return

    if not validate_name(section):
        print("Invalid section. Section cannot be empty.")
        return

    if not validate_positive_integer(semester):
        print("Invalid semester. Please enter a positive number.")
        return

    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO students (name, class_name, section, semester)
        VALUES (?, ?, ?, ?)
    """, (name, class_name, section, int(semester)))

    connection.commit()
    connection.close()

    print("Student added successfully!")
    

def view_students():
    print("\n--- All Students ---")

    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
                SELECT student_id, name, class_name, section, semester
                FROM students
                """)
    
    students = cursor.fetchall()
    
    connection.close()
    
    if not students:
        print("No students found.")
        return
    
    print("\nID | Name | Class | Section | Semester")
    print("-" * 50)
    
    for student in students:
        print(
               f"{student[0]} | "
               f"{student[1]} | "
               f"{student[2]} | "
               f"{student[3]} | "
               f"{student[4]}"
            )

def search_student():
    print("\n--- Search Student ---")

    student_id = input("Enter student ID: ")

    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()


    cursor.execute("""
        SELECT student_id, name, class_name, section, semester
        FROM students
        WHERE student_id = ?
    """, (student_id,))

    student = cursor.fetchone()

    connection.close()

    if student:
        print("\nStudent Found")
        print("-------------------------")
        print(f"Student ID : {student[0]}")
        print(f"Name       : {student[1]}")
        print(f"Class      : {student[2]}")
        print(f"Section    : {student[3]}")
        print(f"Semester   : {student[4]}")
    else:
        print("Student not found.")


def update_student():
    print("\n--- Update Student ---")
    
    student_id = input("Enter student ID to update: ")
    
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()
    
    # Check if student exists
    cursor.execute("""
        SELECT * FROM students
        WHERE student_id = ?
    """, (student_id,))

    student = cursor.fetchone()

    if not student:
        print("Student not found.")
        connection.close()
        return

    print("\nEnter new details:")

    name = input("Enter new name: ")
    class_name = input("Enter new class: ")
    section = input("Enter new section: ")
    semester = input("Enter new semester: ")

    cursor.execute("""
        UPDATE students
        SET name = ?, class_name = ?, section = ?, semester = ?
        WHERE student_id = ?
    """, (name, class_name, section, semester, student_id))

    connection.commit()
    connection.close()

    print("Student updated successfully!")


def delete_student():
    print("\n--- Delete Student ---")

    student_id = input("Enter student ID to delete: ")

    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    # Check if student exists
    cursor.execute("""
        SELECT name
        FROM students
        WHERE student_id = ?
    """, (student_id,))

    student = cursor.fetchone()

    if not student:
        print("Student not found.")
        connection.close()
        return

    confirm = input(
        f"Are you sure you want to delete {student[0]}? (yes/no): "
    )

    if confirm.lower() == "yes":
        cursor.execute("""
            DELETE FROM students
            WHERE student_id = ?
        """, (student_id,))

        connection.commit()
        print("Student deleted successfully!")
    else:
        print("Deletion cancelled.")

    connection.close()