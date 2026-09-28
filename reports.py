import sqlite3

DATABASE_NAME = "student_performance.db"


def student_report():
    print("\n--- Student Report ---")

    student_id = input("Enter student ID: ")

    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    # Get student details
    cursor.execute("""
        SELECT name, class_name, section, semester
        FROM students
        WHERE student_id = ?
    """, (student_id,))

    student = cursor.fetchone()

    if not student:
        print("Student not found.")
        connection.close()
        return

    # Get attendance
    cursor.execute("""
        SELECT subject, total_classes, classes_attended
        FROM attendance
        WHERE student_id = ?
        ORDER BY subject
    """, (student_id,))

    attendance_records = cursor.fetchall()

    # Get performance
    cursor.execute("""
        SELECT subject, assignment_marks, internal_marks, exam_marks
        FROM performance
        WHERE student_id = ?
        ORDER BY subject
    """, (student_id,))

    performance_records = cursor.fetchall()

    connection.close()

    print("\n==============================================")
    print("                STUDENT REPORT")
    print("==============================================")

    print("\nStudent Details")
    print("----------------------------------------------")
    print(f"Student ID : {student_id}")
    print(f"Name       : {student[0]}")
    print(f"Class      : {student[1]}")
    print(f"Section    : {student[2]}")
    print(f"Semester   : {student[3]}")

    # Attendance report
    print("\nAttendance")
    print("----------------------------------------------")

    if attendance_records:
        total_classes = 0
        total_attended = 0

        print("Subject | Total | Attended | Percentage")
        print("-" * 50)

        for record in attendance_records:
            subject = record[0]
            total = record[1]
            attended = record[2]

            percentage = (attended / total) * 100

            total_classes += total
            total_attended += attended

            print(
                f"{subject} | "
                f"{total} | "
                f"{attended} | "
                f"{percentage:.2f}%"
            )

        overall_attendance = (
            total_attended / total_classes
        ) * 100

        print("-" * 50)
        print(f"Overall Attendance: {overall_attendance:.2f}%")

    else:
        print("No attendance records found.")

    # Performance report
    print("\nPerformance")
    print("----------------------------------------------")

    if performance_records:
        total_percentage = 0

        print("Subject | Assignment | Internal | Exam | Total")
        print("-" * 60)

        for record in performance_records:
            subject = record[0]
            assignment = record[1]
            internal = record[2]
            exam = record[3]

            total = assignment + internal + exam
            total_percentage += total

            print(
                f"{subject} | "
                f"{assignment:.2f} | "
                f"{internal:.2f} | "
                f"{exam:.2f} | "
                f"{total:.2f}"
            )

        average_performance = (
            total_percentage / len(performance_records)
        )

        print("-" * 60)
        print(f"Average Performance: {average_performance:.2f}%")

    else:
        print("No performance records found.")

    print("\n==============================================")
    print("              END OF REPORT")
    print("==============================================")