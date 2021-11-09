"""
@author : Jidnesh
@goal : Check Triangle by taking points
"""


class Point2D:
    def __init__(self, pt1: float, pt2: float):
        """
          @return : object initialization
        """
        self.x = pt1
        self.y = pt2

    def get_points(self):
        return [self.x, self.y]


class Triangle:
    def __init__(self, A: Point2D, B: Point2D, C: Point2D):
        """
        @return : Object initialization
        """
        self.X = A
        self.Y = B
        self.Z = C

    def distance(self, A: Point2D, B: Point2D) -> float:
        """
        @return : The distance between two points
        """
        x1, y1 = A.get_points()
        x2, y2 = B.get_points()
        distance = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5
        return distance

    def check_triangle(self):
        d_XY = self.distance(self.X, self.Y)
        d_YZ = self.distance(self.Y, self.Z)
        d_ZX = self.distance(self.Z, self.X)

        if (d_XY + d_YZ) > d_ZX and (d_YZ + d_ZX) > d_XY and (d_ZX + d_XY) > d_YZ:
            return "Triangle can be form"
        else:
            return "Invalid co-ordinates"


x = Point2D(3, 5)
y = Point2D(10, 12)
z = Point2D(4, 8)

T1 = Triangle(x, y, z)
d = T1.check_triangle()
print(d)

x = Point2D(-3.5, -1.5)
y = Point2D(1.5, 4.0)
z = Point2D(3.0, 0.5)

T2 = Triangle(x, y, z)
d = T2.check_triangle()
print(d)

x = Point2D(5, 5)
y = Point2D(1, 1)
z = Point2D(-2, -2)

T3 = Triangle(x, y, z)
d = T3.check_triangle()
print(d)