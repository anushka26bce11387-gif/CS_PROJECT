from reports import student_report
from database import create_tables

from student import (
    add_student,
    search_student,
    update_student,
    delete_student
)

from attendance import (
    add_attendance,
    calculate_attendance_percentage
)

from performance import (
    add_performance,
    calculate_performance_percentage
)

from analytics import student_summary, class_summary


def main():
    create_tables()

    while True:
        print("\n==============================================")
        print(" Student Performance and Attendance Analytics")
        print("==============================================")
        print("A. Add Student")
        print("B. Search Student")
        print("C. Update Student")
        print("D. Delete Student")
        print("E. Add Attendance")
        print("F. Attendance Percentage")
        print("G. Add Performance")
        print("H. Performance Percentage")
        print("I. Student Analytics Summary")
        print("J. Student Report")
        print("K. Class Analytics Summary")
        print("X. Exit")
        print("==============================================")

        choice = input("Enter your choice: ").strip().upper()

        if choice == "A":
            add_student()

        elif choice == "B":
            search_student()

        elif choice == "C":
            update_student()

        elif choice == "D":
            delete_student()

        elif choice == "E":
            add_attendance()

        elif choice == "F":
            calculate_attendance_percentage()

        elif choice == "G":
            add_performance()

        elif choice == "H":
            calculate_performance_percentage()

        elif choice == "I":
            student_summary()

        elif choice == "J":
            student_report()

        elif choice == "K":
            class_summary()

        elif choice == "X":
            print("\nThank you for using the system!")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
    