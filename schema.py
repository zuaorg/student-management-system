import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="partay.123",
    database="student_management_system"
)
cursor = conn.cursor()

create_student_table = """
CREATE TABLE IF NOT EXISTS student (
    student_number INT PRIMARY KEY,
    name VARCHAR(16),
    class VARCHAR(16),
    major VARCHAR(16)
)
"""

create_course_table = """
CREATE TABLE IF NOT EXISTS course (
    course_number VARCHAR(16) PRIMARY KEY,
    course_name VARCHAR(32),
    credit_hours INT,
    department VARCHAR(16)
)
"""

create_prerequisite_table = """
CREATE TABLE IF NOT EXISTS prerequisite (
    course_number VARCHAR(16),
    prerequisite_number VARCHAR(16),
    FOREIGN KEY (course_number) REFERENCES course(course_number),
    PRIMARY KEY (course_number, prerequisite_number)
)
"""

create_section_table = """
CREATE TABLE IF NOT EXISTS section (
    section_id INT PRIMARY KEY,
    course_number VARCHAR(16),
    semester VARCHAR(16),
    year INT,
    instructor VARCHAR(16),
    FOREIGN KEY (course_number) REFERENCES course(course_number)
)
"""

create_grade_report_table = """
CREATE TABLE IF NOT EXISTS grade_report (
    student_number INT,
    section_id INT,
    grade VARCHAR(2),
    FOREIGN KEY (student_number) REFERENCES student(student_number),
    FOREIGN KEY (section_id) REFERENCES section(section_id),
    PRIMARY KEY (student_number, section_id)
)
"""

cursor.execute(create_student_table)
cursor.execute(create_course_table)
cursor.execute(create_prerequisite_table)
cursor.execute(create_section_table)
cursor.execute(create_grade_report_table)

cursor.execute("CREATE INDEX student_number_index ON student (student_number)")
cursor.execute("CREATE INDEX course_number_index ON course (course_number)")
cursor.execute("CREATE INDEX course_number_index ON section (course_number)")
cursor.execute("CREATE INDEX student_number_section_id_index ON grade_report (student_number, section_id)")

conn.commit()
conn.close()
