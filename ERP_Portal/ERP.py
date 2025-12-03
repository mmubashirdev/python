import tkinter as tk
from ERP_pyodbc import init_db, create_tables, add_student, verify_login, get_student, delete_student

init_db()
create_tables()

root = tk.Tk()
root.title("School Management System")
root.geometry("500x500")

def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()

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
        name = name_entry.get().strip()
        password = pass_entry.get().strip()
        if verify_login(name, password):
            dashboard(name)
        else:
            tk.Label(root, text="Login Failed", fg="red").pack(pady=10)

    tk.Button(root, text="Login", command=try_login).pack(pady=10)
    tk.Button(root, text="Add New Student", command=add_student_screen).pack(pady=5)

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
        add_student(name_entry.get().strip(), grade_entry.get().strip(), pass_entry.get().strip())
        tk.Label(root, text="Student Added", fg="green").pack(pady=10)

    tk.Button(root, text="Save", command=save_student).pack(pady=10)
    tk.Button(root, text="Back", command=login_screen).pack(pady=5)

def dashboard(user):
    clear_screen()
    tk.Label(root, text=f"Welcome, {user}", font=("Arial", 20), fg="green").pack(pady=20)
    tk.Button(root, text="Add Student", width=20, command=add_student_screen).pack(pady=5)
    tk.Button(root, text="Logout", width=20, command=login_screen).pack(pady=5)

login_screen()
root.mainloop()
