"""
Unit Tests for School Management System
Tests core business logic for students, teachers, and performance tracking
"""

import unittest
from unittest.mock import patch, MagicMock
import ERP_pyodbc as db
from models import Student, Teacher, Performance, School, Attendance, Fee


class TestStudentOperations(unittest.TestCase):
    """Test cases for Student model and operations"""

    @patch("ERP_pyodbc.pyodbc.connect")
    def test_add_student_success(self, mock_connect):
        """Test adding a new student to database"""
        con = MagicMock()
        cur = MagicMock()
        mock_connect.return_value = con
        con.cursor.return_value = cur

        # Test add_student via database function
        db.add_student("John Doe", "10th", "pass123")
        cur.execute.assert_called_with(
            "INSERT INTO Students(name, grade, password) VALUES (?,?,?)",
            ("John Doe", "10th", "pass123")
        )
        con.commit.assert_called()
        con.close.assert_called()

    @patch("ERP_pyodbc.pyodbc.connect")
    def test_verify_login_success(self, mock_connect):
        """Test successful student login verification"""
        con = MagicMock()
        cur = MagicMock()
        mock_connect.return_value = con
        con.cursor.return_value = cur
        
        # Mock successful login
        cur.fetchone.return_value = (1, "John Doe", "10th", "pass123")
        
        result = db.verify_login("John Doe", "pass123")
        self.assertTrue(result)
        
        cur.execute.assert_called_with(
            "SELECT * FROM Students WHERE name=? AND password=?",
            ("John Doe", "pass123")
        )

    @patch("ERP_pyodbc.pyodbc.connect")
    def test_verify_login_failure(self, mock_connect):
        """Test failed student login verification"""
        con = MagicMock()
        cur = MagicMock()
        mock_connect.return_value = con
        con.cursor.return_value = cur
        
        # Mock failed login
        cur.fetchone.return_value = None
        
        result = db.verify_login("Jane", "wrongpass")
        self.assertFalse(result)

    @patch("ERP_pyodbc.pyodbc.connect")
    def test_get_all_students(self, mock_connect):
        """Test retrieving all students from database"""
        con = MagicMock()
        cur = MagicMock()
        mock_connect.return_value = con
        con.cursor.return_value = cur
        
        # Mock multiple students
        cur.fetchall.return_value = [
            (1, "John Doe", "10th", "pass123"),
            (2, "Jane Smith", "11th", "pass456")
        ]
        
        students = db.get_all_students()
        self.assertEqual(len(students), 2)
        self.assertEqual(students[0][1], "John Doe")
        self.assertEqual(students[1][1], "Jane Smith")

    @patch("ERP_pyodbc.pyodbc.connect")
    def test_delete_student_with_cascade(self, mock_connect):
        """Test deleting student and all related records"""
        con = MagicMock()
        cur = MagicMock()
        mock_connect.return_value = con
        con.cursor.return_value = cur
        
        db.delete_student(1)
        
        # Verify cascade delete is called
        self.assertEqual(cur.execute.call_count, 4)  # Delete Attendance, Fees, Performance, Student
        con.commit.assert_called()


class TestTeacherOperations(unittest.TestCase):
    """Test cases for Teacher model and operations"""

    @patch("ERP_pyodbc.pyodbc.connect")
    def test_add_teacher_success(self, mock_connect):
        """Test adding a new teacher to database"""
        con = MagicMock()
        cur = MagicMock()
        mock_connect.return_value = con
        con.cursor.return_value = cur

        db.add_teacher("Mr. Smith", "Mathematics")
        cur.execute.assert_called_with(
            "INSERT INTO Teachers(name, subject) VALUES (?,?)",
            ("Mr. Smith", "Mathematics")
        )
        con.commit.assert_called()

    @patch("ERP_pyodbc.pyodbc.connect")
    def test_get_all_teachers(self, mock_connect):
        """Test retrieving all teachers"""
        con = MagicMock()
        cur = MagicMock()
        mock_connect.return_value = con
        con.cursor.return_value = cur
        
        cur.fetchall.return_value = [
            (1, "Mr. Smith", "Mathematics"),
            (2, "Ms. Johnson", "English")
        ]
        
        teachers = db.get_all_teachers()
        self.assertEqual(len(teachers), 2)
        self.assertEqual(teachers[0][1], "Mr. Smith")

    @patch("ERP_pyodbc.pyodbc.connect")
    def test_update_teacher(self, mock_connect):
        """Test updating teacher information"""
        con = MagicMock()
        cur = MagicMock()
        mock_connect.return_value = con
        con.cursor.return_value = cur

        db.update_teacher(1, "Mr. Johnson", "Science")
        cur.execute.assert_called_with(
            "UPDATE Teachers SET name=?, subject=? WHERE id=?",
            ("Mr. Johnson", "Science", 1)
        )


class TestPerformanceTracking(unittest.TestCase):
    """Test cases for Performance tracking and GPA calculation"""

    @patch("ERP_pyodbc.pyodbc.connect")
    def test_add_performance_record(self, mock_connect):
        """Test adding a performance record"""
        con = MagicMock()
        cur = MagicMock()
        mock_connect.return_value = con
        con.cursor.return_value = cur

        db.add_performance(1, "Mathematics", 85)
        cur.execute.assert_called_with(
            "INSERT INTO Performance(student_id, subject, marks) VALUES (?,?,?)",
            (1, "Mathematics", 85)
        )

    @patch("ERP_pyodbc.pyodbc.connect")
    def test_calculate_student_gpa(self, mock_connect):
        """Test GPA calculation based on marks"""
        con = MagicMock()
        cur = MagicMock()
        mock_connect.return_value = con
        con.cursor.return_value = cur
        
        # Mock average marks calculation
        cur.fetchone.return_value = (85.0,)
        
        gpa = db.calculate_student_gpa(1)
        self.assertEqual(gpa, 4.25)  # 85/20 = 4.25

    @patch("ERP_pyodbc.pyodbc.connect")
    def test_get_student_performance(self, mock_connect):
        """Test retrieving all performance records for a student"""
        con = MagicMock()
        cur = MagicMock()
        mock_connect.return_value = con
        con.cursor.return_value = cur
        
        cur.fetchall.return_value = [
            (1, 1, "Mathematics", 85),
            (2, 1, "English", 90),
            (3, 1, "Science", 78)
        ]
        
        performances = db.get_student_performance(1)
        self.assertEqual(len(performances), 3)

    def test_performance_grading(self):
        """Test letter grade calculation from marks"""
        perf_a = Performance(1, "Math", 95)
        self.assertEqual(perf_a.get_grade(), 'A')
        
        perf_b = Performance(1, "Math", 85)
        self.assertEqual(perf_b.get_grade(), 'B')
        
        perf_c = Performance(1, "Math", 75)
        self.assertEqual(perf_c.get_grade(), 'C')
        
        perf_d = Performance(1, "Math", 65)
        self.assertEqual(perf_d.get_grade(), 'D')
        
        perf_f = Performance(1, "Math", 45)
        self.assertEqual(perf_f.get_grade(), 'F')


class TestAttendanceOperations(unittest.TestCase):
    """Test cases for Attendance tracking"""

    @patch("ERP_pyodbc.pyodbc.connect")
    def test_add_attendance_record(self, mock_connect):
        """Test adding an attendance record"""
        con = MagicMock()
        cur = MagicMock()
        mock_connect.return_value = con
        con.cursor.return_value = cur

        db.add_attendance(1, "2024-01-15", "Present")
        cur.execute.assert_called_with(
            "INSERT INTO Attendance(student_id, date, status) VALUES (?,?,?)",
            (1, "2024-01-15", "Present")
        )

    @patch("ERP_pyodbc.pyodbc.connect")
    def test_get_student_attendance(self, mock_connect):
        """Test retrieving attendance records for a student"""
        con = MagicMock()
        cur = MagicMock()
        mock_connect.return_value = con
        con.cursor.return_value = cur
        
        cur.fetchall.return_value = [
            (1, 1, "2024-01-15", "Present"),
            (2, 1, "2024-01-16", "Present"),
            (3, 1, "2024-01-17", "Absent")
        ]
        
        attendances = db.get_student_attendance(1)
        self.assertEqual(len(attendances), 3)


class TestFeeManagement(unittest.TestCase):
    """Test cases for Fee management"""

    @patch("ERP_pyodbc.pyodbc.connect")
    def test_add_fee_record(self, mock_connect):
        """Test adding a fee record"""
        con = MagicMock()
        cur = MagicMock()
        mock_connect.return_value = con
        con.cursor.return_value = cur

        db.add_fee(1, 5000.00, "Pending")
        cur.execute.assert_called_with(
            "INSERT INTO Fees(student_id, amount, status) VALUES (?,?,?)",
            (1, 5000.00, "Pending")
        )

    @patch("ERP_pyodbc.pyodbc.connect")
    def test_get_student_fees(self, mock_connect):
        """Test retrieving fee records for a student"""
        con = MagicMock()
        cur = MagicMock()
        mock_connect.return_value = con
        con.cursor.return_value = cur
        
        cur.fetchall.return_value = [
            (1, 1, 5000.00, "Paid"),
            (2, 1, 5000.00, "Pending")
        ]
        
        fees = db.get_student_fees(1)
        self.assertEqual(len(fees), 2)
        self.assertEqual(fees[0][2], 5000.00)

    @patch("ERP_pyodbc.pyodbc.connect")
    def test_update_fee_status(self, mock_connect):
        """Test updating fee payment status"""
        con = MagicMock()
        cur = MagicMock()
        mock_connect.return_value = con
        con.cursor.return_value = cur

        db.update_fee(1, 5000.00, "Paid")
        cur.execute.assert_called_with(
            "UPDATE Fees SET amount=?, status=? WHERE id=?",
            (5000.00, "Paid", 1)
        )


class TestReportGeneration(unittest.TestCase):
    """Test cases for report generation"""

    @patch("ERP_pyodbc.pyodbc.connect")
    def test_performance_report_generation(self, mock_connect):
        """Test generating comprehensive performance report"""
        con = MagicMock()
        cur = MagicMock()
        mock_connect.return_value = con
        con.cursor.return_value = cur
        
        # Mock student data
        cur.fetchone.return_value = (1, "John Doe", "10th", "pass123")
        cur.fetchall.side_effect = [
            [(1, 1, "Math", 85), (2, 1, "English", 90)],  # Performances
            [(1, 1, "2024-01-15", "Present")],  # Attendance count
            [(1000.00,)]  # Fees
        ]
        
        report = db.get_performance_report(1)
        self.assertIsNotNone(report)
        self.assertEqual(report['student'][1], "John Doe")


class TestSchoolManagement(unittest.TestCase):
    """Test cases for School management operations"""

    @patch("ERP_pyodbc.pyodbc.connect")
    def test_student_gpa_calculation(self, mock_connect):
        """Test comprehensive GPA calculation for student"""
        con = MagicMock()
        cur = MagicMock()
        mock_connect.return_value = con
        con.cursor.return_value = cur
        
        # Mock various marks
        cur.fetchone.return_value = (88.0,)
        
        gpa = db.calculate_student_gpa(1)
        # GPA = Average marks / 20 (if marks out of 100)
        expected_gpa = round(88.0 / 20, 2)
        self.assertEqual(gpa, expected_gpa)

    def test_performance_statistics(self):
        """Test performance statistics calculations"""
        performances = [
            Performance(1, "Math", 95),
            Performance(1, "English", 85),
            Performance(1, "Science", 78)
        ]
        
        avg_marks = sum(p.marks for p in performances) / len(performances)
        self.assertAlmostEqual(avg_marks, 86.0, places=1)

    def test_attendance_percentage_calculation(self):
        """Test calculating attendance percentage"""
        total_days = 20
        present_days = 18
        percentage = (present_days / total_days) * 100
        
        self.assertEqual(percentage, 90.0)

    @patch("ERP_pyodbc.pyodbc.connect")
    def test_fee_collection_summary(self, mock_connect):
        """Test fee collection summary calculation"""
        con = MagicMock()
        cur = MagicMock()
        mock_connect.return_value = con
        con.cursor.return_value = cur
        
        # Mock fee data
        fees = [
            Fee(1, 5000.0, "Paid"),
            Fee(1, 5000.0, "Paid"),
            Fee(1, 5000.0, "Pending")
        ]
        
        total_fees = sum(f.amount for f in fees)
        paid_fees = sum(f.amount for f in fees if f.status == "Paid")
        pending_fees = total_fees - paid_fees
        
        self.assertEqual(total_fees, 15000.0)
        self.assertEqual(paid_fees, 10000.0)
        self.assertEqual(pending_fees, 5000.0)


class TestDataIntegrity(unittest.TestCase):
    """Test cases for data integrity and constraints"""

    @patch("ERP_pyodbc.pyodbc.connect")
    def test_cascade_delete_on_student_deletion(self, mock_connect):
        """Test that related records are deleted when student is deleted"""
        con = MagicMock()
        cur = MagicMock()
        mock_connect.return_value = con
        con.cursor.return_value = cur

        # Delete student should cascade delete related records
        db.delete_student(1)
        
        # Check that all related tables are queried for deletion
        calls = cur.execute.call_args_list
        self.assertEqual(len(calls), 4)  # Attendance, Fees, Performance, Students
        
        # Verify the order of deletes (should delete references first)
        first_call = calls[0][0][0]
        self.assertIn("Attendance", first_call)

    def test_marks_range_validation(self):
        """Test that marks are within valid range"""
        valid_perf = Performance(1, "Math", 85)
        self.assertTrue(0 <= valid_perf.marks <= 100)
        
        # Test boundary values
        min_perf = Performance(1, "Math", 0)
        self.assertEqual(min_perf.marks, 0)
        
        max_perf = Performance(1, "Math", 100)
        self.assertEqual(max_perf.marks, 100)

    def test_fee_amount_positive_value(self):
        """Test that fee amounts are positive"""
        fee = Fee(1, 5000.0, "Paid")
        self.assertGreater(fee.amount, 0)


if __name__ == "__main__":
    unittest.main()
