import unittest
from point import Point
from rectangle import Rectangle
from math import pi


class RectangleTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.r = Rectangle (Point(1, 2), pi / 10, 150, 100, lineColor = "pink", fillColor = "green")

    def test_str(self):
        s="""Point(1.0, 2.0)
Point(143.7, 48.4)
Point(174.6, -46.8)
Point(31.9, -93.1)
closed = True
fillColor = 'green'
backgroundColor = ''
showTurtle = False
lineColor = 'pink'
lineWidth = 10"""
        self.assertEqual(str(self.r), s)

    def test_repr(self):
        s = "Figure(Point(1.0, 2.0), Point(143.7, 48.4), Point(174.6, -46.8), Point(31.9, -93.1), closed = True, \
fillColor = 'green', backgroundColor = '', showTurtle = False, lineColor = 'pink', lineWidth = 10)"
        self.assertEqual(repr(self.r),s)


if __name__ == '__main__':
    unittest.main()
