# TODO: All coding practices (module docstring, class docstring, function docstring, type checking)


class Point2D:
    def __init__(self, x: float, y: float):
        """

        :param x:
        :param y:
        """

        self.x = x
        self.y = y


class Circle:
    def __init__(self, c_center: tuple, c_radius: float):
        """

        :param c_center:
        :param c_radius:
        """
        self.c_center = Point2D(c_center[0], c_center[1])
        self.c_radius = c_radius


C = (5.5, 6.5)
print("type(C):", type(C))
R = 3.0

C1 = Circle(C, R)

print(C1.__dict__)
print(C1.__dict__['c_center'].__dict__)



