import unittest

from dot import Dot
from point import Point


class DotTestCase(unittest.TestCase):
    def setUp(self):
        self.d = Dot(Point(100, -310), dotColor="Pink", dotSize=10)

    def test_str(self):
        s="""Point(100.0, -310.0)
closed = False
fillColor = 'Red'
backgroundColor = ''
showTurtle = False
lineColor = 'Blue'
lineWidth = 10
dotSize = 10
dotColor = 'Pink'"""
        self.assertEqual(str(self.d),s)

    def test_repr(self):
        s = """Dot(Point(100.0, -310.0), closed = False, fillColor = 'Red', backgroundColor = '', showTurtle = False, lineColor = 'Blue', lineWidth = 10, dotSize = 10, dotColor = 'Pink')"""
        self.assertEqual(repr(self.d), s)


if __name__ == '__main__':
    unittest.main()
