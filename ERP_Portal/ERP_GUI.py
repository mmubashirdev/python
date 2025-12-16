import tkinter as tk
from tkinter import messagebox, scrolledtext
from PIL import Image, ImageTk
from ERP_pyodbc import *

init_db()
create_tables()

root = tk.Tk()
root.title("Lahore Garrison University - School Management System")
root.geometry("600x700")

bg_img = Image.open("background.png")
bg = ImageTk.PhotoImage(bg_img)

logo_img = Image.open("lguLogo.png")
logo_img = logo_img.resize((120, 120))
logo = ImageTk.PhotoImage(logo_img)

background_label = tk.Label(root, image=bg)
background_label.image = bg
background_label.place(x=0, y=0, relwidth=1, relheight=1)


def clear_screen():
    for widget in root.winfo_children():
        if widget == background_label:
            continue
        widget.destroy()


def login_screen():
    clear_screen()

    title = tk.Label(root, text="Lahore Garrison University",
                     font=("Arial", 24, "bold"), fg="#006400", bg="white")
    title.pack(pady=(40, 5))

    logo_label = tk.Label(root, image=logo, bg="white")
    logo_label.image = logo
    logo_label.pack(pady=(0, 30))

    tk.Label(root, text="Name", fg="#006400",
             font=("Arial", 16, "bold"), bg="white").pack()
    name_entry = tk.Entry(root, font=("Arial", 14), width=25)
    name_entry.pack(pady=5, ipady=5)

    tk.Label(root, text="Password", fg="#006400",
             font=("Arial", 16, "bold"), bg="white").pack()
    pass_entry = tk.Entry(root, show="*", font=("Arial", 14), width=25)
    pass_entry.pack(pady=5, ipady=5)

    def try_login():
        if verify_login(name_entry.get(), pass_entry.get()):
            dashboard(name_entry.get())
        else:
            messagebox.showerror("Login Failed", "Invalid credentials")

    tk.Button(root, text="Login", bg="#006400", fg="white",
              font=("Arial", 16), width=20, command=try_login).pack(pady=20)

    tk.Button(root, text="Add New Student", bg="#228B22", fg="white",
              font=("Arial", 16), width=20, command=add_student_screen).pack(pady=10)


def add_student_screen():
    clear_screen()

    tk.Label(root, text="Add Student", font=("Arial", 20, "bold"),
             fg="#006400", bg="white").pack(pady=20)

    tk.Label(root, text="Name", fg="#006400",
             font=("Arial", 12, "bold"), bg="white").pack()
    name_entry = tk.Entry(root, font=("Arial", 14), width=25)
    name_entry.pack(pady=5, ipady=5)

    tk.Label(root, text="Grade", fg="#006400",
             font=("Arial", 12, "bold"), bg="white").pack()
    grade_entry = tk.Entry(root, font=("Arial", 14), width=25)
    grade_entry.pack(pady=5, ipady=5)

    tk.Label(root, text="Password", fg="#006400",
             font=("Arial", 12, "bold"), bg="white").pack()
    pass_entry = tk.Entry(root, show="*", font=("Arial", 14), width=25)
    pass_entry.pack(pady=5, ipady=5)

    def save_student():
        add_student(name_entry.get(), grade_entry.get(), pass_entry.get())
        messagebox.showinfo("Success", "Student Added Successfully!")
        login_screen()

    tk.Button(root, text="Save", bg="#006400", fg="white", font=("Arial", 14),
              width=20, command=save_student).pack(pady=10)
    tk.Button(root, text="Back", bg="#228B22", fg="white", font=("Arial", 14),
              width=20, command=login_screen).pack(pady=5)


def dashboard(user):
    clear_screen()

    tk.Label(root, text="Lahore Garrison University", font=(
        "Arial", 14, "bold"), fg="#006400", bg="white").pack(pady=5)
    tk.Label(root, text=f"Welcome, {user}!", font=(
        "Arial", 18, "bold"), fg="#228B22", bg="white").pack(pady=20)

    tk.Button(root, text="View All Students", width=25,
              bg="#006400", fg="white", font=("Arial", 12), command=view_students_screen).pack(pady=5)
    tk.Button(root, text="Add Student", width=25,
              bg="#006400", fg="white", font=("Arial", 12), command=add_student_screen).pack(pady=5)
    tk.Button(root, text="Update Student", width=25,
              bg="#006400", fg="white", font=("Arial", 12), command=update_student_screen).pack(pady=5)
    tk.Button(root, text="Delete Student", width=25,
              bg="#006400", fg="white", font=("Arial", 12), command=delete_student_screen).pack(pady=5)
    tk.Button(root, text="Manage Teachers", width=25,
              bg="#228B22", fg="white", font=("Arial", 12), command=manage_teachers_screen).pack(pady=5)
    tk.Button(root, text="Manage Attendance", width=25,
              bg="#228B22", fg="white", font=("Arial", 12), command=manage_attendance_screen).pack(pady=5)
    tk.Button(root, text="Manage Fees", width=25,
              bg="#228B22", fg="white", font=("Arial", 12), command=manage_fees_screen).pack(pady=5)
    tk.Button(root, text="Manage Performance", width=25,
              bg="#228B22", fg="white", font=("Arial", 12), command=manage_performance_screen).pack(pady=5)
    tk.Button(root, text="Logout", width=25,
              bg="red", fg="white", font=("Arial", 12), command=login_screen).pack(pady=5)


def view_students_screen():
    clear_screen()

    tk.Label(root, text="All Students", font=("Arial", 20, "bold"),
             fg="#006400", bg="white").pack(pady=20)

    students = get_all_students()
    if students:
        text = "ID\tName\t\tGrade\n" + "-" * 40 + "\n"
        for student in students:
            text += f"{student[0]}\t{student[1]}\t\t{student[2]}\n"
        
        text_area = scrolledtext.ScrolledText(root, height=15, width=50, font=("Courier", 10))
        text_area.pack(pady=10)
        text_area.insert(1.0, text)
        text_area.config(state=tk.DISABLED)
    else:
        tk.Label(root, text="No students found", fg="#006400",
                 font=("Arial", 12, "bold"), bg="white").pack(pady=20)

    tk.Button(root, text="Back", bg="#228B22", fg="white", font=("Arial", 14),
              width=20, command=lambda: dashboard("Admin")).pack(pady=10)


def update_student_screen():
    clear_screen()

    tk.Label(root, text="Update Student", font=("Arial", 20, "bold"),
             fg="#006400", bg="white").pack(pady=20)

    tk.Label(root, text="Student ID", fg="#006400",
             font=("Arial", 12, "bold"), bg="white").pack()
    id_entry = tk.Entry(root, font=("Arial", 14), width=25)
    id_entry.pack(pady=5, ipady=5)

    tk.Label(root, text="Name", fg="#006400",
             font=("Arial", 12, "bold"), bg="white").pack()
    name_entry = tk.Entry(root, font=("Arial", 14), width=25)
    name_entry.pack(pady=5, ipady=5)

    tk.Label(root, text="Grade", fg="#006400",
             font=("Arial", 12, "bold"), bg="white").pack()
    grade_entry = tk.Entry(root, font=("Arial", 14), width=25)
    grade_entry.pack(pady=5, ipady=5)

    tk.Label(root, text="Password", fg="#006400",
             font=("Arial", 12, "bold"), bg="white").pack()
    pass_entry = tk.Entry(root, show="*", font=("Arial", 14), width=25)
    pass_entry.pack(pady=5, ipady=5)

    def save_update():
        try:
            update_student(int(id_entry.get()), name_entry.get(), grade_entry.get(), pass_entry.get())
            messagebox.showinfo("Success", "Student Updated Successfully!")
            dashboard("Admin")
        except:
            messagebox.showerror("Error", "Failed to update student")

    tk.Button(root, text="Update", bg="#006400", fg="white", font=("Arial", 14),
              width=20, command=save_update).pack(pady=10)
    tk.Button(root, text="Back", bg="#228B22", fg="white", font=("Arial", 14),
              width=20, command=lambda: dashboard("Admin")).pack(pady=5)


def delete_student_screen():
    clear_screen()

    tk.Label(root, text="Delete Student", font=("Arial", 20, "bold"),
             fg="#006400", bg="white").pack(pady=20)

    tk.Label(root, text="Student ID", fg="#006400",
             font=("Arial", 12, "bold"), bg="white").pack()
    id_entry = tk.Entry(root, font=("Arial", 14), width=25)
    id_entry.pack(pady=5, ipady=5)

    def delete_confirmation():
        try:
            delete_student(int(id_entry.get()))
            messagebox.showinfo("Success", "Student Deleted Successfully!")
            dashboard("Admin")
        except:
            messagebox.showerror("Error", "Failed to delete student")

    tk.Button(root, text="Delete", bg="red", fg="white", font=("Arial", 14),
              width=20, command=delete_confirmation).pack(pady=10)
    tk.Button(root, text="Back", bg="#228B22", fg="white", font=("Arial", 14),
              width=20, command=lambda: dashboard("Admin")).pack(pady=5)


def manage_teachers_screen():
    clear_screen()

    tk.Label(root, text="Manage Teachers", font=("Arial", 20, "bold"),
             fg="#006400", bg="white").pack(pady=20)

    tk.Button(root, text="Add Teacher", bg="#006400", fg="white", font=("Arial", 12),
              width=25, command=add_teacher_screen).pack(pady=5)
    tk.Button(root, text="View Teachers", bg="#006400", fg="white", font=("Arial", 12),
              width=25, command=view_teachers_screen).pack(pady=5)
    tk.Button(root, text="Update Teacher", bg="#006400", fg="white", font=("Arial", 12),
              width=25, command=update_teacher_screen).pack(pady=5)
    tk.Button(root, text="Delete Teacher", bg="#006400", fg="white", font=("Arial", 12),
              width=25, command=delete_teacher_screen).pack(pady=5)
    tk.Button(root, text="Back", bg="#228B22", fg="white", font=("Arial", 14),
              width=20, command=lambda: dashboard("Admin")).pack(pady=10)


def add_teacher_screen():
    clear_screen()

    tk.Label(root, text="Add Teacher", font=("Arial", 20, "bold"),
             fg="#006400", bg="white").pack(pady=20)

    tk.Label(root, text="Name", fg="#006400",
             font=("Arial", 12, "bold"), bg="white").pack()
    name_entry = tk.Entry(root, font=("Arial", 14), width=25)
    name_entry.pack(pady=5, ipady=5)

    tk.Label(root, text="Subject", fg="#006400",
             font=("Arial", 12, "bold"), bg="white").pack()
    subject_entry = tk.Entry(root, font=("Arial", 14), width=25)
    subject_entry.pack(pady=5, ipady=5)

    def save_teacher():
        add_teacher(name_entry.get(), subject_entry.get())
        messagebox.showinfo("Success", "Teacher Added Successfully!")
        manage_teachers_screen()

    tk.Button(root, text="Save", bg="#006400", fg="white", font=("Arial", 14),
              width=20, command=save_teacher).pack(pady=10)
    tk.Button(root, text="Back", bg="#228B22", fg="white", font=("Arial", 14),
              width=20, command=manage_teachers_screen).pack(pady=5)


def view_teachers_screen():
    clear_screen()

    tk.Label(root, text="All Teachers", font=("Arial", 20, "bold"),
             fg="#006400", bg="white").pack(pady=20)

    teachers = get_all_teachers()
    if teachers:
        text = "ID\tName\t\tSubject\n" + "-" * 40 + "\n"
        for teacher in teachers:
            text += f"{teacher[0]}\t{teacher[1]}\t\t{teacher[2]}\n"
        
        text_area = scrolledtext.ScrolledText(root, height=15, width=50, font=("Courier", 10))
        text_area.pack(pady=10)
        text_area.insert(1.0, text)
        text_area.config(state=tk.DISABLED)
    else:
        tk.Label(root, text="No teachers found", fg="#006400",
                 font=("Arial", 12, "bold"), bg="white").pack(pady=20)

    tk.Button(root, text="Back", bg="#228B22", fg="white", font=("Arial", 14),
              width=20, command=manage_teachers_screen).pack(pady=10)


def update_teacher_screen():
    clear_screen()

    tk.Label(root, text="Update Teacher", font=("Arial", 20, "bold"),
             fg="#006400", bg="white").pack(pady=20)

    tk.Label(root, text="Teacher ID", fg="#006400",
             font=("Arial", 12, "bold"), bg="white").pack()
    id_entry = tk.Entry(root, font=("Arial", 14), width=25)
    id_entry.pack(pady=5, ipady=5)

    tk.Label(root, text="Name", fg="#006400",
             font=("Arial", 12, "bold"), bg="white").pack()
    name_entry = tk.Entry(root, font=("Arial", 14), width=25)
    name_entry.pack(pady=5, ipady=5)

    tk.Label(root, text="Subject", fg="#006400",
             font=("Arial", 12, "bold"), bg="white").pack()
    subject_entry = tk.Entry(root, font=("Arial", 14), width=25)
    subject_entry.pack(pady=5, ipady=5)

    def save_update():
        try:
            update_teacher(int(id_entry.get()), name_entry.get(), subject_entry.get())
            messagebox.showinfo("Success", "Teacher Updated Successfully!")
            manage_teachers_screen()
        except:
            messagebox.showerror("Error", "Failed to update teacher")

    tk.Button(root, text="Update", bg="#006400", fg="white", font=("Arial", 14),
              width=20, command=save_update).pack(pady=10)
    tk.Button(root, text="Back", bg="#228B22", fg="white", font=("Arial", 14),
              width=20, command=manage_teachers_screen).pack(pady=5)


def delete_teacher_screen():
    clear_screen()

    tk.Label(root, text="Delete Teacher", font=("Arial", 20, "bold"),
             fg="#006400", bg="white").pack(pady=20)

    tk.Label(root, text="Teacher ID", fg="#006400",
             font=("Arial", 12, "bold"), bg="white").pack()
    id_entry = tk.Entry(root, font=("Arial", 14), width=25)
    id_entry.pack(pady=5, ipady=5)

    def delete_confirmation():
        try:
            delete_teacher(int(id_entry.get()))
            messagebox.showinfo("Success", "Teacher Deleted Successfully!")
            manage_teachers_screen()
        except:
            messagebox.showerror("Error", "Failed to delete teacher")

    tk.Button(root, text="Delete", bg="red", fg="white", font=("Arial", 14),
              width=20, command=delete_confirmation).pack(pady=10)
    tk.Button(root, text="Back", bg="#228B22", fg="white", font=("Arial", 14),
              width=20, command=manage_teachers_screen).pack(pady=5)


def manage_attendance_screen():
    clear_screen()

    tk.Label(root, text="Manage Attendance", font=("Arial", 20, "bold"),
             fg="#006400", bg="white").pack(pady=20)

    tk.Button(root, text="Add Attendance", bg="#006400", fg="white", font=("Arial", 12),
              width=25, command=add_attendance_screen).pack(pady=5)
    tk.Button(root, text="View Attendance", bg="#006400", fg="white", font=("Arial", 12),
              width=25, command=view_attendance_screen).pack(pady=5)
    tk.Button(root, text="Update Attendance", bg="#006400", fg="white", font=("Arial", 12),
              width=25, command=update_attendance_screen).pack(pady=5)
    tk.Button(root, text="Delete Attendance", bg="#006400", fg="white", font=("Arial", 12),
              width=25, command=delete_attendance_screen).pack(pady=5)
    tk.Button(root, text="Back", bg="#228B22", fg="white", font=("Arial", 14),
              width=20, command=lambda: dashboard("Admin")).pack(pady=10)


def add_attendance_screen():
    clear_screen()

    tk.Label(root, text="Add Attendance", font=("Arial", 20, "bold"),
             fg="#006400", bg="white").pack(pady=20)

    tk.Label(root, text="Student ID", fg="#006400",
             font=("Arial", 12, "bold"), bg="white").pack()
    student_id_entry = tk.Entry(root, font=("Arial", 14), width=25)
    student_id_entry.pack(pady=5, ipady=5)

    tk.Label(root, text="Date (YYYY-MM-DD)", fg="#006400",
             font=("Arial", 12, "bold"), bg="white").pack()
    date_entry = tk.Entry(root, font=("Arial", 14), width=25)
    date_entry.pack(pady=5, ipady=5)

    tk.Label(root, text="Status (Present/Absent)", fg="#006400",
             font=("Arial", 12, "bold"), bg="white").pack()
    status_entry = tk.Entry(root, font=("Arial", 14), width=25)
    status_entry.pack(pady=5, ipady=5)

    def save_attendance():
        try:
            add_attendance(int(student_id_entry.get()), date_entry.get(), status_entry.get())
            messagebox.showinfo("Success", "Attendance Added Successfully!")
            manage_attendance_screen()
        except:
            messagebox.showerror("Error", "Failed to add attendance")

    tk.Button(root, text="Save", bg="#006400", fg="white", font=("Arial", 14),
              width=20, command=save_attendance).pack(pady=10)
    tk.Button(root, text="Back", bg="#228B22", fg="white", font=("Arial", 14),
              width=20, command=manage_attendance_screen).pack(pady=5)


def view_attendance_screen():
    clear_screen()

    tk.Label(root, text="View Attendance by Student ID", font=("Arial", 20, "bold"),
             fg="#006400", bg="white").pack(pady=20)

    tk.Label(root, text="Student ID", fg="#006400",
             font=("Arial", 12, "bold"), bg="white").pack()
    student_id_entry = tk.Entry(root, font=("Arial", 14), width=25)
    student_id_entry.pack(pady=5, ipady=5)

    def show_attendance():
        try:
            attendance = get_student_attendance(int(student_id_entry.get()))
            if attendance:
                text = "ID\tDate\t\tStatus\n" + "-" * 40 + "\n"
                for att in attendance:
                    text += f"{att[0]}\t{att[2]}\t\t{att[3]}\n"
                
                text_area = scrolledtext.ScrolledText(root, height=10, width=50, font=("Courier", 10))
                text_area.pack(pady=10)
                text_area.insert(1.0, text)
                text_area.config(state=tk.DISABLED)
            else:
                tk.Label(root, text="No attendance found", fg="#006400",
                         font=("Arial", 12, "bold"), bg="white").pack(pady=20)
        except:
            messagebox.showerror("Error", "Failed to retrieve attendance")

    tk.Button(root, text="View", bg="#006400", fg="white", font=("Arial", 14),
              width=20, command=show_attendance).pack(pady=10)
    tk.Button(root, text="Back", bg="#228B22", fg="white", font=("Arial", 14),
              width=20, command=manage_attendance_screen).pack(pady=5)


def update_attendance_screen():
    clear_screen()

    tk.Label(root, text="Update Attendance", font=("Arial", 20, "bold"),
             fg="#006400", bg="white").pack(pady=20)

    tk.Label(root, text="Attendance ID", fg="#006400",
             font=("Arial", 12, "bold"), bg="white").pack()
    id_entry = tk.Entry(root, font=("Arial", 14), width=25)
    id_entry.pack(pady=5, ipady=5)

    tk.Label(root, text="Status (Present/Absent)", fg="#006400",
             font=("Arial", 12, "bold"), bg="white").pack()
    status_entry = tk.Entry(root, font=("Arial", 14), width=25)
    status_entry.pack(pady=5, ipady=5)

    def save_update():
        try:
            update_attendance(int(id_entry.get()), status_entry.get())
            messagebox.showinfo("Success", "Attendance Updated Successfully!")
            manage_attendance_screen()
        except:
            messagebox.showerror("Error", "Failed to update attendance")

    tk.Button(root, text="Update", bg="#006400", fg="white", font=("Arial", 14),
              width=20, command=save_update).pack(pady=10)
    tk.Button(root, text="Back", bg="#228B22", fg="white", font=("Arial", 14),
              width=20, command=manage_attendance_screen).pack(pady=5)


def delete_attendance_screen():
    clear_screen()

    tk.Label(root, text="Delete Attendance", font=("Arial", 20, "bold"),
             fg="#006400", bg="white").pack(pady=20)

    tk.Label(root, text="Attendance ID", fg="#006400",
             font=("Arial", 12, "bold"), bg="white").pack()
    id_entry = tk.Entry(root, font=("Arial", 14), width=25)
    id_entry.pack(pady=5, ipady=5)

    def delete_confirmation():
        try:
            delete_attendance(int(id_entry.get()))
            messagebox.showinfo("Success", "Attendance Deleted Successfully!")
            manage_attendance_screen()
        except:
            messagebox.showerror("Error", "Failed to delete attendance")

    tk.Button(root, text="Delete", bg="red", fg="white", font=("Arial", 14),
              width=20, command=delete_confirmation).pack(pady=10)
    tk.Button(root, text="Back", bg="#228B22", fg="white", font=("Arial", 14),
              width=20, command=manage_attendance_screen).pack(pady=5)


def manage_fees_screen():
    clear_screen()

    tk.Label(root, text="Manage Fees", font=("Arial", 20, "bold"),
             fg="#006400", bg="white").pack(pady=20)

    tk.Button(root, text="Add Fee", bg="#006400", fg="white", font=("Arial", 12),
              width=25, command=add_fee_screen).pack(pady=5)
    tk.Button(root, text="View Fees", bg="#006400", fg="white", font=("Arial", 12),
              width=25, command=view_fees_screen).pack(pady=5)
    tk.Button(root, text="Update Fee", bg="#006400", fg="white", font=("Arial", 12),
              width=25, command=update_fee_screen).pack(pady=5)
    tk.Button(root, text="Delete Fee", bg="#006400", fg="white", font=("Arial", 12),
              width=25, command=delete_fee_screen).pack(pady=5)
    tk.Button(root, text="Back", bg="#228B22", fg="white", font=("Arial", 14),
              width=20, command=lambda: dashboard("Admin")).pack(pady=10)


def add_fee_screen():
    clear_screen()

    tk.Label(root, text="Add Fee", font=("Arial", 20, "bold"),
             fg="#006400", bg="white").pack(pady=20)

    tk.Label(root, text="Student ID", fg="#006400",
             font=("Arial", 12, "bold"), bg="white").pack()
    student_id_entry = tk.Entry(root, font=("Arial", 14), width=25)
    student_id_entry.pack(pady=5, ipady=5)

    tk.Label(root, text="Amount", fg="#006400",
             font=("Arial", 12, "bold"), bg="white").pack()
    amount_entry = tk.Entry(root, font=("Arial", 14), width=25)
    amount_entry.pack(pady=5, ipady=5)

    tk.Label(root, text="Status (Paid/Pending)", fg="#006400",
             font=("Arial", 12, "bold"), bg="white").pack()
    status_entry = tk.Entry(root, font=("Arial", 14), width=25)
    status_entry.pack(pady=5, ipady=5)

    def save_fee():
        try:
            add_fee(int(student_id_entry.get()), float(amount_entry.get()), status_entry.get())
            messagebox.showinfo("Success", "Fee Added Successfully!")
            manage_fees_screen()
        except:
            messagebox.showerror("Error", "Failed to add fee")

    tk.Button(root, text="Save", bg="#006400", fg="white", font=("Arial", 14),
              width=20, command=save_fee).pack(pady=10)
    tk.Button(root, text="Back", bg="#228B22", fg="white", font=("Arial", 14),
              width=20, command=manage_fees_screen).pack(pady=5)


def view_fees_screen():
    clear_screen()

    tk.Label(root, text="View Fees by Student ID", font=("Arial", 20, "bold"),
             fg="#006400", bg="white").pack(pady=20)

    tk.Label(root, text="Student ID", fg="#006400",
             font=("Arial", 12, "bold"), bg="white").pack()
    student_id_entry = tk.Entry(root, font=("Arial", 14), width=25)
    student_id_entry.pack(pady=5, ipady=5)

    def show_fees():
        try:
            fees = get_student_fees(int(student_id_entry.get()))
            if fees:
                text = "ID\tAmount\t\tStatus\n" + "-" * 40 + "\n"
                for fee in fees:
                    text += f"{fee[0]}\t{fee[2]}\t\t{fee[3]}\n"
                
                text_area = scrolledtext.ScrolledText(root, height=10, width=50, font=("Courier", 10))
                text_area.pack(pady=10)
                text_area.insert(1.0, text)
                text_area.config(state=tk.DISABLED)
            else:
                tk.Label(root, text="No fees found", fg="#006400",
                         font=("Arial", 12, "bold"), bg="white").pack(pady=20)
        except:
            messagebox.showerror("Error", "Failed to retrieve fees")

    tk.Button(root, text="View", bg="#006400", fg="white", font=("Arial", 14),
              width=20, command=show_fees).pack(pady=10)
    tk.Button(root, text="Back", bg="#228B22", fg="white", font=("Arial", 14),
              width=20, command=manage_fees_screen).pack(pady=5)


def update_fee_screen():
    clear_screen()

    tk.Label(root, text="Update Fee", font=("Arial", 20, "bold"),
             fg="#006400", bg="white").pack(pady=20)

    tk.Label(root, text="Fee ID", fg="#006400",
             font=("Arial", 12, "bold"), bg="white").pack()
    id_entry = tk.Entry(root, font=("Arial", 14), width=25)
    id_entry.pack(pady=5, ipady=5)

    tk.Label(root, text="Amount", fg="#006400",
             font=("Arial", 12, "bold"), bg="white").pack()
    amount_entry = tk.Entry(root, font=("Arial", 14), width=25)
    amount_entry.pack(pady=5, ipady=5)

    tk.Label(root, text="Status (Paid/Pending)", fg="#006400",
             font=("Arial", 12, "bold"), bg="white").pack()
    status_entry = tk.Entry(root, font=("Arial", 14), width=25)
    status_entry.pack(pady=5, ipady=5)

    def save_update():
        try:
            update_fee(int(id_entry.get()), float(amount_entry.get()), status_entry.get())
            messagebox.showinfo("Success", "Fee Updated Successfully!")
            manage_fees_screen()
        except:
            messagebox.showerror("Error", "Failed to update fee")

    tk.Button(root, text="Update", bg="#006400", fg="white", font=("Arial", 14),
              width=20, command=save_update).pack(pady=10)
    tk.Button(root, text="Back", bg="#228B22", fg="white", font=("Arial", 14),
              width=20, command=manage_fees_screen).pack(pady=5)


def delete_fee_screen():
    clear_screen()

    tk.Label(root, text="Delete Fee", font=("Arial", 20, "bold"),
             fg="#006400", bg="white").pack(pady=20)

    tk.Label(root, text="Fee ID", fg="#006400",
             font=("Arial", 12, "bold"), bg="white").pack()
    id_entry = tk.Entry(root, font=("Arial", 14), width=25)
    id_entry.pack(pady=5, ipady=5)

    def delete_confirmation():
        try:
            delete_fee(int(id_entry.get()))
            messagebox.showinfo("Success", "Fee Deleted Successfully!")
            manage_fees_screen()
        except:
            messagebox.showerror("Error", "Failed to delete fee")

    tk.Button(root, text="Delete", bg="red", fg="white", font=("Arial", 14),
              width=20, command=delete_confirmation).pack(pady=10)
    tk.Button(root, text="Back", bg="#228B22", fg="white", font=("Arial", 14),
              width=20, command=manage_fees_screen).pack(pady=5)


def manage_performance_screen():
    clear_screen()

    tk.Label(root, text="Manage Performance", font=("Arial", 20, "bold"),
             fg="#006400", bg="white").pack(pady=20)

    tk.Button(root, text="Add Performance", bg="#006400", fg="white", font=("Arial", 12),
              width=25, command=add_performance_screen).pack(pady=5)
    tk.Button(root, text="View Performance", bg="#006400", fg="white", font=("Arial", 12),
              width=25, command=view_performance_screen).pack(pady=5)
    tk.Button(root, text="Update Performance", bg="#006400", fg="white", font=("Arial", 12),
              width=25, command=update_performance_screen).pack(pady=5)
    tk.Button(root, text="Delete Performance", bg="#006400", fg="white", font=("Arial", 12),
              width=25, command=delete_performance_screen).pack(pady=5)
    tk.Button(root, text="Back", bg="#228B22", fg="white", font=("Arial", 14),
              width=20, command=lambda: dashboard("Admin")).pack(pady=10)


def add_performance_screen():
    clear_screen()

    tk.Label(root, text="Add Performance", font=("Arial", 20, "bold"),
             fg="#006400", bg="white").pack(pady=20)

    tk.Label(root, text="Student ID", fg="#006400",
             font=("Arial", 12, "bold"), bg="white").pack()
    student_id_entry = tk.Entry(root, font=("Arial", 14), width=25)
    student_id_entry.pack(pady=5, ipady=5)

    tk.Label(root, text="Subject", fg="#006400",
             font=("Arial", 12, "bold"), bg="white").pack()
    subject_entry = tk.Entry(root, font=("Arial", 14), width=25)
    subject_entry.pack(pady=5, ipady=5)

    tk.Label(root, text="Marks (0-100)", fg="#006400",
             font=("Arial", 12, "bold"), bg="white").pack()
    marks_entry = tk.Entry(root, font=("Arial", 14), width=25)
    marks_entry.pack(pady=5, ipady=5)

    def save_performance():
        try:
            add_performance(int(student_id_entry.get()), subject_entry.get(), int(marks_entry.get()))
            messagebox.showinfo("Success", "Performance Added Successfully!")
            manage_performance_screen()
        except:
            messagebox.showerror("Error", "Failed to add performance")

    tk.Button(root, text="Save", bg="#006400", fg="white", font=("Arial", 14),
              width=20, command=save_performance).pack(pady=10)
    tk.Button(root, text="Back", bg="#228B22", fg="white", font=("Arial", 14),
              width=20, command=manage_performance_screen).pack(pady=5)


def view_performance_screen():
    clear_screen()

    tk.Label(root, text="View Performance by Student ID", font=("Arial", 20, "bold"),
             fg="#006400", bg="white").pack(pady=20)

    tk.Label(root, text="Student ID", fg="#006400",
             font=("Arial", 12, "bold"), bg="white").pack()
    student_id_entry = tk.Entry(root, font=("Arial", 14), width=25)
    student_id_entry.pack(pady=5, ipady=5)

    def show_performance():
        try:
            performance = get_student_performance(int(student_id_entry.get()))
            if performance:
                text = "ID\tSubject\t\tMarks\tGrade\n" + "-" * 50 + "\n"
                for perf in performance:
                    # Calculate grade based on marks
                    marks = perf[3]
                    if marks >= 90:
                        grade = 'A'
                    elif marks >= 80:
                        grade = 'B'
                    elif marks >= 70:
                        grade = 'C'
                    elif marks >= 60:
                        grade = 'D'
                    else:
                        grade = 'F'
                    text += f"{perf[0]}\t{perf[2]}\t\t{marks}\t{grade}\n"
                
                text_area = scrolledtext.ScrolledText(root, height=10, width=50, font=("Courier", 10))
                text_area.pack(pady=10)
                text_area.insert(1.0, text)
                text_area.config(state=tk.DISABLED)
            else:
                tk.Label(root, text="No performance records found", fg="#006400",
                         font=("Arial", 12, "bold"), bg="white").pack(pady=20)
        except:
            messagebox.showerror("Error", "Failed to retrieve performance")

    tk.Button(root, text="View", bg="#006400", fg="white", font=("Arial", 14),
              width=20, command=show_performance).pack(pady=10)
    tk.Button(root, text="Back", bg="#228B22", fg="white", font=("Arial", 14),
              width=20, command=manage_performance_screen).pack(pady=5)


def update_performance_screen():
    clear_screen()

    tk.Label(root, text="Update Performance", font=("Arial", 20, "bold"),
             fg="#006400", bg="white").pack(pady=20)

    tk.Label(root, text="Performance ID", fg="#006400",
             font=("Arial", 12, "bold"), bg="white").pack()
    id_entry = tk.Entry(root, font=("Arial", 14), width=25)
    id_entry.pack(pady=5, ipady=5)

    tk.Label(root, text="Marks (0-100)", fg="#006400",
             font=("Arial", 12, "bold"), bg="white").pack()
    marks_entry = tk.Entry(root, font=("Arial", 14), width=25)
    marks_entry.pack(pady=5, ipady=5)

    def save_update():
        try:
            update_performance(int(id_entry.get()), int(marks_entry.get()))
            messagebox.showinfo("Success", "Performance Updated Successfully!")
            manage_performance_screen()
        except:
            messagebox.showerror("Error", "Failed to update performance")

    tk.Button(root, text="Update", bg="#006400", fg="white", font=("Arial", 14),
              width=20, command=save_update).pack(pady=10)
    tk.Button(root, text="Back", bg="#228B22", fg="white", font=("Arial", 14),
              width=20, command=manage_performance_screen).pack(pady=5)


def delete_performance_screen():
    clear_screen()

    tk.Label(root, text="Delete Performance", font=("Arial", 20, "bold"),
             fg="#006400", bg="white").pack(pady=20)

    tk.Label(root, text="Performance ID", fg="#006400",
             font=("Arial", 12, "bold"), bg="white").pack()
    id_entry = tk.Entry(root, font=("Arial", 14), width=25)
    id_entry.pack(pady=5, ipady=5)

    def delete_confirmation():
        try:
            delete_performance(int(id_entry.get()))
            messagebox.showinfo("Success", "Performance Deleted Successfully!")
            manage_performance_screen()
        except:
            messagebox.showerror("Error", "Failed to delete performance")

    tk.Button(root, text="Delete", bg="red", fg="white", font=("Arial", 14),
              width=20, command=delete_confirmation).pack(pady=10)
    tk.Button(root, text="Back", bg="#228B22", fg="white", font=("Arial", 14),
              width=20, command=manage_performance_screen).pack(pady=5)


login_screen()
root.mainloop()
