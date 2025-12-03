import unittest
from unittest.mock import patch, MagicMock
import ERP_pyodbc as db

class TestERP(unittest.TestCase):

    @patch("ERP_pyodbc.pyodbc.connect")
    def test_add_student_and_login(self, mock_connect):
        con = MagicMock()
        cur = MagicMock()
        mock_connect.return_value = con
        con.cursor.return_value = cur

        # Test add_student
        db.add_student("John", "10th", "pass123")
        cur.execute.assert_called_with(
            "INSERT INTO Students(name, grade, password) VALUES (?,?,?)",
            ("John", "10th", "pass123")
        )

        # Test verify_login success
        cur.fetchone.return_value = (1, "John", "10th", "pass123")
        self.assertTrue(db.verify_login("John", "pass123"))

        # Test verify_login fail
        cur.fetchone.return_value = None
        self.assertFalse(db.verify_login("Jane", "wrong"))

    @patch("ERP_pyodbc.pyodbc.connect")
    def test_add_teacher(self, mock_connect):
        con = MagicMock()
        cur = MagicMock()
        mock_connect.return_value = con
        con.cursor.return_value = cur

        db.add_teacher("Mr. Smith", "Math")
        cur.execute.assert_called_with(
            "INSERT INTO Teachers(name, subject) VALUES (?,?)",
            ("Mr. Smith", "Math")
        )

if __name__ == "__main__":
    unittest.main()
