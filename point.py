from turtle import *

from math import cos, sin, pi, sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%3.1f, %3.1f)" % (self.x, self.y)

    def __repr__(self):
        return "Point(%3.1f, %3.1f)" % (self.x, self.y)

    def move(self, rho, theta):
        """
            new point at rho, theta from current point
            rho is the distance
            theta is the angle in radians
        """
        return Point(self.x + rho * cos(theta), self.y + rho * sin(theta))

    def middle(self, p):
        """
            new point at the middle of the segmment from current point to p
        """
        return Point((self.x + p.x) / 2, (self.y + p.y) / 2)

    def distance(self, p):
        """
            distance from current point to p
        """
        return sqrt((p.x - self.x) ** 2 + (p.y - self.y) ** 2)


def main():
    pass


if __name__ == '__main__':
    main()