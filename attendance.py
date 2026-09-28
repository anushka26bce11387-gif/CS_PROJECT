import sqlite3
from validation import validate_attendance

DATABASE_NAME = "student_performance.db"


def add_attendance():
    print("\n--- Add Attendance ---")

    student_id = input("Enter student ID: ")

    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    # Check whether the student exists
    cursor.execute("""
        SELECT student_id
        FROM students
        WHERE student_id = ?
    """, (student_id,))

    student = cursor.fetchone()

    if student is None:
        print("Student ID does not exist.")
        connection.close()
        return

    subject = input("Enter subject: ").strip()
    total_classes = input("Enter total classes: ")
    classes_attended = input("Enter classes attended: ")

    if not subject:
        print("Subject cannot be empty.")
        connection.close()
        return

    if not validate_attendance(total_classes, classes_attended):
        print(
            "Invalid attendance. "
            "Total classes must be greater than 0, "
            "and attended classes cannot exceed total classes."
        )
        connection.close()
        return

    student_id = int(student_id)
    total_classes = int(total_classes)
    classes_attended = int(classes_attended)

    # Check whether attendance for this subject already exists
    cursor.execute("""
        SELECT attendance_id, total_classes, classes_attended
        FROM attendance
        WHERE student_id = ?
        AND LOWER(subject) = LOWER(?)
    """, (student_id, subject))

    existing_record = cursor.fetchone()

    if existing_record:
        attendance_id = existing_record[0]
        old_total = existing_record[1]
        old_attended = existing_record[2]

        new_total = old_total + total_classes
        new_attended = old_attended + classes_attended

        cursor.execute("""
            UPDATE attendance
            SET total_classes = ?,
                classes_attended = ?
            WHERE attendance_id = ?
        """, (
            new_total,
            new_attended,
            attendance_id
        ))

        connection.commit()
        connection.close()

        print("Attendance record updated successfully!")

    else:
        cursor.execute("""
            INSERT INTO attendance (
                student_id,
                subject,
                total_classes,
                classes_attended
            )
            VALUES (?, ?, ?, ?)
        """, (
            student_id,
            subject,
            total_classes,
            classes_attended
        ))

        connection.commit()
        connection.close()

        print("Attendance added successfully!")

        
def view_attendance():
    print("\n--- All Attendance Records ---")

    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            attendance.attendance_id,
            attendance.student_id,
            students.name,
            attendance.subject,
            attendance.total_classes,
            attendance.classes_attended
        FROM attendance
        JOIN students
        ON attendance.student_id = students.student_id
        ORDER BY attendance.student_id, attendance.subject
    """)

    records = cursor.fetchall()
    connection.close()

    if not records:
        print("No attendance records found.")
        return

    print("\nID | Student ID | Name | Subject | Total | Attended")
    print("-" * 65)

    for record in records:
        print(
            f"{record[0]} | "
            f"{record[1]} | "
            f"{record[2]} | "
            f"{record[3]} | "
            f"{record[4]} | "
            f"{record[5]}"
        )


def calculate_attendance_percentage():
    print("\n--- Attendance Percentage ---")

    student_id = input("Enter student ID: ")

    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            subject,
            total_classes,
            classes_attended
        FROM attendance
        WHERE student_id = ?
    """, (student_id,))

    records = cursor.fetchall()
    connection.close()

    if not records:
        print("No attendance records found for this student.")
        return

    print("\nSubject | Attendance Percentage")
    print("-" * 40)

    for record in records:
        subject = record[0]
        total_classes = record[1]
        classes_attended = record[2]

        if total_classes == 0:
            percentage = 0
        else:
            percentage = (classes_attended / total_classes) * 100

        print(f"{subject} | {percentage:.2f}%")