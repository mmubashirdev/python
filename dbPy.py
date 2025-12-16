import pyodbc

con = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER={localhost\MSSQLSERVER01};"
    "DATABASE=Harry_db;"
    "Trusted_Connection=yes;",
    autocommit=True
)

cursor = con.cursor()
print("DB connection successful")

cursor.execute("""
IF DB_ID('Harry_db') IS NULL 
    CREATE DATABASE Harry_db;
""")
con.commit()
print("Database created")

cursor.execute('''IF OBJECT_ID('student','U') IS NULL
CREATE TABLE student(
    id int identity(1,1) primary key,
    studName nvarchar(20),
    age int,
    grade nvarchar(10)
)
''')
con.commit()
print("Table created")

cursor.execute("insert into student(studName,age,grade) values (?,?,?)",('Alice',20,'A'))
cursor.execute("insert into student(studName,age,grade) values (?,?,?)",('Bob',22,'B'))
con.commit()

print("Sample data inserted successfully!")
cursor.execute("Select * from student")
row = cursor.fetchall()

for r in row:
    print(r)
con.close()
print("Connection close!")

