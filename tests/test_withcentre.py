import unittest
from turtle import Screen, done

from point import Point
from rhombus import Rhombus
from withcentre import WithCentre


class WithCentreTestCase(unittest.TestCase):
    def setUp(self):
        self.loz = Rhombus(Point(-150, 200), 0, 100, 40)
        self.cloz = WithCentre(self.loz, centreSize = 12, centreColor = "White")


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
centreSize = 12
centreColor = 'White'"""
        self.assertEqual(s,str(self.cloz))

    def test_repr(self):
        s = """Figure(Point(-150.0, 200.0), Point(-100.0, 180.0), Point(-50.0, 200.0), \
Point(-100.0, 220.0), closed = True, fillColor = 'Red', backgroundColor = '', \
showTurtle = False, lineColor = 'Blue', lineWidth = 10, centreSize = 12, centreColor = 'White')"""
        self.assertEqual(s,repr(self.cloz))


    def test_draw(self):
        """Check that drawing does not alter the figure"""
        s1 = repr(self.cloz)
        win = Screen()
        self.cloz.draw()
        #done()
        self.assertEqual(s1, repr(self.cloz))


if __name__ == '__main__':
    unittest.main()
