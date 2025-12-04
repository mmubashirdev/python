import pyodbc

def get_con():
    return pyodbc.connect(
        "Driver={ODBC Driver 17 for SQL Server};"
        "Server={localhost\\MSSQLSERVER01};"
        "Database=SCHOOL_DB;"
        "trusted_connection=yes;",
        autocommit=True
    )

def init_db():
    con = pyodbc.connect(
        "Driver={ODBC Driver 17 for SQL Server};"
        "Server={localhost\\MSSQLSERVER01};"
        "trusted_connection=yes;",
        autocommit=True
    )
    cur = con.cursor()
    cur.execute("IF DB_ID('SCHOOL_DB') IS NULL CREATE DATABASE SCHOOL_DB;")
    con.commit()
    con.close()

def create_tables():
    con = get_con()
    cur = con.cursor()

    # Students
    cur.execute("""
        IF OBJECT_ID('Students') IS NULL
        CREATE TABLE Students (
            id INT IDENTITY(1,1) PRIMARY KEY,
            name NVARCHAR(50),
            grade NVARCHAR(10),
            password NVARCHAR(50)
        )
    """)

    # Teachers
    cur.execute("""
        IF OBJECT_ID('Teachers') IS NULL
        CREATE TABLE Teachers (
            id INT IDENTITY(1,1) PRIMARY KEY,
            name NVARCHAR(50),
            subject NVARCHAR(50)
        )
    """)

    # Attendance
    cur.execute("""
        IF OBJECT_ID('Attendance') IS NULL
        CREATE TABLE Attendance (
            id INT IDENTITY(1,1) PRIMARY KEY,
            student_id INT,
            date DATE,
            status NVARCHAR(10),
            FOREIGN KEY(student_id) REFERENCES Students(id)
        )
    """)

    # Fees
    cur.execute("""
        IF OBJECT_ID('Fees') IS NULL
        CREATE TABLE Fees (
            id INT IDENTITY(1,1) PRIMARY KEY,
            student_id INT,
            amount DECIMAL(10,2),
            status NVARCHAR(10),
            FOREIGN KEY(student_id) REFERENCES Students(id)
        )
    """)

    # Performance
    cur.execute("""
        IF OBJECT_ID('Performance') IS NULL
        CREATE TABLE Performance (
            id INT IDENTITY(1,1) PRIMARY KEY,
            student_id INT,
            subject NVARCHAR(50),
            marks INT,
            FOREIGN KEY(student_id) REFERENCES Students(id)
        )
    """)

    con.commit()
    con.close()


# ----- CRUD Operations -----
def add_student(name, grade, password):
    con = get_con()
    cur = con.cursor()
    cur.execute("INSERT INTO Students(name, grade, password) VALUES (?,?,?)",
                (name, grade, password))
    con.commit()
    con.close()

def verify_login(name, password):
    con = get_con()
    cur = con.cursor()
    cur.execute("SELECT * FROM Students WHERE name=? AND password=?", (name, password))
    result = cur.fetchone()
    con.close()
    return result is not None

def add_teacher(name, subject):
    con = get_con()
    cur = con.cursor()
    cur.execute("INSERT INTO Teachers(name, subject) VALUES (?,?)", (name, subject))
    con.commit()
    con.close()

def add_attendance(student_id, date, status):
    con = get_con()
    cur = con.cursor()
    cur.execute("INSERT INTO Attendance(student_id, date, status) VALUES (?,?,?)",
                (student_id, date, status))
    con.commit()
    con.close()

def add_fee(student_id, amount, status):
    con = get_con()
    cur = con.cursor()
    cur.execute("INSERT INTO Fees(student_id, amount, status) VALUES (?,?,?)",
                (student_id, amount, status))
    con.commit()
    con.close()

def add_performance(student_id, subject, marks):
    con = get_con()
    cur = con.cursor()
    cur.execute("INSERT INTO Performance(student_id, subject, marks) VALUES (?,?,?)",
                (student_id, subject, marks))
    con.commit()
    con.close()

# ----- Additional CRUD Operations -----
def get_student(student_id):
    con = get_con()
    cur = con.cursor()
    cur.execute("SELECT * FROM Students WHERE id=?", (student_id,))
    result = cur.fetchone()
    con.close()
    return result

def get_all_students():
    con = get_con()
    cur = con.cursor()
    cur.execute("SELECT * FROM Students")
    results = cur.fetchall()
    con.close()
    return results

def update_student(student_id, name, grade, password):
    con = get_con()
    cur = con.cursor()
    cur.execute("UPDATE Students SET name=?, grade=?, password=? WHERE id=?",
                (name, grade, password, student_id))
    con.commit()
    con.close()

def delete_student(student_id):
    con = get_con()
    cur = con.cursor()
    # Delete related records first
    cur.execute("DELETE FROM Attendance WHERE student_id=?", (student_id,))
    cur.execute("DELETE FROM Fees WHERE student_id=?", (student_id,))
    cur.execute("DELETE FROM Performance WHERE student_id=?", (student_id,))
    cur.execute("DELETE FROM Students WHERE id=?", (student_id,))
    con.commit()
    con.close()

def get_all_teachers():
    con = get_con()
    cur = con.cursor()
    cur.execute("SELECT * FROM Teachers")
    results = cur.fetchall()
    con.close()
    return results

def update_teacher(teacher_id, name, subject):
    con = get_con()
    cur = con.cursor()
    cur.execute("UPDATE Teachers SET name=?, subject=? WHERE id=?",
                (name, subject, teacher_id))
    con.commit()
    con.close()

def delete_teacher(teacher_id):
    con = get_con()
    cur = con.cursor()
    cur.execute("DELETE FROM Teachers WHERE id=?", (teacher_id,))
    con.commit()
    con.close()

def get_student_attendance(student_id):
    con = get_con()
    cur = con.cursor()
    cur.execute("SELECT * FROM Attendance WHERE student_id=? ORDER BY date DESC", (student_id,))
    results = cur.fetchall()
    con.close()
    return results

def update_attendance(attendance_id, status):
    con = get_con()
    cur = con.cursor()
    cur.execute("UPDATE Attendance SET status=? WHERE id=?", (status, attendance_id))
    con.commit()
    con.close()

def delete_attendance(attendance_id):
    con = get_con()
    cur = con.cursor()
    cur.execute("DELETE FROM Attendance WHERE id=?", (attendance_id,))
    con.commit()
    con.close()

def get_student_fees(student_id):
    con = get_con()
    cur = con.cursor()
    cur.execute("SELECT * FROM Fees WHERE student_id=?", (student_id,))
    results = cur.fetchall()
    con.close()
    return results

def update_fee(fee_id, amount, status):
    con = get_con()
    cur = con.cursor()
    cur.execute("UPDATE Fees SET amount=?, status=? WHERE id=?",
                (amount, status, fee_id))
    con.commit()
    con.close()

def delete_fee(fee_id):
    con = get_con()
    cur = con.cursor()
    cur.execute("DELETE FROM Fees WHERE id=?", (fee_id,))
    con.commit()
    con.close()

def get_student_performance(student_id):
    con = get_con()
    cur = con.cursor()
    cur.execute("SELECT * FROM Performance WHERE student_id=?", (student_id,))
    results = cur.fetchall()
    con.close()
    return results

def update_performance(performance_id, subject, marks):
    con = get_con()
    cur = con.cursor()
    cur.execute("UPDATE Performance SET subject=?, marks=? WHERE id=?",
                (subject, marks, performance_id))
    con.commit()
    con.close()

def delete_performance(performance_id):
    con = get_con()
    cur = con.cursor()
    cur.execute("DELETE FROM Performance WHERE id=?", (performance_id,))
    con.commit()
    con.close()

def get_student_by_name(name):
    con = get_con()
    cur = con.cursor()
    cur.execute("SELECT * FROM Students WHERE name=?", (name,))
    result = cur.fetchone()
    con.close()
    return result

def calculate_student_gpa(student_id):
    """Calculate GPA based on performance marks"""
    con = get_con()
    cur = con.cursor()
    cur.execute("SELECT AVG(CAST(marks AS FLOAT)) FROM Performance WHERE student_id=?", 
                (student_id,))
    result = cur.fetchone()
    con.close()
    if result and result[0]:
        return round(result[0] / 20, 2)  # Assuming marks out of 100, GPA out of 5
    return 0.0

def get_performance_report(student_id):
    """Generate performance report for a student"""
    con = get_con()
    cur = con.cursor()
    
    # Get student info
    cur.execute("SELECT * FROM Students WHERE id=?", (student_id,))
    student = cur.fetchone()
    
    # Get all performance records
    cur.execute("SELECT subject, marks FROM Performance WHERE student_id=? ORDER BY subject", 
                (student_id,))
    performances = cur.fetchall()
    
    # Get attendance info
    cur.execute("""SELECT COUNT(*) as total, 
                   SUM(CASE WHEN status='Present' THEN 1 ELSE 0 END) as present 
                   FROM Attendance WHERE student_id=?""", (student_id,))
    attendance = cur.fetchone()
    
    # Get fees info
    cur.execute("SELECT SUM(amount) as total, COUNT(*) as count FROM Fees WHERE student_id=?", 
                (student_id,))
    fees = cur.fetchone()
    
    con.close()
    
    return {
        'student': student,
        'performances': performances,
        'attendance': attendance,
        'fees': fees
    }
