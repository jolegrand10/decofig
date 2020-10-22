import unittest
from turtle import Screen, done

from point import Point
from rhombus import Rhombus
from withrotation import WithRotation


class WithRotationTestCase(unittest.TestCase):
    def setUp(self):
        self.loz = Rhombus(Point(-150, 200), 0, 100, 40)
        self.rloz = WithRotation(self.loz, alpha = 45)

    def tearDown(self):
        pass

    def test_str(self):
        s = """Point(-135.4, 235.4)
Point(-114.1, 185.9)
Point(-64.6, 164.6)
Point(-85.9, 214.1)
closed = True
fillColor = 'Red'
backgroundColor = ''
showTurtle = False
lineColor = 'Blue'
lineWidth = 10"""
        self.assertEqual(s,str(self.rloz))

    def test_repr(self):
        s = """Figure(Point(-135.4, 235.4), Point(-114.1, 185.9), Point(-64.6, 164.6), \
Point(-85.9, 214.1), closed = True, fillColor = 'Red', backgroundColor = '', \
showTurtle = False, lineColor = 'Blue', lineWidth = 10)"""
        self.assertEqual(s, repr(self.rloz))
        loz1 = WithRotation(self.rloz, alpha = 60)
        s1 = "Figure(Point(-87.1, 248.3), Point(-119.3, 205.2), Point(-112.9, 151.7), \
Point(-80.7, 194.8), closed = True, fillColor = 'Red', backgroundColor = '', \
showTurtle = False, lineColor = 'Blue', lineWidth = 10)"
        self.assertEqual(s1, repr(loz1))

    def test_draw(self):
        """Check that drawing does not alter the figure"""
        s1 = repr(self.rloz)
        win = Screen()
        self.rloz.draw()
        #done()
        self.assertEqual(s1, repr(self.rloz))


if __name__ == '__main__':
    unittest.main()
