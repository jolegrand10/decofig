import unittest

from figure import Figure


class FigureTestCase(unittest.TestCase):
    def setUp(self):
        self.f = Figure(lineColor = "blue", backgroundColor="yellow")

    def test_str(self):
        s = """closed = False
fillColor = 'Red'
backgroundColor = 'yellow'
showTurtle = False
lineColor = 'blue'
lineWidth = 10"""
        self.assertEqual(str(self.f), s)

    def test_repr(self):
        s = """Figure(closed = False, fillColor = 'Red', backgroundColor = 'yellow', showTurtle = False, lineColor = 'blue', lineWidth = 10)"""
        self.assertEqual(repr(self.f), s)


if __name__ == '__main__':
    unittest.main()
