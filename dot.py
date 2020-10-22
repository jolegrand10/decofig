from turtle import *
from figure import Figure
from point import Point
class Dot(Figure):
    """ a simple figure made of a dot defined by 1 point """
    def __init__(self,p,dotSize = 5, dotColor = 'White'):
        """ shows a dot at point p """
        super().__init__()
        self.point = [p]
        self.prop['dotSize'] = dotSize
        self.prop['dotColor'] = dotColor

    def draw(self):
        """ moves to point location and draws a dot
        """
        super().draw()
        dot(self.prop['dotSize'], self.prop['dotColor'])

    def __repr__(self):
        return "Dot(%s)" % (", ".join(self._point() + self._prop()))



def main():
    #tests draw
    win=Screen()
    hideturtle()
    d = Dot(Point(100, -100), dotColor="Pink", dotSize=50)
    d.draw()
    done()

if __name__ == '__main__':
    main()