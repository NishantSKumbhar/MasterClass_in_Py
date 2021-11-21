""""
@author : Nishant Sanjay Kumbhar
@goal : Example 1: Find the angle between two lines having slopes of 1, and 1/2 respectively.

Solution:

The gives slopes of the two lines are m1
= 1 and m2

= 1/2.

The formula to find the angle between the two lines is Tanθ = m1−m21+m1.m2

Tanθ = 1−1/21+1/2.1

Tanθ = 1/23/2

θ = Tan−113

Therefore, the angle between the lines is Tan−113.
****************************************************************************************************
Example 2: Find the angle between two straight lines having the equations 3x + 4y - 10 = 0, and 4x -5y + 2 = 0.

Solution:

The given two equations of the lines are 3x + 4y - 10 = 0, and 4x -5y + 2 = 0.

Here we have a1=3,b1=4,a2=4,b2=−5

The angle between the two lines can be calculated using the formula Tanθ = a2b1−a1b2 / a1a2+b1b2

.

Tanθ =4×4−3×(−5) / 3×4+4×(−5)

Tanθ =16+1512−20

Tanθ =31−8

θ =Tan−1−318

Therefore, the angle between the lines is Tan−1−318
.
"""
import sys
import math


class Equation:
    """
    this is class of equation to form equation data type i.e a , b, c
    """
    def __init__(self, a_var: float, b_var: float, c_var_const: float):
        """
        This is Equation class Constructor
        :param a_var: a  float
        :param b_var: b : float
        :param c_var_const: c : float
        """
        if type(a_var) != float and type(a_var) != int or type(b_var) != int and type(b_var) != float or type(c_var_const) != int and type(c_var_const) != float:
            print("bad type !")
            sys.exit(-1)

        self.a = a_var
        self.b = b_var
        self.c = c_var_const

        print(self.a, self.b, self.c)

    def get_angle(self, other_a2):
        """
        this is class method used to get angle between two lines using line equations
        :param other_a2: second line object
        :return: angle between two lines : float
        a1 = self.a       b1 = self.b       c1 = self.c
        a2 = other_a2.a   a2 = other_a2.b   a3 = other_a2.c

         Tanθ = a2b1−a1b2 / a1a2+b1b2

        """
        tan = ((other_a2*self.b) - (self.a*other_a2.b)) / ((self.a*other_a2.a) + (self.b*other_a2.b))
        r_angle = math.atan(tan)
        main_angle = Equation(r_angle, 0, 0)
        return main_angle


a1, b1, c1 = float(input("Enter the value of a1 of the First Equation : ")), float(input("Enter the value of b1 of the Second Equation : ")), float(input("Enter the value of c1 of the Second Equation : "))
e1 = Equation(a1, b1, c1)
a2, b2, c2 = float(input("Enter the value of a2 of the First Equation : ")), float(input("Enter the value of b2 of the Second Equation : ")), float(input("Enter the value of c2 of the Second Equation : "))
e2 = Equation(a2, b2, c2)

angle = e1.get_angle(e2)
