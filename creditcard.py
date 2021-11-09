"""
@author : Yogeshwar
@goal : To implement a credit card class
"""

class Date:
    """Date class"""
    def __init__(self, init_day:int, init_month:int, init_year:int):
        """
        Constructor of Date Class
        :param init_day: day component of date
        :param init_month: month component of date
        :param init_year: year component of date
        """
        #TODO : Add Type and Value  Checking

        self.day = init_day
        self.month = init_month
        self.year = init_year


class CreditCard:
    def __init__(self, cc_name: str, cc_number: int, cc_valid_thru: Date, cc_expiry: Date, cc_cvv: int):
        """
        Constructor of Creditcard
        :param cc_name: card holder name
        :param cc_number: card number
        :param cc_valid_thru: issue date of card
        :param cc_expiry: Expirey date of card
        :param cc_cvv: cvv number on card
        """
        # TODO : Add Type and Value  Checking
        self.cc_name = cc_name
        self.cc_number = cc_number
        self.cc_valid_thru = cc_valid_thru
        self.cc_expiry = cc_expiry
        self.cc_cvv = cc_cvv


Card_1 = CreditCard("Yogeshwar Shukla", 55566666665, Date(1,12, 2020), Date(1, 12, 2000), 123)
