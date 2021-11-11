"""
@author : Nishant Sanjay Kumbhar
@goal   : Understand the concept of creating class object inside class
"""
import sys


class Main:
    """
    This is the main class where two number are accepted and in this class methods
    we add (or sub, multi, div) two numbers and then store them in variable but, the variable should be class
    object, so we send it to Main(variable) so new class object will be created
    ******************************************************************************
    what actually is going to happen is value-1 is class object and value-2 is also class
    object so their addition or whatever.. should be class object . so lets see
    """
    def __init__(self, num: int):
        """
        main class constructor
        :param num: accepts the number : int
        """
        if type(num) != int:
            print("Bad Type Parameter for Main class")
            sys.exit(-1)

        self.value = num

    def addition(self, other):
        add = self.value + other.value
        res = Main(add)
        return res
    
    def reminder(self, other1):
        remin = self.value % other1.value
        remind = Main(remin)
        return remind

    def show(self, param):
        print(param, self.value)


num1 = Main(5)
num1.show("num1 : ")
print(num1.__dict__)
num2 = Main(45)
num2.show("num2 : ")
print(num2.__dict__)
result = num1.addition(num2)
result.show("result of add : ")
print(result.__dict__)
result1 = num1.reminder(num2)
result1.show("result1 of reminder : ")
print(result1.__dict__)
