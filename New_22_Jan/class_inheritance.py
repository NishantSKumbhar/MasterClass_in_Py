"""
@author : Nishant Sanjay Kumbhar
@goal : implement 'has a' type inheritance i.e Creditcard has a Date.
"""
import sys


class Date:
    def __init__(self, dd: int, mm: int, yy: int):
        """
        Constructor of Date Class.
        :param dd: day : int
        :param mm: month : int
        :param yy: year : int
        """
        if (type(dd) or type(mm) or type(yy)) != int:
            print("Date object unacceptable !")
            sys.exit(-1)
        self.dd = dd
        self.mm = mm
        self.yy = yy


class Creditcard:
    def __init__(self, name: str, cr_number: int, cvv: int, ex_date: Date):
        """
        Constructor of Credit-card class.
        :param name: name on creaditcard : str
        :param cr_number: card number : int
        :param cvv: cvv number : int
        :param ex_date: Expiry date of card: Date
        """
        self.name = name
        self.num = cr_number
        self.cvv = cvv
        self.date = ex_date

    def show(self):
        """
        This method is used to show/print the objects
        :return:
        """
        print(f"Hi, {self.name}, Your card Number is {self.num} and cvv : {self.cvv} which is going to expire at {self.date.dd}/{self.date.mm}/{self.date.yy}.")


c1 = Creditcard("Mr.Nishant Sanjay Kumbhar", 406040986586, 322, Date(23, 5, 2027))
print(c1.__dict__)  # this print the c1 object
print(c1.__dict__['date'].__dict__)  # this print date object
c1.show()
