import tkinter as tk
from ERP_pyodbc import *

# Initialize DB
init_db()
create_tables()

root = tk.Tk()
root.title("School ERP Portal")
root.geometry("500x500")

def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()

# ---------- Screens ----------
def login_screen():
    clear_screen()
    tk.Label(root, text="Login", font=("Arial", 20)).pack(pady=20)

    tk.Label(root, text="Name").pack()
    name_entry = tk.Entry(root)
    name_entry.pack(pady=5)

    tk.Label(root, text="Password").pack()
    pass_entry = tk.Entry(root, show="*")
    pass_entry.pack(pady=5)

    def try_login():
        if verify_login(name_entry.get(), pass_entry.get()):
            dashboard(name_entry.get())
        else:
            tk.Label(root, text="Login Failed", fg="red").pack(pady=10)

    tk.Button(root, text="Login", command=try_login).pack(pady=10)
    tk.Button(root, text="Add New Student", command=add_student_screen).pack(pady=5)

# ----- Student -----
def add_student_screen():
    clear_screen()
    tk.Label(root, text="Add Student", font=("Arial", 20)).pack(pady=20)

    tk.Label(root, text="Name").pack()
    name_entry = tk.Entry(root)
    name_entry.pack(pady=5)

    tk.Label(root, text="Grade").pack()
    grade_entry = tk.Entry(root)
    grade_entry.pack(pady=5)

    tk.Label(root, text="Password").pack()
    pass_entry = tk.Entry(root, show="*")
    pass_entry.pack(pady=5)

    def save_student():
        add_student(name_entry.get(), grade_entry.get(), pass_entry.get())
        tk.Label(root, text="Student Added!", fg="green").pack(pady=10)

    tk.Button(root, text="Save", command=save_student).pack(pady=10)
    tk.Button(root, text="Back", command=login_screen).pack(pady=5)

# ----- Teacher -----
def add_teacher_screen():
    clear_screen()
    tk.Label(root, text="Add Teacher", font=("Arial", 20)).pack(pady=20)

    tk.Label(root, text="Name").pack()
    name_entry = tk.Entry(root)
    name_entry.pack(pady=5)

    tk.Label(root, text="Subject").pack()
    sub_entry = tk.Entry(root)
    sub_entry.pack(pady=5)

    def save_teacher():
        add_teacher(name_entry.get(), sub_entry.get())
        tk.Label(root, text="Teacher Added!", fg="green").pack(pady=10)

    tk.Button(root, text="Save", command=save_teacher).pack(pady=10)
    tk.Button(root, text="Back", command=dashboard_root).pack(pady=5)

# ----- Dashboard -----
def dashboard(user):
    global dashboard_root
    dashboard_root = lambda: dashboard(user)
    clear_screen()
    tk.Label(root, text=f"Welcome, {user}", font=("Arial", 20), fg="green").pack(pady=20)
    tk.Button(root, text="Add Student", width=20, command=add_student_screen).pack(pady=5)
    tk.Button(root, text="Add Teacher", width=20, command=add_teacher_screen).pack(pady=5)
    tk.Button(root, text="Logout", width=20, command=login_screen).pack(pady=5)

login_screen()
root.mainloop()
