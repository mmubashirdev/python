import tkinter as tk
from ERP_pyodbc import *

# Initialize DB
init_db()
create_tables()

root = tk.Tk()
root.title("Lahore Garrison University - School Management System")
root.geometry("500x500")
root.configure(bg="#f0f0f0")

def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()

# ---------- Screens ----------
def login_screen():
    clear_screen()
    tk.Label(root, text="Lahore Garrison University", font=("Arial", 16, "bold"), fg="#006400").pack(pady=10)
    tk.Label(root, text="School Management System", font=("Arial", 12), fg="#228B22").pack(pady=5)
    tk.Label(root, text="Login", font=("Arial", 20, "bold"), fg="#006400").pack(pady=20)

    tk.Label(root, text="Name", fg="#006400", font=("Arial", 10, "bold")).pack()
    name_entry = tk.Entry(root)
    name_entry.pack(pady=5)

    tk.Label(root, text="Password", fg="#006400", font=("Arial", 10, "bold")).pack()
    pass_entry = tk.Entry(root, show="*")
    pass_entry.pack(pady=5)

    def try_login():
        if verify_login(name_entry.get(), pass_entry.get()):
            dashboard(name_entry.get())
        else:
            tk.Label(root, text="Login Failed", fg="red", font=("Arial", 10, "bold")).pack(pady=10)

    tk.Button(root, text="Login", command=try_login).pack(pady=10)
    tk.Button(root, text="Add New Student", command=add_student_screen).pack(pady=5)

# ----- Student -----
def add_student_screen():
    clear_screen()
    tk.Label(root, text="Add Student", font=("Arial", 20, "bold"), fg="#006400").pack(pady=20)

    tk.Label(root, text="Name", fg="#006400", font=("Arial", 10, "bold")).pack()
    name_entry = tk.Entry(root)
    name_entry.pack(pady=5)

    tk.Label(root, text="Grade", fg="#006400", font=("Arial", 10, "bold")).pack()
    grade_entry = tk.Entry(root)
    grade_entry.pack(pady=5)

    tk.Label(root, text="Password", fg="#006400", font=("Arial", 10, "bold")).pack()
    pass_entry = tk.Entry(root, show="*")
    pass_entry.pack(pady=5)

    def save_student():
        add_student(name_entry.get(), grade_entry.get(), pass_entry.get())
        tk.Label(root, text="Student Added!", fg="#006400", font=("Arial", 10, "bold")).pack(pady=10)

    tk.Button(root, text="Save", command=save_student).pack(pady=10)
    tk.Button(root, text="Back", command=login_screen).pack(pady=5)

# ----- Teacher -----
def add_teacher_screen():
    clear_screen()
    tk.Label(root, text="Add Teacher", font=("Arial", 20, "bold"), fg="#006400").pack(pady=20)

    tk.Label(root, text="Name", fg="#006400", font=("Arial", 10, "bold")).pack()
    name_entry = tk.Entry(root)
    name_entry.pack(pady=5)

    tk.Label(root, text="Subject", fg="#006400", font=("Arial", 10, "bold")).pack()
    sub_entry = tk.Entry(root)
    sub_entry.pack(pady=5)

    def save_teacher():
        add_teacher(name_entry.get(), sub_entry.get())
        tk.Label(root, text="Teacher Added!", fg="#006400", font=("Arial", 10, "bold")).pack(pady=10)

    tk.Button(root, text="Save", command=save_teacher).pack(pady=10)
    tk.Button(root, text="Back", command=dashboard_root).pack(pady=5)

# ----- Dashboard -----
def dashboard(user):
    global dashboard_root
    dashboard_root = lambda: dashboard(user)
    clear_screen()
    tk.Label(root, text="Lahore Garrison University", font=("Arial", 14, "bold"), fg="#006400").pack(pady=5)
    tk.Label(root, text=f"Welcome, {user}!", font=("Arial", 18, "bold"), fg="#228B22").pack(pady=20)
    tk.Button(root, text="Add Student", width=20, command=add_student_screen).pack(pady=5)
    tk.Button(root, text="Add Teacher", width=20, command=add_teacher_screen).pack(pady=5)
    tk.Button(root, text="Logout", width=20, command=login_screen).pack(pady=5)

login_screen()
root.mainloop()
