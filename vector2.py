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

    def addition(self, other):
        x_addition = self.x + other.x
        y_addition = self.y + other.y
        v_addition = Vector2D(x_addition, y_addition)
        return v_addition

    def subtraction(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def dot_product(self, other) -> float:
        return self.x * other.x + self.y * other.y

    def show(self) -> None:
        print("(", self.x, ",", self.y, ")")


v1 = Vector2D(1.1, 4.5)
v2 = Vector2D(-3.5, 1.2)

v1.show() # (1.1, 4.5)
v2.show() # (-3.5, 1.2)

v1_magnitude = v1.get_length()
v1_angle = v1.get_angle()

print("magnitude(v1):", v1_magnitude)
print("angle(v1):", v1_angle)

vector_addition = v1.addition(v2)
vector_subtraction = v1.subtraction(v2)

print("addition_vector:")
vector_addition.show()

print("Subtraction vector:")
vector_subtraction.show()

result = v1.dot_product(v2)
print("Dot product of v1 and v2:", result)