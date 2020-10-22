import unittest

from point import Point
from rhombus import Rhombus
from withtranslation import WithTranslation
from turtle import Screen, done, hideturtle


class WithTranslationTestCase(unittest.TestCase):
    def setUp(self):
        self.loz = Rhombus(Point(-150, 200), 0, 100, 40)
        self.tloz=WithTranslation(self.loz, dx =0, dy = 100.0)

    def tearDown(self):
        pass

    def test_str(self):
        #Note that translation is applied on coordinates
        s = """Point(-150.0, 200.0)
Point(-100.0, 180.0)
Point(-50.0, 200.0)
Point(-100.0, 220.0)
closed = True
fillColor = 'Red'
backgroundColor = ''
showTurtle = False
lineColor = 'Blue'
lineWidth = 10"""
        self.assertEqual(str(self.tloz), s)

    def test_repr(self):
        s = """Figure(Point(-150.0, 200.0), Point(-100.0, 180.0), Point(-50.0, 200.0), \
Point(-100.0, 220.0), closed = True, fillColor = 'Red', backgroundColor = '', \
showTurtle = False, lineColor = 'Blue', lineWidth = 10)"""
        self.assertEqual(s,repr(self.tloz))
        loz1= WithTranslation(self.tloz, dx=140, dy=123)
        s1 = "Figure(Point(-150.0, 200.0), Point(-100.0, 180.0), Point(-50.0, 200.0), \
Point(-100.0, 220.0), closed = True, fillColor = 'Red', backgroundColor = '', \
showTurtle = False, lineColor = 'Blue', lineWidth = 10)"
        self.assertEqual(s1,repr(loz1))

    def test_draw(self):
        """Check that drawing does not alter the figure"""
        s1=repr(self.tloz)
        win = Screen()
        self.tloz.draw()
        self.assertEqual(s1,repr(self.tloz))

if __name__ == '__main__':
    unittest.main()
