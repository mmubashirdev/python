studentData = [
    {'name': 'Ali', 'age': 15, 'grade': 8},
    {'name': 'Sara', 'age': 14, 'grade': 7},
    {'name': 'John', 'age': 16, 'grade': 9}
]


def studentRecord():
    for student in studentData:
        print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")


def greet(num=3):
    for _ in range(num):  
        print("Hello")


def login(role, username, password):

    if role == 'teacher':
        if username == 'tea' and password == 111:
            print("Login Success as Teacher")
        else:
            print("Wrong credentials")
    elif role == 'admin':
        if username == 'adm' and password == 222:
            print("Login Success as Admin")
        else:
            print("Wrong credentials")
    else:
        print("Invalid role")

studentRecord()
greet()
login("teacher", "tea", 111) 
