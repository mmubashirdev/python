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
