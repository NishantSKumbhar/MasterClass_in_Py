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

 1 radian = 57.2958 degrees
"""
import math
import cmath


class Equation:
    """
    this is class of equation to form equation data type i.e a , b, c
    """
    def __init__(self, a_var: int, b_var: int, c_var_const: int):
        """
        This is Equation class Constructor
        :param a_var: a  float
        :param b_var: b : float
        :param c_var_const: c : float
        """
        """if type(a_var) != float and type(a_var) != int or type(b_var) != int and type(b_var) != float or type(c_var_const) != int and type(c_var_const) != float:
            print("bad type !")
            sys.exit(-1)"""

        self.a = a_var
        self.b = b_var
        self.c = c_var_const

        # print(self.a, self.b, self.c)

    def get_angle(self, other_a2):
        """
        this is class method used to get angle between two lines using line equations
        :param other_a2: second line object
        :return: angle between two lines : float
        a1 = self.a       b1 = self.b       c1 = self.c
        a2 = other_a2.a   a2 = other_a2.b   a3 = other_a2.c

         Tanθ = a2b1−a1b2 / a1a2+b1b2

        """
        """a = other_a2 * self.b
        print(a)
        b = self.a * other_a2.b
        c = self.a * other_a2.a
        d = self.b * other_a2.b

        tan = (a - b) / (c + d)
        r_angle = math.atan(tan)
        main_angle = Equation(r_angle, 0, 0)
        return main_angle"""
        # Tanθ = a2b1−a1b2 / a1a2+b1b2
        print(self.a)
        print(other_a2.a)
        """
        a1 = self.a       b1 = self.b       c1 = self.c
        a2 = other_a2.a   b2 = other_a2.b   a3 = other_a2.c
        """
        a = self.b * other_a2.a
        b = self.a * other_a2.b
        c = self.a * other_a2.a
        d = self.b * other_a2.b
        print(a)
        print(b)
        print(c)
        print(d)
        tan1 = a - b
        tan2 = c + d
        print(tan1)
        print(tan2)
        final = tan1 / tan2
        print("div :", final)
        if final < 0:
            final = final * -1
        tan_theta = math.atan(final)
        print(tan_theta)
        degrees = tan_theta * 57.2958
        print("Final angle between lines is : ", degrees)


    def show(self):
        print("a : ", self.a)
        print("b : ", self.b)
        print("c : ", self.c)


e1 = Equation(1, -1, 4)
e1.show()
e2 = Equation(1, 0, 7)
e2.show()
print(type(e1))
print(type(e2))
print(e1.__dict__)
print(e2.__dict__)
final = e1.get_angle(e2)
#final = e1.get_angle(e2)

"""a1, b1, c1 = float(input("Enter the value of a1 of the First Equation : ")), float(input("Enter the value of b1 of the Second Equation : ")), float(input("Enter the value of c1 of the Second Equation : "))
e1 = Equation(a1, b1, c1)
a2, b2, c2 = float(input("Enter the value of a2 of the First Equation : ")), float(input("Enter the value of b2 of the Second Equation : ")), float(input("Enter the value of c2 of the Second Equation : "))
e2 = Equation(a2, b2, c2)

angle = e1.get_angle(e2)
-1.3182420510168371
"""
