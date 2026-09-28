# Student Performance and Attendance Analytics System

## 1. Project Overview

The Student Performance and Attendance Analytics System is a Python-based application designed to manage student information, attendance records, academic performance, and analytics.

The system uses SQLite for data storage and provides a menu-driven interface through which users can add, search, update, and delete student records, manage attendance and performance data, generate analytics, and create student reports.

## 2. Problem Statement

Educational institutions need to maintain accurate student records and monitor attendance and academic performance regularly.

Managing these records manually can be time-consuming and may make it difficult to identify attendance problems or understand student performance.

This project provides a centralized system for storing student information and generating useful attendance and performance analytics.

## 3. Objectives

The main objectives of the project are:

- To maintain student information digitally.
- To manage student attendance records.
- To manage academic performance records.
- To calculate attendance percentages.
- To calculate performance percentages.
- To provide individual student analytics.
- To provide class-level analytics.
- To generate student reports.
- To validate user input and reduce invalid data.
- To store information securely using an SQLite database.

## 4. Features

### Student Management
- Add student
- Search student
- Update student
- Delete student

### Attendance Management
- Add attendance records
- Update attendance for an existing subject
- Calculate attendance percentage
- Generate subject-wise attendance information

### Performance Management
- Add performance records
- Update performance for an existing subject
- Calculate total performance
- Calculate performance percentage

### Analytics
- Individual student analytics
- Class-level analytics
- Attendance analysis
- Performance analysis
- Student status classification

### Reporting
- Generate detailed student reports
- Display student details
- Display attendance information
- Display performance information
- Display overall statistics

## 5. Technologies Used

- Python 3
- SQLite
- SQL
- VS Code
- Git and GitHub

## 6. Project Structure
```text
CS_PROJECT/
│
├── main.py
├── database.py
├── student.py
├── attendance.py
├── performance.py
├── analytics.py
├── reports.py
├── validation.py
├── student_performance.db
├── README.md
└── statement.md


7. Description of Modules
main.py

Acts as the main entry point of the application and provides the menu-driven interface.

database.py

Creates the SQLite database connection and required database tables.

student.py

Handles student management operations such as adding, searching, updating, and deleting students.

attendance.py

Handles attendance records and attendance percentage calculations.

performance.py

Handles academic performance records and performance calculations.

analytics.py

Provides individual student and class-level analytics.

reports.py

Generates detailed student reports containing attendance and performance information.

validation.py

Contains validation functions used to check user input.


8. Database Design

The project uses three main tables:

Students

Stores student information.

Important fields:

student_id
name
class_name
section
semester
Attendance

Stores attendance information.

Important fields:

attendance_id
student_id
subject
total_classes
classes_attended
Performance

Stores academic performance.

Important fields:

performance_id
student_id
subject
assignment_marks
internal_marks
exam_marks

The attendance and performance tables are related to the students table through student_id.


9. Application Workflow
Start Application
       |
       v
Create/Connect Database
       |
       v
Display Main Menu
       |
       +---- Student Management
       |
       +---- Attendance Management
       |
       +---- Performance Management
       |
       +---- Student Analytics
       |
       +---- Student Reports
       |
       +---- Class Analytics
       |
       v
Exit Application


10. Validation and Error Handling

The system validates important user inputs, including:

Empty names
Empty subjects
Invalid student IDs
Invalid semester values
Invalid attendance values
Invalid marks
Non-existent students

Database operations use parameterized SQL queries to reduce SQL injection risks.


11. Testing

The application was tested for:

Student creation
Student search
Student update
Student deletion
Attendance insertion
Attendance update
Attendance percentage calculation
Performance insertion
Performance update
Performance percentage calculation
Individual analytics
Class analytics
Student report generation
Invalid input handling


12. Example Result

For a sample student:

Attendance : 66.67%
Performance: 90.00
Status     : Needs Improvement

The system can also generate a detailed student report containing subject-wise attendance and performance.


13. Future Enhancements

Possible future improvements include:

Graphical user interface
Web-based interface
Login and authentication
Export reports to PDF
Export data to Excel
Attendance and performance charts
Automated notifications for low attendance
More advanced student performance analysis


14. Conclusion

The Student Performance and Attendance Analytics System provides a structured way to manage student information, attendance, and academic performance.

The modular Python implementation and SQLite database make the system easy to maintain and extend. The analytics and reporting features provide additional insight into student and class performance.