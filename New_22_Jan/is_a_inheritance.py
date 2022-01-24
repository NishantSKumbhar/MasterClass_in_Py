"""
@author : Nishant Sanjay kumbhar
@goal : implement is a relationship of inheritance..i.e  square is a Quadrilateral.
"""


class Quadrilateral:
    def __init__(self, a: int, b: int, c: int, d: int):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def perimeter(self):
        a = self.a + self.b + self.c + self.d
        return a


class Square(Quadrilateral):
    def __init__(self, side: int):
        Quadrilateral.__init__(self, side, side, side, side)
        self.side = side

    def diagonal(self):
        return self.side * (2 ** 0.5)


s = Square(5)
p = s.perimeter()
print(f"Perimeter of Square : {p}")
d = s.diagonal()
print(f"Diagonal of Square : {d}")
