import unittest
from numerical_methods import bisection, false_position, fixed_point, newton

class TestMethods(unittest.TestCase):
    def setUp(self):
        self.f = lambda x: x**3-x-2
        self.df = lambda x: 3*x*x-1
        self.alpha = 1.5213797068
    def test_bisection(self):
        self.assertAlmostEqual(bisection(self.f,1,2)["root"], self.alpha, places=8)
    def test_false_position(self):
        self.assertAlmostEqual(false_position(self.f,1,2)["root"], self.alpha, places=8)
    def test_newton(self):
        self.assertAlmostEqual(newton(self.f,self.df,1.5)["root"], self.alpha, places=8)
    def test_fixed_point(self):
        g = lambda x: (x+2)**(1/3)
        self.assertAlmostEqual(fixed_point(g,1.5)["root"], self.alpha, places=8)
    def test_bad_interval(self):
        with self.assertRaises(ValueError): bisection(self.f,2,3)

if __name__ == "__main__": unittest.main()
