"""
@author : Nishant Sanjay Kumbhar
@goal : to find out , is it correct triangle or not
"""
import sys


class Point2D:
    def __init__(self, x: float, y: float):
        """
        Constructor of Point2D class
        :param x: x-coordinate of point
        :param y: y-coordinate of point
        """

        if type(x) != int and type(x) != float:
            print("Bad type for x")
            sys.exit(-1)
        if type(y) != int and type(y) != float:
            print("Bad type for y")
            sys.exit(-1)
        self.x = x
        self.y = y


class Triangle:
    """
    Triangle class is implemented to check whether the entered point of triangle are correct
    """
    def __init__(self, a: tuple, b: tuple, c: tuple):
        # now calculate the length
        len_ab = ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5
        len_bc = ((b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2) ** 0.5
        len_ca = ((c[0] - a[0]) ** 2 + (c[1] - a[1]) ** 2) ** 0.5

        if len_ab + len_bc <= len_ca or len_bc + len_ca <= len_ab or len_ca + len_ab <= len_bc:
            print("Co-ordinate are false, triangle not formed.")
            sys.exit(-1)

        print("Triangle can form with given co-ordinates.")
        self.a = Point2D(a[0], a[1])
        self.b = Point2D(b[0], b[1])
        self.c = Point2D(c[0], c[1])

        self.ab = len_ab
        self.bc = len_bc
        self.ca = len_ca


t1 = Triangle((-3.5, -1.5), (1.5, 4.0), (3.0, 0.5))
print(t1.__dict__)
print(t1.__dict__['a'].__dict__)
print(t1.__dict__['b'].__dict__)
print(t1.__dict__['c'].__dict__)

