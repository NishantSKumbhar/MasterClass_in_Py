"""
@author : Nishant Sanjay Kumbhar
@goal   : To Demonstrate Class in Python
"""


class Mobile:
    def __init__(self, name, company, is_refurbished, price, processor, battery, rated):
        print("This will print whenever the new class object will be created")
        self.nAme = name
        self.cOmpany = company
        self.iS_refurbished = is_refurbished
        self.pRice = price
        self.pRocessor = processor
        self.bAttery = battery
        self.rAted = rated
        print(name)
        print(id(name))
        print(type(name))
        print(self.nAme)
        print(id(self.nAme))
        print(type(self.nAme))


m = Mobile("iPhone 13 Pro Max", "Apple", False, 2000, "A-15 Bionic", 4500, 'A')
m1 = Mobile("iPhone 12 Pro Max", "Apple", True, 890, "A-14 Bionic", 3800, 'B')
