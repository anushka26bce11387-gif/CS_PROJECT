import sqlite3


DATABASE_NAME = "student_performance.db"


def create_connection():
    """Create and return a connection to the SQLite database."""
    try:
        connection = sqlite3.connect(DATABASE_NAME)

        # Enable foreign key constraints
        connection.execute("PRAGMA foreign_keys = ON")

        return connection

    except sqlite3.Error as error:
        print(f"Database connection error: {error}")
        return None


def create_tables():
    """Create the required tables for the project."""

    connection = create_connection()

    if connection is None:
        return

    cursor = connection.cursor()

    # Students table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            class_name TEXT NOT NULL,
            section TEXT NOT NULL,
            semester INTEGER
        )
    """)

    # Attendance table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS attendance (
            attendance_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            subject TEXT NOT NULL,
            total_classes INTEGER NOT NULL,
            classes_attended INTEGER NOT NULL,

            FOREIGN KEY (student_id)
            REFERENCES students(student_id)
        )
    """)

    # Performance table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS performance (
            performance_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            subject TEXT NOT NULL,
            assignment_marks REAL DEFAULT 0,
            internal_marks REAL DEFAULT 0,
            exam_marks REAL DEFAULT 0,

            FOREIGN KEY (student_id)
            REFERENCES students(student_id)
        )
    """)

    connection.commit()
    connection.close()

    print("Database and tables created successfully.")


if __name__ == "__main__":
    create_tables()