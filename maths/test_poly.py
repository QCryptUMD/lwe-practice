import unittest
import polynomial


class TestPolynomials(unittest.TestCase):

   def test_printpoly(self):
       c1 = polynomial.Polynomial.from_coefficients([0, 1, 0, 1])
       c2 = polynomial.Polynomial.from_coefficients([1, 1, 0])
       c3 = polynomial.Polynomial.from_coefficients([0, 1, 0, 0, 1, 1])

       c4 = polynomial.Polynomial.from_coefficients([0, 1, 0, 0, 1, 1, 1, 0, 1, 1])
       self.assertEqual(str(c1), '<1x^1 + 1x^3>')
       self.assertEqual(str(c2), '<1x^0 + 1x^1>')
       self.assertEqual(str(c3), '<1x^0>')
       self.assertEqual(str(c4), '<1x^1 + 1x^2>')
    
    #need to implement 
    #def test_addpoly(self):
    #    c1 = polynomial.Polynomial.from_coefficients([3, 0, 2, 1, 0, 4, 5])

if __name__ == '__main__' :
    unittest.main()

