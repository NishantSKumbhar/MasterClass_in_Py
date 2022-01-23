"""
@author : Nishant Sanjay Kumbhar
@goal : sending self from one to another.
"""


class Self:
    def __init__(self, n1: int, n2: int, n3: int):
        """
        Constructor of Self.
        :param n1: :)
        :param n2: :)
        :param n3: :)
        """
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3

    def average(self):
        ave = (self.n1 + self.n2 + self.n3) / 3
        return ave

    def percentage(self, other):
        return other / 100


n = Self(4, 5, 6)
a = n.average()
print(a)
j = n.percentage(987)
print(j)
