def validate_name(name):
    """Check that the name is not empty."""
    return bool(name.strip())


def validate_positive_integer(value):
    """Check that a value is a positive integer."""
    try:
        number = int(value)
        return number > 0
    except ValueError:
        return False


def validate_non_negative_integer(value):
    """Check that a value is a non-negative integer."""
    try:
        number = int(value)
        return number >= 0
    except ValueError:
        return False


def validate_marks(value):
    """Check that marks are between 0 and 100."""
    try:
        marks = float(value)
        return 0 <= marks <= 100
    except ValueError:
        return False


def validate_attendance(total_classes, classes_attended):
    """Check that attendance values are valid."""
    try:
        total = int(total_classes)
        attended = int(classes_attended)

        if total <= 0:
            return False

        if attended < 0 or attended > total:
            return False

        return True

    except ValueError:
        return False


def student_exists(student_id):
    """Check whether a student ID exists in the database."""
    import sqlite3

    try:
        student_id = int(student_id)
    except ValueError:
        return False

    connection = sqlite3.connect("student_performance.db")
    cursor = connection.cursor()

    cursor.execute(
        "SELECT student_id FROM students WHERE student_id = ?",
        (student_id,)
    )

    student = cursor.fetchone()
    connection.close()

    return student is not None