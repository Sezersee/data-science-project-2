import psycopg2

## Bu değeri localinde çalışırken kendi passwordün yap. Ama kodu pushlarken 'postgres' olarak bırak.
password = 'postgres'


def connect_db():
    conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="postgres",
    user="postgres",
    password="301291")
    return conn


def question_1_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM students WHERE age > 22;')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_2_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM courses WHERE category = 'Veritabanı';")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_3_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students WHERE first_name LIKE 'A%'") 
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_4_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM courses WHERE course_name LIKE '%SQL%';") 
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_5_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students WHERE age BETWEEN 22 AND 24;")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_6_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT DISTINCT s.first_name, s.last_name FROM students s JOIN enrollments e ON s.student_id = e.student_id;')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_7_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT c.course_name, COUNT(DISTINCT e.student_id) AS student_count FROM courses c JOIN enrollments e ON c.course_id = e.course_id WHERE c.course_name LIKE '%SQL%' GROUP BY c.course_name;")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_8_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT c.course_name, i.name AS instructor_name FROM courses c JOIN course_instructors ci ON c.course_id = ci.course_id JOIN instructors i ON ci.instructor_id = i.instructor_id;')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_9_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT s.student_id, s.first_name, s.last_name FROM students s LEFT JOIN enrollments e ON s.student_id = e.student_id WHERE e.enrollment_id IS NULL;')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_10_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT c.course_name, ROUND(AVG(s.age), 2) AS average_age FROM courses c JOIN enrollments e ON c.course_id = e.course_id JOIN students s ON e.student_id = s.student_id GROUP BY c.course_name;')
    data = cursor.fetchall() 
    cursor.close()
    connection.close()
    return data


def question_11_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT s.first_name, s.last_name, COUNT(e.course_id)AS total_courses FROM students AS s LEFT JOIN enrollments AS e ON s.student_id=e.student_id  JOIN courses AS c ON c.course_id=e.course_id GROUP BY s.student_id;')
    data = cursor.fetchall()
    cursor.close()   
    connection.close()
    return data


def question_12_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT i.name AS instructor_name, COUNT(ci.course_id) AS total_courses FROM instructors i JOIN course_instructors ci ON i.instructor_id = ci.instructor_id GROUP BY i.name HAVING COUNT(ci.course_id) > 1;')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_13_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT c.course_name, COUNT(DISTINCT e.student_id) AS unique_student_count FROM courses c JOIN enrollments e ON c.course_id = e.course_id GROUP BY c.course_name;')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_14_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT s.first_name , s.last_name  FROM courses AS c RIGHT JOIN enrollments AS e ON c.course_id=e.course_id RIGHT JOIN students AS s ON s.student_id=e.student_id WHERE c.course_name='SQL Temelleri' OR c.course_name='İleri SQL' GROUP BY s.student_id HAVING COUNT(s.student_id)>1;")
    data = cursor.fetchall() 
    cursor.close()
    connection.close()
    return data


def question_15_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT s.first_name , s.last_name ,c.course_name , i.name as instructor_name, e.enrollment_date FROM students AS s RIGHT JOIN enrollments AS e ON s.student_id=e.student_id  JOIN courses AS c ON c.course_id=e.course_id JOIN course_instructors  AS ci ON c.course_id=ci.course_id  join instructors AS i ON ci.instructor_id=i.instructor_id;")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data