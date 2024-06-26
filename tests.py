from fraction import Fraction
import unittest


class TestInit(unittest.TestCase):
    # several of these will need to check to see if an exception is raised
    def test_divZero(self):
        with self.assertRaises(ZeroDivisionError, msg="Denominator of zero fails to raise DivByZero"):
            a = Fraction(1, 0)

    def test_default(self):
        # pass #will the 0 argument version of the constructor produce the correct fraction?
        a = Fraction()
        self.assertEqual(a.numerator, 0)
        self.assertEqual(a.denominator, 1)

    def test_oneArg(self):
        # pass #will the 1 argument version of the constructor produce the correct fraction?
        a = Fraction(6)
        self.assertEqual(a.numerator, 6)
        self.assertEqual(a.denominator, 1)

    def test_twoArg(self):
        # pass #will the 2 argument version of the constructor produce the correct fraction?
        a = Fraction(6, 5)
        self.assertEqual(a.numerator, 6)
        self.assertEqual(a.denominator, 5)

    def test_invalidArg(self):
        # pass #will constructor through an exception if non-numeric data is passed?
        with self.assertRaises(TypeError, msg="must take int variables"):
            a = Fraction(3.5)

    def test_reduced(self):
        # pass #if the inputs share a factor, is the fraction reduced? i.e. 2/4 = 1/2
        a = Fraction(4, 2)
        self.assertEqual(a.numerator, 2)
        self.assertEqual(a.denominator, 1)


class TestStr(unittest.TestCase):
    
    def setUp(self):
        self.f0 = Fraction()
        self.f1 = Fraction(1,2)
        self.f2 = Fraction(-1,2)
    
    def test_displayFraction(self):
        
        self.assertEqual(" 1/2 ", self.f1.__str__())

    def test_displayInt(self):
        # pass #if the denominator is 1, does display omit the /1?
        a = Fraction(5, 1)
        self.assertEqual(" 5 ", a.__str__())

    def test_displayNeg(self):
        # pass #if the fraction is negative, is it possible to erroneously have it display 1/-2, vs -1/2?
        self.assertEqual(" -1/2 ", self.f2.__str__())
        self.assertEqual(" -1/2 ", self.f2.__str__())


class TestFloat(unittest.TestCase):
    
    def setUp(self):
        self.f0 = Fraction()
        self.f1 = Fraction(1,2)
        self.f2 = Fraction(-1,2)
        
    def test_displayFloat(self):
        
        self.assertEqual(0.5, self.f1.__str__())

    def test_displayNeg(self):
        a = Fraction(-1, 2)
        self.assertEqual(-0.5, self.f2.__str__())


class TestAdd(unittest.TestCase):

    def setUp(self):
        self.f0 = Fraction()
        self.f1 = Fraction(1,2)
        self.f2 = Fraction(-1,2)
        self.f3 = Fraction(1,1)
        
    def test_invalidType(self):
        
        with self.assertRaises(TypeError, msg="must take Fraction Objects"):
            self.f0.__add__("no, just no")

    def test_add(self):
        self.assertEqual(self.f3, self.f1.__add__(self.f1))

    def test_addZero(self):
        self.assertEqual(self.f1, self.f1.__add__(self.f0))

    def test_addNeg(self):
        self.assertEqual(self.f0, self.f1.__add__(self.f2))


class TestSub(unittest.TestCase):

    def setUp(self):
        self.f0 = Fraction()
        self.f1 = Fraction(1,2)
        self.f2 = Fraction(-1,2)
        
    def test_invalidType(self):
        
        with self.assertRaises(TypeError, msg="must take Fraction Objects"):
            self.f0.__sub__("no, just no")

    def test_sub(self):
        self.assertEqual(self.f0, self.f1.__sub__(self.f1))


class TestMult(unittest.TestCase):

    def test_invalidType(self):
        a = Fraction()
        with self.assertRaises(TypeError, msg="must take Fraction Objects"):
            a.__mul__("no, just no")

    def test_mult(self):
        a = Fraction(1, 2)
        b = Fraction(1, 2)
        c = Fraction(1, 4)
        self.assertEqual(c, a.__mul__(b))

    def test_mulZero(self):
        a = Fraction(1, 2)
        b = Fraction()
        self.assertEqual(b, a.__mul__(b))

    def test_mulOneNeg(self):
        a = Fraction(1, 2)
        b = Fraction(-1, 2)
        c = Fraction(-1, 4)
        self.assertEqual(c, a.__mul__(b))

    def test_mulTwoNeg(self):
        a = Fraction(-1, 2)
        b = Fraction(-1, 2)
        c = Fraction(1, 4)
        self.assertEqual(c, a.__mul__(b))


class TestDiv(unittest.TestCase):

    def test_invalidType(self):
        a = Fraction(1, 2)
        with self.assertRaises(TypeError, msg="must take Fraction Objects"):
            a.__truediv__("no, just no")

    def test_div(self):
        a = Fraction(1, 2)
        b = Fraction(1, 2)
        c = Fraction(1, 1)
        self.assertEqual(c, a.__truediv__(b))

    def test_divZero(self):
        a = Fraction(1, 2)
        b = Fraction()
        with self.assertRaises(ZeroDivisionError):
            a.__truediv__(b)

    def test_divOneNeg(self):
        a = Fraction(1, 2)
        b = Fraction(-1, 2)
        c = Fraction(-1, 1)
        self.assertEqual(c, a.__truediv__(b))

    def test_divTwoNeg(self):
        a = Fraction(-1, 2)
        b = Fraction(-1, 2)
        c = Fraction(1, 1)
        self.assertEqual(c, a.__truediv__(b))
