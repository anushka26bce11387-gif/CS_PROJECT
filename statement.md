# Student Performance and Attendance Analytics System

## 1. Project Introduction

The **Student Performance and Attendance Analytics System** is a Python-based application developed to manage student information, attendance records, academic performance, and analytics.

The system uses **SQLite** for database storage and provides a menu-driven interface for performing student management, attendance management, performance management, analytics, and report generation.

---

## 2. Problem Statement

Managing student information, attendance, and academic performance manually can be time-consuming and may lead to calculation and record-management errors.

The proposed system provides a centralized solution for storing student records and automatically calculating attendance and performance information.

---

## 3. Objectives

The main objectives of the project are:

* To manage student information digitally.
* To maintain attendance records.
* To manage academic performance records.
* To calculate attendance and performance percentages.
* To provide student and class-level analytics.
* To generate student reports.
* To validate user input and reduce errors.
* To store records using an SQLite database.

---

## 4. Scope

The system covers:

* Student management
* Attendance management
* Performance management
* Student analytics
* Class analytics
* Student report generation
* Input validation
* SQLite database storage

The current version is a local, command-line application. Features such as online access, authentication, mobile applications, and machine-learning prediction are outside the current scope.

---

## 5. Functional Requirements

The system provides the following major functions:

1. Add, search, update, and delete students.
2. Add and update attendance records.
3. Calculate attendance percentages.
4. Add and update performance records.
5. Calculate performance information.
6. Generate individual student analytics.
7. Generate class-level analytics.
8. Generate detailed student reports.
9. Validate user input and display error messages.

---

## 6. Non-Functional Requirements

* **Usability:** The system should be simple and easy to operate.
* **Reliability:** Student records should be stored and retrieved correctly.
* **Maintainability:** The application should use separate modules for different functions.
* **Performance:** Database operations and calculations should be performed efficiently.
* **Security:** Parameterized SQL queries should be used for database operations.
* **Data Integrity:** Foreign key relationships should maintain consistency between related records.

---

## 7. Technologies Used

* **Python 3** – Application development
* **SQLite** – Database management
* **SQL** – Database operations
* **VS Code** – Development environment
* **Git/GitHub** – Version control and project repository

---

## 8. System Modules

| Module           | Purpose                                 |
| ---------------- | --------------------------------------- |
| `main.py`        | Main menu and application control       |
| `database.py`    | Database connection and table creation  |
| `student.py`     | Student management                      |
| `attendance.py`  | Attendance management and calculations  |
| `performance.py` | Performance management and calculations |
| `analytics.py`   | Student and class analytics             |
| `reports.py`     | Student report generation               |
| `validation.py`  | Input validation                        |

---

## 9. Database Design

The system uses an SQLite database named `student_performance.db`.

It contains three main tables:

* **Students** – stores student details.
* **Attendance** – stores attendance records.
* **Performance** – stores academic performance records.

The `student_id` field connects attendance and performance records with the corresponding student.

The relationship is:

```text
Students
   |
   | 1
   |
   +------< Attendance
   |
   +------< Performance
```

This represents a **one-to-many relationship** between students and their attendance/performance records.

---

## 10. Testing

The system was tested for:

* Student CRUD operations
* Attendance entry and calculation
* Duplicate attendance updates
* Performance entry and calculation
* Duplicate performance updates
* Student analytics
* Class analytics
* Student report generation
* Invalid student IDs
* Invalid attendance values
* Invalid marks

All major functional tests performed during development produced the expected results.

---

## 11. Future Enhancements

Possible future enhancements include:

* Graphical User Interface
* Web-based application
* User authentication
* Attendance visualization
* PDF/Excel report export
* Cloud database support
* Automated attendance
* Machine-learning-based performance prediction

---

## 12. Conclusion

The Student Performance and Attendance Analytics System provides a structured solution for managing student records, attendance, performance, analytics, and reports.

The project demonstrates practical use of Python, modular programming, SQL, SQLite, input validation, database relationships, and software testing. It provides a foundation that can be extended with advanced features in the future.
