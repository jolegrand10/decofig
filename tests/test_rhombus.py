import unittest
from point import Point
from rhombus import Rhombus
from math import pi

class RhombusTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.r = Rhombus(Point(1, 2), pi / 10, 150, 100, lineColor = "pink", backgroundColor = "green")

    def test_str(self):
        s="""Point(1.0, 2.0)
Point(87.8, -22.4)
Point(143.7, 48.4)
Point(56.9, 72.7)
closed = True
fillColor = 'Red'
backgroundColor = 'green'
showTurtle = False
lineColor = 'pink'
lineWidth = 10"""
        self.assertEqual(str(self.r), s)

    def test_repr(self):
        s= "Figure(Point(1.0, 2.0), Point(87.8, -22.4), Point(143.7, 48.4), Point(56.9, 72.7), closed = True, fillColor = 'Red', \
backgroundColor = 'green', showTurtle = False, lineColor = 'pink', lineWidth = 10)"
        self.assertEqual(repr(self.r), s)


if __name__ == '__main__':
    unittest.main()
