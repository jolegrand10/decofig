from point import Point
from figure import Figure
from line import Line
from polyline import Polyline
from polygon import Polygon
from rectangle import Rectangle
from rhombus import Rhombus
from withdots import WithDots
from withcentre import WithCentre
from withrotation import WithRotation
from withtranslation import WithTranslation
from withtransparency import WithTransparency
from turtle import *

def demo():

    win=Screen()
    #Build display list
    displayList = []
    # rectangle,centered at 0,0
    a = 50.0
    r0 = Rhombus(Point(-a, a),0,1.5*a,2*a, lineWidth=1, lineColor='green', fillColor='aquamarine', showTurtle='False', backgroundColor = 'black')
    displayList.append(r0)
    # draw the same rectangle in the top left corner
    b = 150.0
    r1 = r0.translate1(-b, +b)
    displayList.append(r1)
    # draw the rectangle in the top midlle but rotated
    r2 = r1.rotate1(45).translate1(b,0)
    displayList.append(r2)
    # one more slightly rotated in the top right corner
    r3 = r2.translate1(b,0).rotate1(15)
    displayList.append(r3)
    # same figures in the bottom
    r4 = WithCentre(r1.translate1(0,-2*b),centreColor='red')
    r5 = WithTransparency(r2.translate1(0,-2*b))
    r6 = WithDots(r3.translate1(0, -2 * b), dotColor = 'pink')
    displayList += [r4, r5, r6]


    #WithTransparency(WithCentre(WithDots(r))).draw()
    #Display the list
    for f in displayList:
        f.draw()
    hideturtle()
    done()

def main():
    win=Screen()
    #Build display list
    displayList = []

    # check translate
    a = 50.0
    r0 = Rhombus(Point(-a, a), 0, 1.5 * a, 2 * a, lineWidth = 1, lineColor = 'green', fillColor = 'aquamarine',
                 showTurtle = 'False', backgroundColor = 'black')
    displayList.append(r0)

    r0.translate(100,100)
    r0.translate(100, 100)
    r1 = WithTranslation(r0,-200,-200)
    displayList.append(r1)

    # Display the list
    for f in displayList:
        f.draw()
    hideturtle()
    done()

if __name__ == "__main__":
    demo()