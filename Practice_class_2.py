"""
@author : Nishant Sanjay Kumbhar
@goal   : To Demonstrate Class in Python
"""


class Mobile:
    def __init__(self):
        print("This will print whenever the new class object will be created")
        self.name = "Apple"
        self.price = 1800
        self.processor = "A15_Bionic"
        print(self.name)
        print("id of self : ", id(self))
        print("type of self: ", type(self))


m = Mobile()
print("id of m : ", id(m))
print("type of m : ", type(m))
m.price = 8999        # imp
print(m.price)
print(m.name)
print(m.processor)
m1 = Mobile()
print("id of m1 : ", id(m1))
print("type of m1 : ", type(m1))
print(m1.price)
print(m1.name)
print(m1.processor)
