import unittest
from calculate import add,multiply,subtract,divide 

class modulesTesting(unittest.TestCase):
  def test_add(self):
    self.assertEqual(add(5,5),10)
  def test_multiply(self):
    self.assertEqual(multiply(4,2),8)
  def test_subtract(self):
    self.assertEqual(subtract(3,2),1)
  def test_divide(self):
    self.assertEqual(divide(10,5),2)
    
if __name__ == '__main__':
     unittest.main()