import sqlite3

DATABASE_NAME = "student_performance.db"


def student_summary():
    print("\n--- Student Performance Summary ---")

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

    # Get attendance data
    cursor.execute("""
        SELECT
            SUM(total_classes),
            SUM(classes_attended)
        FROM attendance
        WHERE student_id = ?
    """, (student_id,))

    attendance = cursor.fetchone()

    # Get performance data
    cursor.execute("""
        SELECT
            AVG(assignment_marks + internal_marks + exam_marks)
        FROM performance
        WHERE student_id = ?
    """, (student_id,))

    performance = cursor.fetchone()

    connection.close()

    total_classes = attendance[0] or 0
    classes_attended = attendance[1] or 0
    average_marks = performance[0] or 0

    if total_classes > 0:
        attendance_percentage = (
            classes_attended / total_classes
        ) * 100
    else:
        attendance_percentage = 0

    print("\nStudent Details")
    print("-------------------------")
    print(f"Name       : {student[0]}")
    print(f"Class      : {student[1]}")
    print(f"Section    : {student[2]}")
    print(f"Semester   : {student[3]}")

    print("\nAnalytics")
    print("-------------------------")
    print(f"Attendance : {attendance_percentage:.2f}%")
    print(f"Avg Marks  : {average_marks:.2f}")

        # Determine student status
    if attendance_percentage >= 75 and average_marks >= 50:
        status = "Good"
    elif attendance_percentage >= 60 and average_marks >= 40:
        status = "Needs Improvement"
    else:
        status = "At Risk"

    print(f"Status     : {status}")


def class_summary():
    print("\n--- Class Analytics Summary ---")

    class_name = input("Enter class name: ").strip()

    if not class_name:
        print("Class name cannot be empty.")
        return

    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    # Get students in the selected class
    cursor.execute("""
        SELECT student_id, name
        FROM students
        WHERE LOWER(class_name) = LOWER(?)
        ORDER BY student_id
    """, (class_name,))

    students = cursor.fetchall()

    if not students:
        print("No students found in this class.")
        connection.close()
        return

    print("\n==============================================")
    print("             CLASS ANALYTICS")
    print("==============================================")

    print(f"\nClass: {class_name}")
    print(f"Total Students: {len(students)}")

    total_attendance = 0
    attendance_students = 0

    total_performance = 0
    performance_students = 0

    print("\nStudent Summary")
    print("----------------------------------------------")
    print("ID | Name | Attendance | Performance")
    print("-" * 50)

    for student in students:
        student_id = student[0]
        name = student[1]

        # Calculate attendance
        cursor.execute("""
            SELECT
                SUM(total_classes),
                SUM(classes_attended)
            FROM attendance
            WHERE student_id = ?
        """, (student_id,))

        attendance = cursor.fetchone()

        total_classes = attendance[0] or 0
        classes_attended = attendance[1] or 0

        if total_classes > 0:
            attendance_percentage = (
                classes_attended / total_classes
            ) * 100

            total_attendance += attendance_percentage
            attendance_students += 1
        else:
            attendance_percentage = 0

        # Calculate performance
        cursor.execute("""
            SELECT AVG(
                assignment_marks
                + internal_marks
                + exam_marks
            )
            FROM performance
            WHERE student_id = ?
        """, (student_id,))

        performance = cursor.fetchone()

        if performance[0] is not None:
            performance_percentage = performance[0]
            total_performance += performance_percentage
            performance_students += 1
        else:
            performance_percentage = 0

        print(
            f"{student_id} | "
            f"{name} | "
            f"{attendance_percentage:.2f}% | "
            f"{performance_percentage:.2f}%"
        )

    connection.close()

    print("\nClass Averages")
    print("----------------------------------------------")

    if attendance_students > 0:
        class_attendance = (
            total_attendance / attendance_students
        )
    else:
        class_attendance = 0

    if performance_students > 0:
        class_performance = (
            total_performance / performance_students
        )
    else:
        class_performance = 0

    print(f"Average Attendance : {class_attendance:.2f}%")
    print(f"Average Performance: {class_performance:.2f}%")

    print("==============================================")