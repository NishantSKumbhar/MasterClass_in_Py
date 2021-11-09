"""
@author: Yogeshwar
@Goal: To implement triangle class
"""

import sys


class Point2D:
    """
    Implementation of Point2D class.
    """

    def __init__(self, x: float, y: float):
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
    Implementation of Triangle Class
    """

    def __init__(self, A: Point2D, B: Point2D, C: Point2D):
        if type(A) != Point2D or type(B) != Point2D or type(C) != Point2D:
            print("Bad type for vertex A or B or C")
            sys.exit(-1)
        self.A = A
        self.B = B
        self.C = C


T1 = Triangle(Point2D(-3.5, 1), Point2D(0.0, 4.5), Point2D(3.5, 2.5))
print(T1.__dict__)
print(T1.__dict__['A'].__dict__)
print(T1.__dict__['B'].__dict__)
print(T1.__dict__['C'].__dict__)

# another type :
"""
class Triangle:  
    def __init__(self, pt_A: tuple, pt_B: tuple, pt_C: tuple):
        self.A = Point2D(pt_A[0], pt_A[1])
        self.B = Point2D(pt_B[0], pt_B[1])
        self.C = Point2D(pt_C[0], pt_C[1])

T1 = Triangle((-3.5, 1), (0.0, 4.5), (3.5, 2.5))
"""