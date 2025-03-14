from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="partay.123",
    database="student_management_system"
)
cursor = conn.cursor()

@app.route('/students/all')
def show_all_students():
    cursor.execute("SELECT * FROM student")
    students = cursor.fetchall()
    # for student in students:
    # print(students)
    return render_template('all_students.html', students=students)

@app.route('/students/<int:student_number>')
def show_student_info(student_number):
    cursor.execute("SELECT * FROM student WHERE student_number = %s", (student_number,))
    student = cursor.fetchone()
    if student is None:
        return "Student not found", 404

    cursor.execute("""
        SELECT course.course_name, course.course_number, section.section_id, section.instructor,
               course.credit_hours, section.semester, section.year, grade_report.grade
        FROM grade_report
        JOIN section ON grade_report.section_id = section.section_id
        JOIN course ON section.course_number = course.course_number
        WHERE grade_report.student_number = %s
    """, (student_number,))
    student_info = cursor.fetchall()

    conn.close()
    return render_template('student.html', student=student, student_info = student_info)

@app.route('/courses/all')
def show_all_courses():
    cursor.execute("SELECT * FROM course")
    courses = cursor.fetchall()
    
    cursor.execute("SELECT * FROM prerequisite")
    prerequisites = cursor.fetchall()
    
    return render_template('all_courses.html', courses=courses, prerequisites=prerequisites)


@app.route('/courses/<course_id>')
def show_course(course_id):
    cursor.execute("SELECT * FROM course WHERE course_number = %s", (course_id,))
    course = cursor.fetchone()
    cursor.execute("SELECT * FROM prerequisite WHERE course_number = %s", (course_id,))
    prerequisites = cursor.fetchall()
    # print(prerequisites)
    return render_template('course.html', course=course, prerequisites=prerequisites)

@app.route('/instructors/<id>')
def show_instructor(id):
    cursor.execute("""
        SELECT section.section_id, course.course_name, section.semester, section.year
        FROM section
        JOIN course ON section.course_number = course.course_number
        WHERE section.instructor = %s
    """, (id,))
    instructor_courses_data = cursor.fetchall()

    instructor_name = id

    return render_template('instructor.html', instructor_name=instructor_name, instructor_courses=instructor_courses_data)


if __name__ == '__main__':
    app.run(debug=True)
