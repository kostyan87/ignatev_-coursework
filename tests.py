from calculator import Calculator
from math import pi, e, cos, sin, tan, atan, log1p, log2, sqrt, asin
import unittest

test_1 = Calculator('cos(pi)')
test_2 = Calculator('sin(22*pi)')
test_3 = Calculator('-sqrt(4)')
test_4 = Calculator('-cos(3)')
test_5 = Calculator('((2+3)*4-(5-6))*(7+8)')
test_6 = Calculator('-sin(-cos(2*3 - -ln(e)*4))*5+-2*6')
test_7 = Calculator('sin(cos(2*3 - ln(3)*4))*5+2*6')
test_8 = Calculator('(cos((1-(2+3))*4))^(5+6)')
test_9 = Calculator('cos(1.2534-(2+3))')
test_10 = Calculator('cos(3+5)')
test_11 = Calculator('ln(23.1278*e)')
test_12 = Calculator('tg(log((log(23.1278 * 4))))')
test_13 = Calculator('-cos(-pi+1)*tg(log(log(ln(23.1278*e))))/13.0498-sin(3^7)')
test_14 = Calculator('cos( pi) * tg( log(log(ln(23.1278* e))))  /   13.0498-sin(3^ 7)')
test_15 = Calculator('cos( pi) * tg(- log(sin(-ln(23.1278* e))))  /   13.0498-sin(3^ 7) ')

class InsertTests(unittest.TestCase):
   
   def test_calculate_1(self):
      self.assertEqual(test_1.calculate(), cos(pi))

   def test_calculate_2(self):
      self.assertEqual(test_2.calculate(), sin(22*pi))

   def test_calculate_3(self):
      self.assertEqual(test_3.calculate(), -sqrt(4))

   def test_calculate_4(self):
      self.assertEqual(test_4.calculate(), -cos(3))

   def test_calculate_5(self):
      self.assertEqual(test_5.calculate(), ((2+3)*4-(5-6))*(7+8))
   
   def test_calculate_6(self):
      self.assertEqual(test_6.calculate(), -sin(-cos(2*3 - -log1p(e)*4))*5+-2*6)
   
   def test_calculate_7(self):
      self.assertEqual(test_7.calculate(), sin(cos(2*3 - log1p(3)*4))*5+2*6)
   
   def test_calculate_8(self):
      self.assertEqual(test_8.calculate(), (cos((1-(2+3))*4))**(5+6))
   
   def test_calculate_9(self):
      self.assertEqual(test_9.calculate(), cos(1.2534-(2+3)))
   
   def test_calculate_10(self):
      self.assertEqual(test_10.calculate(), cos(3+5))
   
   def test_calculate_11(self):
      self.assertEqual(test_11.calculate(), log1p(23.1278*e))
   
   def test_calculate_12(self):
      self.assertEqual(test_12.calculate(), tan(log2((log2(23.1278 * 4)))))
   
   def test_calculate_13(self):
      self.assertEqual(test_13.calculate(), -cos(-pi+1)*tan(log2(log2(log1p(23.1278*e))))/13.0498-sin(3**7))
   
   def test_calculate_14(self):
      self.assertEqual(test_14.calculate(), cos( pi) * tan( log2(log2(log1p(23.1278* e))))  /   13.0498-sin(3** 7))
   
   def test_calculate_15(self):
      self.assertEqual(test_15.calculate(), cos( pi) * tan(- log2(sin(-log1p(23.1278* e))))  /   13.0498-sin(3** 7))

if __name__ == '__name__':
   unittest.main()

# command to run tests: python -m unittest -v tests.py