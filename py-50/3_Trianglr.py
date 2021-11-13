"""
@author : Nishant Sanjay Kumbhar
@goal   : To implement full Triangle Class
"""
import sys


class Point2D:
    """
    This Class is for point data type.
    Implementation of Two Dimensional point in cartesian coordinate system
    """

    def __init__(self, x: float, y: float):
        """
        This is Point2D Constructor .
        :param x: x co-ordinate of point2D object : float
        :param y: y co-ordinate of point2D object : float
        """
        # Now Type Checking
        if type(x) != int and type(x) != float:
            print("Bad type for x.")
            sys.exit(-1)

        if type(y) != int and type(y) != float:
            print("Bad type for y.")
            sys.exit(-1)

        self.x = x
        self.y = y

    def get_distance(self, other) -> float:
        """
        This is Point2D class method used to measure distance between
        :param other: object of other point object
        :return: distance between two points
        """
        dis = ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
        return dis


def type_check_triangle_parameter(t) -> bool:
    if type(t) != tuple:
        return False
    if len(t) != 2:
        return False
    if (type(t[0]) != int and type(t[0]) != float) or (type(t[1]) != int and type(t[1]) != float):
        return False
    return True


class Triangle:
    """
    This is The Main Class Of Triangle Implementation.....
    """

    def __init__(self, vertex_a: tuple, vertex_b: tuple, vertex_c: tuple):
        """
        This is Constructor of triangle Class
        :param vertex_a: co-ordinate of vertex 'a' in tuple form
        :param vertex_b: co-ordinate of vertex 'b' in tuple form
        :param vertex_c: co-ordinate of vertex 'c' in tuple form
        """
        if type_check_triangle_parameter(vertex_a) == False or type_check_triangle_parameter(
                vertex_b) == False or type_check_triangle_parameter(vertex_c) == False:
            print("Bad Type for Triangle Class Parameter")
            sys.exit(-1)

        self.vertex_a = Point2D(vertex_a[0], vertex_a[1])
        self.vertex_b = Point2D(vertex_b[0], vertex_b[1])
        self.vertex_c = Point2D(vertex_c[0], vertex_c[1])

        self.len_ab = self.vertex_a.get_distance(self.vertex_b)
        self.len_bc = self.vertex_b.get_distance(self.vertex_c)
        self.len_ca = self.vertex_c.get_distance(self.vertex_a)

        if self.len_ab + self.len_bc <= self.len_ca \
                or self.len_bc + self.len_ca <= self.len_ab \
                or self.len_ca + self.len_ab <= self.len_bc:
            print("Sum of lengths of two sides of a triangle must be greater than the other side")
            sys.exit(-1)

    def perimeter(self) -> float:
        peri = self.len_ab + self.len_bc + self.len_ca
        return peri

    def area(self) -> float:
        s = self.perimeter() / 2
        # A(triangle) = ((semi-perimeter) * (semi-perimeter - side1) * (semi-perimeter - side2)
        #               * (semi-perimeter - side3) ** 0.5
        ar = (s * (s - self.len_ab) * (s - self.len_bc) * (s - self.len_ca)) ** 0.5
        return ar

    def get_len_ab(self) -> float:
        return self.len_ab

    def get_len_bc(self) -> float:
        return self.len_bc

    def get_len_ca(self) -> float:
        return self.len_ca


T1 = Triangle((-4.5, -1.5), (1.5, 5.0), (4.5, 0.5))
P = T1.perimeter()
print("Perimeter of a triangle =", P)
A = T1.area()
print("Area of a triangle =", A)
print("L(AB)=", T1.get_len_ab())
print("L(BC)=", T1.get_len_bc())
print("L(CA)=", T1.get_len_ca())
