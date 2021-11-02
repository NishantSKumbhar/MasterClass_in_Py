"""
@author: Yogeshwar
@goal: To demonstrate class statement through Date class.
"""


class Date:

    def __init__(self):   # callback function
        print("__init__:New object of class Date is created")
        print("__init__:id(self):", id(self))
        print("__init__:type(self):", type(self))
        print('----------------------------------------------------')

d1 = Date()     # new object
print("id(d1):", id(d1))
print("type(d1):", type(d1))

d2 = Date()
print("id(d2):", id(d2))
print("type(d2):", type(d2))
