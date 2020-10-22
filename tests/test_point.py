import unittest
from point import Point
from math import pi


EPS = 1E-7

def showtest (f):
    def _intern(*args, **kwargs):
        print("Running %s"%(f.__name__))
        return f(*args, **kwargs)
    return _intern

class PointTestCase(unittest.TestCase):

    def setUp(self):
        self.p = Point(123.4, 2)
        self.p1 = Point(100,0)
        self.p2 = Point(0,100)
        self.p3 = Point(-100,0)
        self.o = Point(0,0)

    #@showtest
    def test_str(self):
        s = "(123.4, 2.0)"
        self.assertEqual(str(self.p), s)

    #@showtest
    def test_repr(self):
        s = "Point(123.4, 2.0)"
        self.assertEqual(repr(self.p), s)

    #@showtest
    def test_distance(self):
        d=self.p1.distance(self.p1)
        self.assertTrue(d<=EPS)

    #"@showtest
    def test_move(self):
        p3 = self.o.move(100,0)
        d=p3.distance(self.p1)
        self.assertTrue(d<=EPS)
        #
        p4 = self.o.move(100,pi/2)
        d=p4.distance(self.p2)
        self.assertTrue(d<=EPS)

    #@showtest
    def test_middle(self):
        m = self.p1.middle(self.p3)
        d = self.o.distance(m)
        self.assertTrue(d <= EPS)






if __name__ == '__main__':
    unittest.main()
