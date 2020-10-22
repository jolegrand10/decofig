import unittest
from polygon import Polygon
from point import Point


class PolygonTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.p = Polygon(Point(10, 20), Point(20, 30), Point(30, 40), Point(40, 50), lineColor = "pink", backgroundColor = "green")

    def test_str(self):
        s="""Point(10.0, 20.0)
Point(20.0, 30.0)
Point(30.0, 40.0)
Point(40.0, 50.0)
closed = True
fillColor = 'Red'
backgroundColor = 'green'
showTurtle = False
lineColor = 'pink'
lineWidth = 10"""
        self.assertEqual(str(self.p), s)

    def test_repr(self):
        s = "Figure(Point(10.0, 20.0), Point(20.0, 30.0), Point(30.0, 40.0), Point(40.0, 50.0), closed = True, fillColor = 'Red', backgroundColor = 'green', showTurtle = False, lineColor = 'pink', lineWidth = 10)"
        self.assertEqual(repr(self.p), s)

if __name__ == '__main__':
    unittest.main()
