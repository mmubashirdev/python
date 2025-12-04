"""
Object-Oriented Models for School Management System
This module defines the core classes for managing students, teachers, and performance
"""

import ERP_pyodbc as db
from datetime import datetime


class Student:
    """Class to represent a Student"""
    
    def __init__(self, name, grade, password, student_id=None):
        self.id = student_id
        self.name = name
        self.grade = grade
        self.password = password
    
    def save(self):
        """Save student to database"""
        if self.id is None:
            db.add_student(self.name, self.grade, self.password)
        else:
            db.update_student(self.id, self.name, self.grade, self.password)
    
    def delete(self):
        """Delete student from database"""
        if self.id:
            db.delete_student(self.id)
    
    def get_gpa(self):
        """Get student's GPA"""
        return db.calculate_student_gpa(self.id)
    
    def get_attendance(self):
        """Get student's attendance records"""
        return db.get_student_attendance(self.id)
    
    def get_fees(self):
        """Get student's fee records"""
        return db.get_student_fees(self.id)
    
    def get_performance(self):
        """Get student's performance records"""
        return db.get_student_performance(self.id)
    
    @staticmethod
    def get_all():
        """Get all students from database"""
        students = db.get_all_students()
        return [Student(row[1], row[2], row[3], row[0]) for row in students] if students else []
    
    @staticmethod
    def get_by_id(student_id):
        """Get student by ID"""
        row = db.get_student(student_id)
        if row:
            return Student(row[1], row[2], row[3], row[0])
        return None
    
    @staticmethod
    def verify_login(name, password):
        """Verify student login credentials"""
        return db.verify_login(name, password)
    
    @staticmethod
    def get_by_name(name):
        """Get student by name"""
        row = db.get_student_by_name(name)
        if row:
            return Student(row[1], row[2], row[3], row[0])
        return None
    
    def __repr__(self):
        return f"Student({self.id}, {self.name}, {self.grade})"


class Teacher:
    """Class to represent a Teacher"""
    
    def __init__(self, name, subject, teacher_id=None):
        self.id = teacher_id
        self.name = name
        self.subject = subject
    
    def save(self):
        """Save teacher to database"""
        if self.id is None:
            db.add_teacher(self.name, self.subject)
        else:
            db.update_teacher(self.id, self.name, self.subject)
    
    def delete(self):
        """Delete teacher from database"""
        if self.id:
            db.delete_teacher(self.id)
    
    @staticmethod
    def get_all():
        """Get all teachers from database"""
        teachers = db.get_all_teachers()
        return [Teacher(row[1], row[2], row[0]) for row in teachers] if teachers else []
    
    def __repr__(self):
        return f"Teacher({self.id}, {self.name}, {self.subject})"


class Performance:
    """Class to represent Student Performance"""
    
    def __init__(self, student_id, subject, marks, perf_id=None):
        self.id = perf_id
        self.student_id = student_id
        self.subject = subject
        self.marks = marks
    
    def save(self):
        """Save performance record to database"""
        if self.id is None:
            db.add_performance(self.student_id, self.subject, self.marks)
        else:
            db.update_performance(self.id, self.subject, self.marks)
    
    def delete(self):
        """Delete performance record from database"""
        if self.id:
            db.delete_performance(self.id)
    
    def get_grade(self):
        """Calculate letter grade based on marks"""
        if self.marks >= 90:
            return 'A'
        elif self.marks >= 80:
            return 'B'
        elif self.marks >= 70:
            return 'C'
        elif self.marks >= 60:
            return 'D'
        else:
            return 'F'
    
    @staticmethod
    def get_by_student(student_id):
        """Get all performance records for a student"""
        performances = db.get_student_performance(student_id)
        return [Performance(row[1], row[2], row[3], row[0]) for row in performances] if performances else []
    
    def __repr__(self):
        return f"Performance({self.id}, Student:{self.student_id}, {self.subject}, {self.marks})"


class Attendance:
    """Class to represent Student Attendance"""
    
    def __init__(self, student_id, date, status, att_id=None):
        self.id = att_id
        self.student_id = student_id
        self.date = date
        self.status = status  # 'Present' or 'Absent'
    
    def save(self):
        """Save attendance record to database"""
        if self.id is None:
            db.add_attendance(self.student_id, self.date, self.status)
        else:
            db.update_attendance(self.id, self.status)
    
    def delete(self):
        """Delete attendance record from database"""
        if self.id:
            db.delete_attendance(self.id)
    
    @staticmethod
    def get_by_student(student_id):
        """Get all attendance records for a student"""
        attendances = db.get_student_attendance(student_id)
        return [Attendance(row[1], row[2], row[3], row[0]) for row in attendances] if attendances else []
    
    def __repr__(self):
        return f"Attendance({self.id}, Student:{self.student_id}, {self.date}, {self.status})"


class Fee:
    """Class to represent Student Fee"""
    
    def __init__(self, student_id, amount, status, fee_id=None):
        self.id = fee_id
        self.student_id = student_id
        self.amount = amount
        self.status = status  # 'Paid' or 'Pending'
    
    def save(self):
        """Save fee record to database"""
        if self.id is None:
            db.add_fee(self.student_id, self.amount, self.status)
        else:
            db.update_fee(self.id, self.amount, self.status)
    
    def delete(self):
        """Delete fee record from database"""
        if self.id:
            db.delete_fee(self.id)
    
    @staticmethod
    def get_by_student(student_id):
        """Get all fee records for a student"""
        fees = db.get_student_fees(student_id)
        return [Fee(row[1], row[2], row[3], row[0]) for row in fees] if fees else []
    
    @staticmethod
    def get_total_amount(student_id):
        """Get total fee amount for a student"""
        fees = Fee.get_by_student(student_id)
        return sum(fee.amount for fee in fees)
    
    def __repr__(self):
        return f"Fee({self.id}, Student:{self.student_id}, {self.amount}, {self.status})"


class School:
    """School class to manage CRUD operations for all entities"""
    
    @staticmethod
    def initialize():
        """Initialize database and create tables"""
        db.init_db()
        db.create_tables()
    
    # Student operations
    @staticmethod
    def add_student(name, grade, password):
        """Add a new student"""
        student = Student(name, grade, password)
        student.save()
        return student
    
    @staticmethod
    def get_all_students():
        """Get all students"""
        return Student.get_all()
    
    @staticmethod
    def get_student(student_id):
        """Get student by ID"""
        return Student.get_by_id(student_id)
    
    @staticmethod
    def update_student(student_id, name, grade, password):
        """Update student information"""
        student = Student(name, grade, password, student_id)
        student.save()
        return student
    
    @staticmethod
    def delete_student(student_id):
        """Delete a student"""
        student = Student.get_by_id(student_id)
        if student:
            student.delete()
    
    # Teacher operations
    @staticmethod
    def add_teacher(name, subject):
        """Add a new teacher"""
        teacher = Teacher(name, subject)
        teacher.save()
        return teacher
    
    @staticmethod
    def get_all_teachers():
        """Get all teachers"""
        return Teacher.get_all()
    
    @staticmethod
    def update_teacher(teacher_id, name, subject):
        """Update teacher information"""
        teacher = Teacher(name, subject, teacher_id)
        teacher.save()
        return teacher
    
    @staticmethod
    def delete_teacher(teacher_id):
        """Delete a teacher"""
        teacher = Teacher(None, None, teacher_id)
        teacher.delete()
    
    # Performance operations
    @staticmethod
    def add_performance(student_id, subject, marks):
        """Add performance record"""
        performance = Performance(student_id, subject, marks)
        performance.save()
        return performance
    
    @staticmethod
    def get_student_performance(student_id):
        """Get student performance"""
        return Performance.get_by_student(student_id)
    
    @staticmethod
    def get_student_gpa(student_id):
        """Get student GPA"""
        student = Student.get_by_id(student_id)
        if student:
            return student.get_gpa()
        return 0.0
    
    # Report generation
    @staticmethod
    def generate_performance_report(student_id):
        """Generate comprehensive performance report for a student"""
        student = Student.get_by_id(student_id)
        if not student:
            return None
        
        performances = Performance.get_by_student(student_id)
        attendances = Attendance.get_by_student(student_id)
        fees = Fee.get_by_student(student_id)
        
        # Calculate statistics
        if attendances:
            total_days = len(attendances)
            present_days = sum(1 for a in attendances if a.status == 'Present')
            attendance_percent = (present_days / total_days * 100) if total_days > 0 else 0
        else:
            total_days = 0
            present_days = 0
            attendance_percent = 0
        
        if performances:
            avg_marks = sum(p.marks for p in performances) / len(performances)
        else:
            avg_marks = 0
        
        if fees:
            total_fees = sum(f.amount for f in fees)
            paid_fees = sum(f.amount for f in fees if f.status == 'Paid')
        else:
            total_fees = 0
            paid_fees = 0
        
        return {
            'student': student,
            'performances': performances,
            'avg_marks': round(avg_marks, 2),
            'gpa': student.get_gpa(),
            'attendance': {
                'total_days': total_days,
                'present_days': present_days,
                'percentage': round(attendance_percent, 2)
            },
            'fees': {
                'total': total_fees,
                'paid': paid_fees,
                'pending': total_fees - paid_fees
            },
            'report_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
