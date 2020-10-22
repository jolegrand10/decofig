import unittest

from line import Line
from point import Point


class LineTestCase(unittest.TestCase):
    def setUp(self):
        self.l = Line(Point(100, 110), Point(220, 230), lineColor="Pink", lineWidth=1, fillColor='Yellow')

    def test_str(self):
        s = """Point(100.0, 110.0)
Point(220.0, 230.0)
closed = False
fillColor = 'Yellow'
backgroundColor = ''
showTurtle = False
lineColor = 'Pink'
lineWidth = 1"""
        self.assertEqual(str(self.l), s)

    def test_repr(self):
        s = """Line(Point(100.0, 110.0), Point(220.0, 230.0), closed = False, fillColor = 'Yellow', backgroundColor = '', showTurtle = False, lineColor = 'Pink', lineWidth = 1)"""
        self.assertEqual(repr(self.l), s)


if __name__  == '__main__':
    unittest.main()
