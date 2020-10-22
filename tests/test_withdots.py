import unittest
from turtle import Screen

from point import Point
from rhombus import Rhombus
from withdots import WithDots


class WithDotsTestCase(unittest.TestCase):
    def setUp(self):
        self.loz = Rhombus(Point(-150, 200), 0, 100, 40)
        self.dloz = WithDots(self.loz, dotSize = 5, dotColor = "Cyan")
        self.maxDiff = None

    def tearDown(self):
        pass

    def test_str(self):
        s = """Point(-150.0, 200.0)
Point(-100.0, 180.0)
Point(-50.0, 200.0)
Point(-100.0, 220.0)
closed = True
fillColor = 'Red'
backgroundColor = ''
showTurtle = False
lineColor = 'Blue'
lineWidth = 10
dotSize = 5
dotColor = 'Cyan'"""
        self.assertEqual(s,str(self.dloz))

    def test_repr(self):
        s = """Figure(Point(-150.0, 200.0), Point(-100.0, 180.0), Point(-50.0, 200.0), \
Point(-100.0, 220.0), closed = True, fillColor = 'Red', backgroundColor = '', \
showTurtle = False, lineColor = 'Blue', lineWidth = 10, dotSize = 5, dotColor = 'Cyan')"""
        self.assertEqual(s,repr(self.dloz))

    def test_draw(self):
        """Check that drawing does not alter the figure"""
        s1 = repr(self.dloz)
        win = Screen()
        self.dloz.draw()
        # done()
        self.assertEqual(s1, repr(self.dloz))


if __name__ == '__main__':
    unittest.main()
