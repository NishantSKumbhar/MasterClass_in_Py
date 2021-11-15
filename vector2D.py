"""
@author: Yogeshwar
@goal: Implement 2D vector with methods
"""

import math


class Vector2D:
    """
    Implementation of directed line segment in 2D space.
    """
    def __init__(self, head_x: float, head_y: float):
        """
        Constructor of Vector2D (vector is line joining
        (0, 0)  ->   (head_x, head_y)
        tail    ->  head
        :param head_x: x coordinate of head point of a vector
        :param head_y: y coordinate of head point of a vector
        """
        self.x = head_x
        self.y = head_y

    def get_length(self) -> float:
        # (x**2 + y**2) ** 0.5
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_angle(self) -> float:
        # theta = tan-1(y/x)
        return math.atan(self.y/self.x)

    def show(self) -> None:
        print("(", self.x, ",", self.y, ")")


v1 = Vector2D(1.1, 4.5)
v2 = Vector2D(-3.5, 1.2)

v1.show()
v2.show()

v1_magnitude = v1.get_length()
v1_angle = v1.get_angle()

print("magnitude(v1):", v1_magnitude)
print("angle(v1):", v1_angle)
