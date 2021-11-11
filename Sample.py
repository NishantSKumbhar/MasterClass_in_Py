import sys


def nana():
    print("Nishant")


class BIG:
    print("This will print first !- 1")

    def __init__(self, param_1, param_2):
        print("param_1 : ", param_1)
        self.p1 = param_1
        self.p2 = param_2
        print("HI : Constructor")
        print(self.p2)
        if type(self.p2) != int:
            print("Error")
            sys.exit(-1)
        print("param 2: ", param_2)
        print("param 1: ", param_1)

    print("This will print first ! - 2")

    # print(self.p2)  : NameError

    def show(self):
        print("HI : in class method i.e class function")
        print(self.p2)
        add = self.p1 + self.p2
        print(add)


    def tempo(self, n1, n2):
        print("self.p1 : ", self.p1)
        tp = self.p1 + self.p2
        sp = n1 + n2
        ttp = self.p1 + n2 + n1 + self.p2
        print(ttp)
        self.num1 = n1        # here it gives warning but not error
        self.num2 = n2
    """
    it is ok to send variable like n1 and n2 , but python says if you want your object have variable 
    then send it through constructor . 
    so it is good to send them while the object is being created i.e constructor
    as self.p1 and self.p2 are accessible in tempo so from this we understand that always send 
    the variables of object through constructor.
    as it is easier to use...
    
    """
    def lmp(self):
        print("self.num2 : ", self.num2)

    def create_obj(self, x):
        add = obj1.p1 + x.p1
        add1= obj1.p2 + x.p2
        res = BIG(add, add1)
        return res


a = 88
print(a)

obj1 = BIG(78, 88)
print(obj1.p2)
print(obj1.p1)
obj1.show()
nana()
obj1.tempo(45, 100)
obj1.lmp()
obj2 = BIG(100, 1000)
summation = obj1.create_obj(obj2)
print("Summation__dict : ",summation.__dict__)
summation.show()
