import unittest
from calculator import calculator

class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(calculator(3, '+', 2), 5)

    def test_subtraction(self):
        self.assertEqual(calculator(5, '-', 3), 2)

    def test_multiplication(self):
        self.assertEqual(calculator(4, '*', 3), 12)

    def test_division(self):
        self.assertEqual(calculator(10, '/', 2), 5)

        self.assertEqual(calculator(5, '/', 0), "Error: Divisor cannot be zero")

    def test_invalid_operator(self):
        self.assertEqual(calculator(3, '%', 2), "Invalid operator")
        self.assertEqual(calculator(4, 'x', 1), "Invalid operator")

if __name__ == '__main__':
    unittest.main()
