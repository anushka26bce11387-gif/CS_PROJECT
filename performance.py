import sqlite3
from validation import validate_marks

DATABASE_NAME = "student_performance.db"


def add_performance():
    print("\n--- Add Performance ---")

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
    assignment_marks = input("Enter assignment marks: ")
    internal_marks = input("Enter internal marks: ")
    exam_marks = input("Enter exam marks: ")

    if not subject:
        print("Subject cannot be empty.")
        connection.close()
        return

    if not validate_marks(assignment_marks):
        print("Invalid assignment marks. Enter a value between 0 and 100.")
        connection.close()
        return

    if not validate_marks(internal_marks):
        print("Invalid internal marks. Enter a value between 0 and 100.")
        connection.close()
        return

    if not validate_marks(exam_marks):
        print("Invalid exam marks. Enter a value between 0 and 100.")
        connection.close()
        return

    student_id = int(student_id)
    assignment_marks = float(assignment_marks)
    internal_marks = float(internal_marks)
    exam_marks = float(exam_marks)

    # Check whether performance for this subject already exists
    cursor.execute("""
        SELECT performance_id
        FROM performance
        WHERE student_id = ?
        AND LOWER(subject) = LOWER(?)
    """, (student_id, subject))

    existing_record = cursor.fetchone()

    if existing_record:
        performance_id = existing_record[0]

        cursor.execute("""
            UPDATE performance
            SET assignment_marks = ?,
                internal_marks = ?,
                exam_marks = ?
            WHERE performance_id = ?
        """, (
            assignment_marks,
            internal_marks,
            exam_marks,
            performance_id
        ))

        connection.commit()
        connection.close()

        print("Performance record updated successfully!")

    else:
        cursor.execute("""
            INSERT INTO performance (
                student_id,
                subject,
                assignment_marks,
                internal_marks,
                exam_marks
            )
            VALUES (?, ?, ?, ?, ?)
        """, (
            student_id,
            subject,
            assignment_marks,
            internal_marks,
            exam_marks
        ))

        connection.commit()
        connection.close()

        print("Performance record added successfully!")


def view_performance():
    print("\n--- All Performance Records ---")

    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            performance.performance_id,
            performance.student_id,
            students.name,
            performance.subject,
            performance.assignment_marks,
            performance.internal_marks,
            performance.exam_marks
        FROM performance
        JOIN students
        ON performance.student_id = students.student_id
        ORDER BY performance.student_id, performance.subject
    """)

    records = cursor.fetchall()
    connection.close()

    if not records:
        print("No performance records found.")
        return

    print("\nID | Student ID | Name | Subject | Assignment | Internal | Exam")
    print("-" * 75)

    for record in records:
        print(
            f"{record[0]} | "
            f"{record[1]} | "
            f"{record[2]} | "
            f"{record[3]} | "
            f"{record[4]} | "
            f"{record[5]} | "
            f"{record[6]}"
        )


def calculate_performance_percentage():
    print("\n--- Performance Percentage ---")

    student_id = input("Enter student ID: ")

    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            subject,
            assignment_marks,
            internal_marks,
            exam_marks
        FROM performance
        WHERE student_id = ?
    """, (student_id,))

    records = cursor.fetchall()
    connection.close()

    if not records:
        print("No performance records found for this student.")
        return

    print("\nSubject | Total Marks | Percentage")
    print("-" * 45)

    for record in records:
        subject = record[0]
        assignment_marks = record[1]
        internal_marks = record[2]
        exam_marks = record[3]

        total_marks = (
            assignment_marks
            + internal_marks
            + exam_marks
        )

        percentage = total_marks

        print(
            f"{subject} | "
            f"{total_marks:.2f} | "
            f"{percentage:.2f}%"
        )