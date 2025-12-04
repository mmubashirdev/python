"""
School Management System GUI
Built with Tkinter for a comprehensive school management experience
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from datetime import datetime, date
from models import School, Student, Teacher, Performance, Attendance, Fee


class SchoolManagementGUI:
    """Main GUI application for School Management System"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("School Management System")
        self.root.geometry("900x700")
        self.root.resizable(False, False)
        
        # Initialize database
        try:
            School.initialize()
        except Exception as e:
            messagebox.showerror("Database Error", f"Failed to initialize database: {e}")
        
        self.current_user = None
        self.show_login_screen()
    
    def clear_screen(self):
        """Clear all widgets from root window"""
        for widget in self.root.winfo_children():
            widget.destroy()
    
    # ===== LOGIN SCREEN =====
    def show_login_screen(self):
        """Display login screen"""
        self.clear_screen()
        
        frame = ttk.Frame(self.root, padding="20")
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        ttk.Label(frame, text="School Management System", font=("Arial", 24, "bold")).pack(pady=20)
        ttk.Label(frame, text="Student Login", font=("Arial", 16)).pack(pady=10)
        
        ttk.Label(frame, text="Student Name:").pack()
        name_var = tk.StringVar()
        ttk.Entry(frame, textvariable=name_var, width=30).pack(pady=5)
        
        ttk.Label(frame, text="Password:").pack()
        pass_var = tk.StringVar()
        ttk.Entry(frame, textvariable=pass_var, show="*", width=30).pack(pady=5)
        
        def login():
            name = name_var.get().strip()
            password = pass_var.get().strip()
            if not name or not password:
                messagebox.showwarning("Input Error", "Please enter name and password")
                return
            
            if Student.verify_login(name, password):
                self.current_user = Student.get_by_name(name)
                self.show_student_dashboard()
            else:
                messagebox.showerror("Login Failed", "Invalid credentials")
        
        ttk.Button(frame, text="Login", command=login, width=20).pack(pady=10)
        ttk.Button(frame, text="Add New Student", command=self.show_add_student_screen, width=20).pack(pady=5)
        ttk.Button(frame, text="Admin Panel", command=self.show_admin_login, width=20).pack(pady=5)
    
    def show_admin_login(self):
        """Show admin login screen"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Admin Login")
        dialog.geometry("300x200")
        
        ttk.Label(dialog, text="Admin Password:", font=("Arial", 12)).pack(pady=10)
        pass_var = tk.StringVar()
        ttk.Entry(dialog, textvariable=pass_var, show="*", width=25).pack(pady=5)
        
        def verify_admin():
            if pass_var.get() == "admin123":
                dialog.destroy()
                self.show_admin_dashboard()
            else:
                messagebox.showerror("Error", "Invalid admin password")
        
        ttk.Button(dialog, text="Login", command=verify_admin).pack(pady=10)
    
    # ===== STUDENT DASHBOARD =====
    def show_student_dashboard(self):
        """Show student dashboard"""
        self.clear_screen()
        
        ttk.Label(self.root, text=f"Welcome, {self.current_user.name}!", 
                 font=("Arial", 18, "bold")).pack(pady=20)
        
        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=20)
        
        ttk.Button(button_frame, text="View My Performance", 
                  command=self.show_student_performance, width=25).pack(pady=5)
        ttk.Button(button_frame, text="View My Attendance", 
                  command=self.show_student_attendance, width=25).pack(pady=5)
        ttk.Button(button_frame, text="View My Fees", 
                  command=self.show_student_fees, width=25).pack(pady=5)
        ttk.Button(button_frame, text="Generate Report", 
                  command=self.show_student_report, width=25).pack(pady=5)
        ttk.Button(button_frame, text="Logout", 
                  command=self.show_login_screen, width=25).pack(pady=20)
    
    def show_student_performance(self):
        """Show student's performance records"""
        self.clear_screen()
        
        ttk.Label(self.root, text="My Academic Performance", font=("Arial", 16, "bold")).pack(pady=10)
        
        # Create treeview
        columns = ("Subject", "Marks", "Grade")
        tree = ttk.Treeview(self.root, columns=columns, height=15)
        tree.column("#0", width=0)
        tree.heading("#0", text="")
        
        for col in columns:
            tree.column(col, anchor=tk.CENTER, width=250)
            tree.heading(col, text=col)
        
        performances = Performance.get_by_student(self.current_user.id)
        for perf in performances:
            tree.insert("", tk.END, text="", values=(perf.subject, perf.marks, perf.get_grade()))
        
        tree.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        
        # Stats frame
        stats_frame = ttk.Frame(self.root)
        stats_frame.pack(pady=10)
        ttk.Label(stats_frame, text=f"GPA: {self.current_user.get_gpa()}", 
                 font=("Arial", 12, "bold")).pack(side=tk.LEFT, padx=20)
        
        ttk.Button(self.root, text="Back", command=self.show_student_dashboard).pack(pady=10)
    
    def show_student_attendance(self):
        """Show student's attendance"""
        self.clear_screen()
        
        ttk.Label(self.root, text="My Attendance", font=("Arial", 16, "bold")).pack(pady=10)
        
        columns = ("Date", "Status")
        tree = ttk.Treeview(self.root, columns=columns, height=15)
        tree.column("#0", width=0)
        
        for col in columns:
            tree.column(col, anchor=tk.CENTER, width=250)
            tree.heading(col, text=col)
        
        attendances = Attendance.get_by_student(self.current_user.id)
        for att in attendances:
            tree.insert("", tk.END, text="", values=(att.date, att.status))
        
        tree.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        
        ttk.Button(self.root, text="Back", command=self.show_student_dashboard).pack(pady=10)
    
    def show_student_fees(self):
        """Show student's fees"""
        self.clear_screen()
        
        ttk.Label(self.root, text="My Fees", font=("Arial", 16, "bold")).pack(pady=10)
        
        columns = ("Amount", "Status")
        tree = ttk.Treeview(self.root, columns=columns, height=15)
        tree.column("#0", width=0)
        
        for col in columns:
            tree.column(col, anchor=tk.CENTER, width=250)
            tree.heading(col, text=col)
        
        fees = Fee.get_by_student(self.current_user.id)
        for fee in fees:
            tree.insert("", tk.END, text="", values=(fee.amount, fee.status))
        
        tree.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        
        ttk.Button(self.root, text="Back", command=self.show_student_dashboard).pack(pady=10)
    
    def show_student_report(self):
        """Generate and display student performance report"""
        self.clear_screen()
        
        report = School.generate_performance_report(self.current_user.id)
        if not report:
            messagebox.showerror("Error", "Cannot generate report")
            return
        
        ttk.Label(self.root, text="Performance Report", font=("Arial", 16, "bold")).pack(pady=10)
        
        # Use scrolledtext to display report
        report_text = scrolledtext.ScrolledText(self.root, width=100, height=25, wrap=tk.WORD)
        report_text.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        
        report_content = f"""
{'='*80}
                    STUDENT PERFORMANCE REPORT
{'='*80}

Student Information:
  Name: {report['student'].name}
  Grade: {report['student'].grade}
  Report Date: {report['report_date']}

Academic Performance:
  Average Marks: {report['avg_marks']}
  GPA: {report['gpa']}

Attendance:
  Total Days: {report['attendance']['total_days']}
  Days Present: {report['attendance']['present_days']}
  Attendance Percentage: {report['attendance']['percentage']}%

Subject-wise Performance:
"""
        for perf in report['performances']:
            report_content += f"\n  {perf.subject}: {perf.marks} ({perf.get_grade()})"
        
        report_content += f"\n\nFinancial Status:\n"
        report_content += f"  Total Fees: Rs. {report['fees']['total']}\n"
        report_content += f"  Paid: Rs. {report['fees']['paid']}\n"
        report_content += f"  Pending: Rs. {report['fees']['pending']}\n"
        report_content += f"\n{'='*80}\n"
        
        report_text.insert(tk.END, report_content)
        report_text.config(state=tk.DISABLED)
        
        ttk.Button(self.root, text="Back", command=self.show_student_dashboard).pack(pady=10)
    
    # ===== ADD STUDENT SCREEN =====
    def show_add_student_screen(self):
        """Show screen to add new student"""
        self.clear_screen()
        
        ttk.Label(self.root, text="Register New Student", font=("Arial", 16, "bold")).pack(pady=20)
        
        frame = ttk.Frame(self.root, padding="20")
        frame.pack(pady=20)
        
        ttk.Label(frame, text="Name:").grid(row=0, column=0, sticky=tk.W, pady=5)
        name_var = tk.StringVar()
        ttk.Entry(frame, textvariable=name_var, width=30).grid(row=0, column=1, pady=5)
        
        ttk.Label(frame, text="Grade:").grid(row=1, column=0, sticky=tk.W, pady=5)
        grade_var = tk.StringVar()
        ttk.Entry(frame, textvariable=grade_var, width=30).grid(row=1, column=1, pady=5)
        
        ttk.Label(frame, text="Password:").grid(row=2, column=0, sticky=tk.W, pady=5)
        pass_var = tk.StringVar()
        ttk.Entry(frame, textvariable=pass_var, show="*", width=30).grid(row=2, column=1, pady=5)
        
        def save_student():
            name = name_var.get().strip()
            grade = grade_var.get().strip()
            password = pass_var.get().strip()
            
            if not name or not grade or not password:
                messagebox.showwarning("Input Error", "All fields are required")
                return
            
            try:
                School.add_student(name, grade, password)
                messagebox.showinfo("Success", "Student registered successfully")
                self.show_login_screen()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to register: {e}")
        
        ttk.Button(frame, text="Register", command=save_student).grid(row=3, column=0, columnspan=2, pady=20)
        ttk.Button(self.root, text="Back", command=self.show_login_screen).pack(pady=10)
    
    # ===== ADMIN DASHBOARD =====
    def show_admin_dashboard(self):
        """Show admin dashboard"""
        self.clear_screen()
        
        ttk.Label(self.root, text="Admin Dashboard", font=("Arial", 18, "bold")).pack(pady=20)
        
        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=20)
        
        ttk.Button(button_frame, text="Manage Students", command=self.show_manage_students, width=25).pack(pady=5)
        ttk.Button(button_frame, text="Manage Teachers", command=self.show_manage_teachers, width=25).pack(pady=5)
        ttk.Button(button_frame, text="Manage Attendance", command=self.show_manage_attendance, width=25).pack(pady=5)
        ttk.Button(button_frame, text="Manage Fees", command=self.show_manage_fees, width=25).pack(pady=5)
        ttk.Button(button_frame, text="Manage Performance", command=self.show_manage_performance, width=25).pack(pady=5)
        ttk.Button(button_frame, text="Logout", command=self.show_login_screen, width=25).pack(pady=20)
    
    # ===== MANAGE STUDENTS =====
    def show_manage_students(self):
        """Manage students"""
        self.clear_screen()
        
        ttk.Label(self.root, text="Manage Students", font=("Arial", 16, "bold")).pack(pady=10)
        
        # Buttons
        btn_frame = ttk.Frame(self.root)
        btn_frame.pack(pady=10)
        ttk.Button(btn_frame, text="Add Student", command=self.show_add_student_admin).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Refresh", command=self.show_manage_students).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Back", command=self.show_admin_dashboard).pack(side=tk.LEFT, padx=5)
        
        # Treeview
        columns = ("ID", "Name", "Grade", "Password")
        tree = ttk.Treeview(self.root, columns=columns, height=15)
        tree.column("#0", width=0)
        
        for col in columns:
            tree.column(col, anchor=tk.CENTER, width=150)
            tree.heading(col, text=col)
        
        students = School.get_all_students()
        for student in students:
            tree.insert("", tk.END, text="", values=(student.id, student.name, student.grade, "***"))
        
        tree.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        
        def delete_student():
            selected = tree.selection()
            if not selected:
                messagebox.showwarning("Warning", "Please select a student to delete")
                return
            
            item = tree.item(selected[0])
            student_id = item['values'][0]
            
            if messagebox.askyesno("Confirm", "Delete this student?"):
                School.delete_student(student_id)
                messagebox.showinfo("Success", "Student deleted")
                self.show_manage_students()
        
        ttk.Button(self.root, text="Delete Selected", command=delete_student).pack(pady=5)
    
    def show_add_student_admin(self):
        """Add student from admin panel"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Add Student")
        dialog.geometry("400x250")
        
        ttk.Label(dialog, text="Student Name:").pack(pady=5)
        name_var = tk.StringVar()
        ttk.Entry(dialog, textvariable=name_var, width=30).pack(pady=5)
        
        ttk.Label(dialog, text="Grade:").pack(pady=5)
        grade_var = tk.StringVar()
        ttk.Entry(dialog, textvariable=grade_var, width=30).pack(pady=5)
        
        ttk.Label(dialog, text="Password:").pack(pady=5)
        pass_var = tk.StringVar()
        ttk.Entry(dialog, textvariable=pass_var, show="*", width=30).pack(pady=5)
        
        def save():
            name = name_var.get().strip()
            grade = grade_var.get().strip()
            password = pass_var.get().strip()
            
            if not name or not grade or not password:
                messagebox.showwarning("Input Error", "All fields required")
                return
            
            try:
                School.add_student(name, grade, password)
                messagebox.showinfo("Success", "Student added successfully")
                dialog.destroy()
                self.show_manage_students()
            except Exception as e:
                messagebox.showerror("Error", f"Failed: {e}")
        
        ttk.Button(dialog, text="Save", command=save).pack(pady=10)
    
    # ===== MANAGE TEACHERS =====
    def show_manage_teachers(self):
        """Manage teachers"""
        self.clear_screen()
        
        ttk.Label(self.root, text="Manage Teachers", font=("Arial", 16, "bold")).pack(pady=10)
        
        btn_frame = ttk.Frame(self.root)
        btn_frame.pack(pady=10)
        ttk.Button(btn_frame, text="Add Teacher", command=self.show_add_teacher).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Refresh", command=self.show_manage_teachers).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Back", command=self.show_admin_dashboard).pack(side=tk.LEFT, padx=5)
        
        columns = ("ID", "Name", "Subject")
        tree = ttk.Treeview(self.root, columns=columns, height=15)
        tree.column("#0", width=0)
        
        for col in columns:
            tree.column(col, anchor=tk.CENTER, width=200)
            tree.heading(col, text=col)
        
        teachers = School.get_all_teachers()
        for teacher in teachers:
            tree.insert("", tk.END, text="", values=(teacher.id, teacher.name, teacher.subject))
        
        tree.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        
        def delete_teacher():
            selected = tree.selection()
            if not selected:
                messagebox.showwarning("Warning", "Please select a teacher to delete")
                return
            
            item = tree.item(selected[0])
            teacher_id = item['values'][0]
            
            if messagebox.askyesno("Confirm", "Delete this teacher?"):
                School.delete_teacher(teacher_id)
                messagebox.showinfo("Success", "Teacher deleted")
                self.show_manage_teachers()
        
        ttk.Button(self.root, text="Delete Selected", command=delete_teacher).pack(pady=5)
    
    def show_add_teacher(self):
        """Add teacher"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Add Teacher")
        dialog.geometry("400x200")
        
        ttk.Label(dialog, text="Teacher Name:").pack(pady=5)
        name_var = tk.StringVar()
        ttk.Entry(dialog, textvariable=name_var, width=30).pack(pady=5)
        
        ttk.Label(dialog, text="Subject:").pack(pady=5)
        subject_var = tk.StringVar()
        ttk.Entry(dialog, textvariable=subject_var, width=30).pack(pady=5)
        
        def save():
            name = name_var.get().strip()
            subject = subject_var.get().strip()
            
            if not name or not subject:
                messagebox.showwarning("Input Error", "All fields required")
                return
            
            try:
                School.add_teacher(name, subject)
                messagebox.showinfo("Success", "Teacher added successfully")
                dialog.destroy()
                self.show_manage_teachers()
            except Exception as e:
                messagebox.showerror("Error", f"Failed: {e}")
        
        ttk.Button(dialog, text="Save", command=save).pack(pady=10)
    
    # ===== MANAGE ATTENDANCE =====
    def show_manage_attendance(self):
        """Manage attendance"""
        self.clear_screen()
        
        ttk.Label(self.root, text="Manage Attendance", font=("Arial", 16, "bold")).pack(pady=10)
        
        btn_frame = ttk.Frame(self.root)
        btn_frame.pack(pady=10)
        ttk.Button(btn_frame, text="Add Attendance", command=self.show_add_attendance).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Refresh", command=self.show_manage_attendance).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Back", command=self.show_admin_dashboard).pack(side=tk.LEFT, padx=5)
        
        columns = ("ID", "Student", "Date", "Status")
        tree = ttk.Treeview(self.root, columns=columns, height=15)
        tree.column("#0", width=0)
        
        for col in columns:
            tree.column(col, anchor=tk.CENTER, width=180)
            tree.heading(col, text=col)
        
        students = School.get_all_students()
        for student in students:
            attendances = Attendance.get_by_student(student.id)
            for att in attendances:
                tree.insert("", tk.END, text="", values=(att.id, student.name, att.date, att.status))
        
        tree.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
    
    def show_add_attendance(self):
        """Add attendance"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Add Attendance")
        dialog.geometry("400x250")
        
        ttk.Label(dialog, text="Student:").pack(pady=5)
        student_var = tk.StringVar()
        students = School.get_all_students()
        student_names = [s.name for s in students]
        ttk.Combobox(dialog, textvariable=student_var, values=student_names, width=27).pack(pady=5)
        
        ttk.Label(dialog, text="Date (YYYY-MM-DD):").pack(pady=5)
        date_var = tk.StringVar(value=str(date.today()))
        ttk.Entry(dialog, textvariable=date_var, width=30).pack(pady=5)
        
        ttk.Label(dialog, text="Status:").pack(pady=5)
        status_var = tk.StringVar()
        ttk.Combobox(dialog, textvariable=status_var, values=["Present", "Absent"], width=27).pack(pady=5)
        
        def save():
            student_name = student_var.get().strip()
            att_date = date_var.get().strip()
            status = status_var.get().strip()
            
            if not student_name or not att_date or not status:
                messagebox.showwarning("Input Error", "All fields required")
                return
            
            student = Student.get_by_name(student_name)
            if not student:
                messagebox.showerror("Error", "Student not found")
                return
            
            try:
                att = Attendance(student.id, att_date, status)
                att.save()
                messagebox.showinfo("Success", "Attendance recorded")
                dialog.destroy()
                self.show_manage_attendance()
            except Exception as e:
                messagebox.showerror("Error", f"Failed: {e}")
        
        ttk.Button(dialog, text="Save", command=save).pack(pady=10)
    
    # ===== MANAGE FEES =====
    def show_manage_fees(self):
        """Manage fees"""
        self.clear_screen()
        
        ttk.Label(self.root, text="Manage Fees", font=("Arial", 16, "bold")).pack(pady=10)
        
        btn_frame = ttk.Frame(self.root)
        btn_frame.pack(pady=10)
        ttk.Button(btn_frame, text="Add Fee", command=self.show_add_fee).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Refresh", command=self.show_manage_fees).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Back", command=self.show_admin_dashboard).pack(side=tk.LEFT, padx=5)
        
        columns = ("ID", "Student", "Amount", "Status")
        tree = ttk.Treeview(self.root, columns=columns, height=15)
        tree.column("#0", width=0)
        
        for col in columns:
            tree.column(col, anchor=tk.CENTER, width=180)
            tree.heading(col, text=col)
        
        students = School.get_all_students()
        for student in students:
            fees = Fee.get_by_student(student.id)
            for fee in fees:
                tree.insert("", tk.END, text="", values=(fee.id, student.name, fee.amount, fee.status))
        
        tree.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
    
    def show_add_fee(self):
        """Add fee"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Add Fee")
        dialog.geometry("400x250")
        
        ttk.Label(dialog, text="Student:").pack(pady=5)
        student_var = tk.StringVar()
        students = School.get_all_students()
        student_names = [s.name for s in students]
        ttk.Combobox(dialog, textvariable=student_var, values=student_names, width=27).pack(pady=5)
        
        ttk.Label(dialog, text="Amount:").pack(pady=5)
        amount_var = tk.StringVar()
        ttk.Entry(dialog, textvariable=amount_var, width=30).pack(pady=5)
        
        ttk.Label(dialog, text="Status:").pack(pady=5)
        status_var = tk.StringVar()
        ttk.Combobox(dialog, textvariable=status_var, values=["Paid", "Pending"], width=27).pack(pady=5)
        
        def save():
            student_name = student_var.get().strip()
            amount_str = amount_var.get().strip()
            status = status_var.get().strip()
            
            if not student_name or not amount_str or not status:
                messagebox.showwarning("Input Error", "All fields required")
                return
            
            try:
                amount = float(amount_str)
            except ValueError:
                messagebox.showerror("Error", "Invalid amount")
                return
            
            student = Student.get_by_name(student_name)
            if not student:
                messagebox.showerror("Error", "Student not found")
                return
            
            try:
                fee = Fee(student.id, amount, status)
                fee.save()
                messagebox.showinfo("Success", "Fee recorded")
                dialog.destroy()
                self.show_manage_fees()
            except Exception as e:
                messagebox.showerror("Error", f"Failed: {e}")
        
        ttk.Button(dialog, text="Save", command=save).pack(pady=10)
    
    # ===== MANAGE PERFORMANCE =====
    def show_manage_performance(self):
        """Manage performance"""
        self.clear_screen()
        
        ttk.Label(self.root, text="Manage Performance", font=("Arial", 16, "bold")).pack(pady=10)
        
        btn_frame = ttk.Frame(self.root)
        btn_frame.pack(pady=10)
        ttk.Button(btn_frame, text="Add Performance", command=self.show_add_performance).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Refresh", command=self.show_manage_performance).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Back", command=self.show_admin_dashboard).pack(side=tk.LEFT, padx=5)
        
        columns = ("ID", "Student", "Subject", "Marks", "Grade")
        tree = ttk.Treeview(self.root, columns=columns, height=15)
        tree.column("#0", width=0)
        
        for col in columns:
            tree.column(col, anchor=tk.CENTER, width=140)
            tree.heading(col, text=col)
        
        students = School.get_all_students()
        for student in students:
            performances = Performance.get_by_student(student.id)
            for perf in performances:
                tree.insert("", tk.END, text="", values=(perf.id, student.name, perf.subject, perf.marks, perf.get_grade()))
        
        tree.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
    
    def show_add_performance(self):
        """Add performance"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Add Performance")
        dialog.geometry("400x250")
        
        ttk.Label(dialog, text="Student:").pack(pady=5)
        student_var = tk.StringVar()
        students = School.get_all_students()
        student_names = [s.name for s in students]
        ttk.Combobox(dialog, textvariable=student_var, values=student_names, width=27).pack(pady=5)
        
        ttk.Label(dialog, text="Subject:").pack(pady=5)
        subject_var = tk.StringVar()
        ttk.Entry(dialog, textvariable=subject_var, width=30).pack(pady=5)
        
        ttk.Label(dialog, text="Marks (0-100):").pack(pady=5)
        marks_var = tk.StringVar()
        ttk.Entry(dialog, textvariable=marks_var, width=30).pack(pady=5)
        
        def save():
            student_name = student_var.get().strip()
            subject = subject_var.get().strip()
            marks_str = marks_var.get().strip()
            
            if not student_name or not subject or not marks_str:
                messagebox.showwarning("Input Error", "All fields required")
                return
            
            try:
                marks = int(marks_str)
                if marks < 0 or marks > 100:
                    raise ValueError
            except ValueError:
                messagebox.showerror("Error", "Marks must be between 0 and 100")
                return
            
            student = Student.get_by_name(student_name)
            if not student:
                messagebox.showerror("Error", "Student not found")
                return
            
            try:
                perf = Performance(student.id, subject, marks)
                perf.save()
                messagebox.showinfo("Success", "Performance recorded")
                dialog.destroy()
                self.show_manage_performance()
            except Exception as e:
                messagebox.showerror("Error", f"Failed: {e}")
        
        ttk.Button(dialog, text="Save", command=save).pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = SchoolManagementGUI(root)
    root.mainloop()

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
