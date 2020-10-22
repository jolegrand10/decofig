import unittest
from polyline import Polyline
from point import Point

class PolylineTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.p = Polyline(Point(1, 2), Point(2, 3), Point(3, 4), Point(4, 5), lineColor="pink", backgroundColor="green")

    def test_str(self):
        s="""Point(1.0, 2.0)
Point(2.0, 3.0)
Point(3.0, 4.0)
Point(4.0, 5.0)
closed = False
fillColor = 'Red'
backgroundColor = 'green'
showTurtle = False
lineColor = 'pink'
lineWidth = 10"""
        self.assertEqual(str(self.p),s)

    def test_repr(self):
        s="Figure(Point(1.0, 2.0), Point(2.0, 3.0), Point(3.0, 4.0), Point(4.0, 5.0), closed = False, fillColor = 'Red', backgroundColor = 'green', showTurtle = False, lineColor = 'pink', lineWidth = 10)"
        self.assertEqual(repr(self.p), s)


if __name__ == '__main__':
    unittest.main()
