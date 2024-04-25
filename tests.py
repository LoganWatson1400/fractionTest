from fraction import Fraction
import unittest

class TestInit(unittest.TestCase):
  #several of these will need to check to see if an exception is raised
  def test_divZero(self):
    with self.assertRaises(ZeroDivisionError,msg="Denominator of zero fails to raise DivByZero"):
      a = Fraction(1,0)
  def test_default(self):
    # pass #will the 0 argument version of the constructor produce the correct fraction?
    a = Fraction()s
    self.assertEqual(a, '0/1')
  def test_oneArg(self):
    # pass #will the 1 argument version of the constructor produce the correct fraction?
    a = Fraction(6)
    self.assertEqual(a, 6)
  def test_twoArg(self):
    pass #will the 2 argument version of the constructor produce the correct fraction?
  def test_invalidArg(self):
    pass #will constructor through an exception if non-numeric data is passed?
  def test_reduced(self):
    pass #if the inputs share a factor, is the fraction reduced? i.e. 2/4 = 1/2

class TestStr(unittest.TestCase):
  def test_displayfraction(self):
    a = Fraction(1,2)
    self.assertEqual(" 1/2 ",a.__str__())
  def test_displayInt(self):
    pass #if the denominator is 1, does display omit the /1?
  def test_displayNeg(self):
    pass #if the fraction is negative, is it possible to erroneously have it display 1/-2, vs -1/2?
    
