"""
@author : Nishant Sanjay kumbhar
@goal   : To write program to find roots of quadratic equation
"""


class Variable:
    """
    This is Variable Class i.e ax2 + bx + c , (a, b, c) are come here
    """
    def __init__(self, var: float):
        """
        This is Variable class Constructor
        :param var: it can be  a or b or c
        """
        self.var = var

    def root1(self, other_b, other_c):
        rot = (-other_b.var + ((other_b.var ** 2) - (4 * self.var * other_c.var)) ** 0.5) / (2 * self.var)
        root_obj = Variable(rot)
        return root_obj

    def root2(self, other_b, other_c):
        rot = (-other_b.var - ((other_b.var ** 2) - (4 * self.var * other_c.var)) ** 0.5) / (2 * self.var)
        root_obj = Variable(rot)
        return root_obj

    def show(self, aa, param_b, bb, param_c, cc, root_1, root_2):
        print(self.var, aa, param_b.var, bb, param_c.var, cc, root_1.var, root_2.var)


a = Variable(1)
print("a : ", a)
print("a.__dict__ : ", a.__dict__)


b = Variable(2)
print("b : ", b)
print("b.__dict__ : ", b.__dict__)


c = Variable(-15)
print("c : ", c)
print("c.__dict__ : ", c.__dict__)

r1 = a.root1(b, c)
print(r1)
print(r1.__dict__)
r2 = a.root2(b, c)
print(r2)
print(r2.__dict__)

a.show("x^2  ", b, "x ", c, " , for this Quadratic Equation roots will be : ", r1, r2)
