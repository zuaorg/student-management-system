import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="partay.123",
    database="student_management_system"
)
cursor = conn.cursor()

students_data = [
    ("Smith", 17, 1, "CS"),
    ("Brown", 8, 2, "CS")
]

courses_data = [
    ("Intro to Computer Science", "CS1310", 4, "CS"),
    ("Data Structures", "CS3320", 4, "CS"),
    ("Discrete Mathematics", "MATH2410", 3, "MATH"),
    ("Database", "CS3380", 3, "CS")
]

sections_data = [
    (85, "MATH2410", "Fall", 2007, "King"),
    (92, "CS1310", "Fall", 2007, "Anderson"),
    (102, "CS3320", "Spring", 2008, "Knuth"),
    (112, "MATH2410", "Fall", 2008, "Chang"),
    (119, "CS1310", "Fall", 2008, "Anderson"),
    (135, "CS3380", "Fall", 2008, "Stone")
]

grade_report_data = [
    (17, 112, "B"),
    (17, 119, "C"),
    (8, 85, "A"),
    (8, 92, "A"),
    (8, 102, "B"),
    (8, 135, "A")
]

prerequisites_data = [
    ("CS3380", "CS3320"),
    ("CS3380", "MATH2410"),
    ("CS3320", "CS1310")
]

student_query = "INSERT INTO student (name, student_number, class, major) VALUES (%s, %s, %s, %s)"
course_query = "INSERT INTO course (course_name, course_number, credit_hours, department) VALUES (%s, %s, %s, %s)"
section_query = "INSERT INTO section (section_id, course_number, semester, year, instructor) VALUES (%s, %s, %s, %s, %s)"
grade_report_query = "INSERT INTO grade_report (student_number, section_id, grade) VALUES (%s, %s, %s)"
prerequisite_query = "INSERT INTO prerequisite (course_number, prerequisite_number) VALUES (%s, %s)"

cursor.executemany(student_query, students_data)
cursor.executemany(course_query, courses_data)
cursor.executemany(section_query, sections_data)
cursor.executemany(grade_report_query, grade_report_data)
cursor.executemany(prerequisite_query, prerequisites_data)

conn.commit()
conn.close()
