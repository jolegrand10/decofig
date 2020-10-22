import unittest
from turtle import Screen

from point import Point
from rhombus import Rhombus
from withtransparency import WithTransparency


class WithTransparencyTestCase(unittest.TestCase):
    def setUp(self):
        self.loz = Rhombus(Point(-150, 200), 0, 100, 40)
        self.trsploz = WithTransparency(self.loz)

    def tearDown(self):
        pass

    def test_str(self):
        s = """Point(-150.0, 200.0)
Point(-100.0, 180.0)
Point(-50.0, 200.0)
Point(-100.0, 220.0)
closed = True
fillColor = ''
backgroundColor = ''
showTurtle = False
lineColor = 'Blue'
lineWidth = 10"""
        self.assertEqual(str(self.trsploz), s)

    def test_repr(self):
        s = """Figure(Point(-150.0, 200.0), Point(-100.0, 180.0), Point(-50.0, 200.0), Point(-100.0, 220.0), \
closed = True, fillColor = '', backgroundColor = '', showTurtle = False, lineColor = 'Blue', lineWidth = 10)"""
        self.assertEqual(s,repr(self.trsploz))

    def test_draw(self):
        """Check that drawing does not alter the figure"""
        s1 = repr(self.trsploz)
        win = Screen()
        self.trsploz.draw()
        # done()
        self.assertEqual(s1, repr(self.trsploz))


if __name__ == '__main__':
    unittest.main()
