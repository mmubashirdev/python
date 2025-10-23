import unittest
from calculator import calculator

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculator(3,'+',2),5)
    def test_substraction(self):
        self.assertEqual(calculator(5,'-',5),0)
    def test_multiplication(self):
        self.assertEqual(calculator(3,'*',3),9)
    def test_divison(self):
        self.assertEqual(calculator(4,'/',2),2)
        self.assertEqual(calculator(4,'/',0), "Error: Divisor cannot be zero")
    def test_invalid_operator(self):
        self.assertEqual(calculator(3,'%',2), "Invalid operator")
        self.assertEqual(calculator(5,'x',4), "Invalid operator")
        
if __name__ == '__main__':
    unittest.main()