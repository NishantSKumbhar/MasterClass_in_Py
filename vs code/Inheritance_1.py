"""
@author : Nishant Sanjay Kumbhar
@goal : To Implement the Inheritance Concept.
"""
import sys


class Quadrilateral:
    def __init__(self, a: int, b: int, c: int, d: int):
        """
        This is the Constructor of Quadrilateral
        :param a: side 1 of quadrilateral.
        :param b: side 2 of quadrilateral.
        :param c: side 3 of quadrilateral.
        :param d: side 4 of quadrilateral.
        """

        acceptable_type = [int, float]
        if (type(a) not in acceptable_type or type(b) not in acceptable_type or type(c) not in acceptable_type or type(
                d) not in acceptable_type):
            print("Bad Type For Side of Quadrilateral")
            sys.exit(-1)

        if a + b + c < d or b + c + d < a or c + d + a < b or d + a + b < c:
            print("Bad Value For Side of Quadrilateral.")

        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def get_perimeter(self) -> float:
        peri = self.a + self.b + self.c + self.d
        return peri

    def get_area(self) -> float:
        semi = self.get_perimeter() / 2
        return ((semi - self.a) * (semi - self.b) * (semi - self.c) * (semi - self.d)) ** 0.5


q1 = Quadrilateral(13, 14, 3, 13)
area = q1.get_area()
print(area)
peri = q1.get_perimeter()
print(peri)
