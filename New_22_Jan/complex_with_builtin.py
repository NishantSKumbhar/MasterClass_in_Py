"""
@author : Nishant Sanjay kumbhar
@goal : addition, multiplication , subtraction, .. of complex number..
"""


class Complex:
    def __init__(self, n1: int, n2: int):
        """
        This is Complex Class Constructor
        :param n1: real part of complex number .
        :param n2:  imaginary part of complex number.
        """
        self.real = n1
        self.img = n2

    def __add__(self, other):
        """
        This is Built-in Function to add two Complex Numbers
        :param other: second complex number object formal parameter.
        :return: object of type Complex which include addition of two Complex Numbers.
        """
        r_add = self.real + other.real
        i_add = self.img + other.img
        a = Complex(r_add, i_add)
        return a

    def __sub__(self, other):
        """
        This is Built-in Function for Subtraction.
        :param other: second complex number object formal parameter.
        :return: object of type Complex which include subtraction of two Complex Numbers.
        """
        r_sub = self.real - other.real
        i_sub = self.img - other.img
        a = Complex(r_sub, i_sub)
        return a

    def __mul__(self, other):
        """
        This is Built-in Function for Multiplication.
        :param other: object of type Complex which include Multiplication of two Complex Numbers.
        :return: return the Dot Product of two Complex numbers : int
        """
        return (self.real * other.real) + (self.img * other.img)

    def show(self, other):
        """
        this is class method to show/print the complex number.
        :param other: Any type of string suitable for purposes.
        :return: None
        """
        print(f"{other} Complex Number is {self.real} + {self.img} i")


c1 = Complex(2, 7)
c2 = Complex(5, 2)
c1.show("first")
c2.show("Second")
addition = c1 + c2     # here we can also use c1.__add__(c2)           which is called OOP syntax.
addition.show("Addition of")
subtraction = c1 - c2  # also use c1.__sub__(c2)
subtraction.show("Subtraction of")
multiplication = c1 * c2
print(f"Multiplication of Complex Number is {multiplication}")
