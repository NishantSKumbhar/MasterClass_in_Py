"""
@author : Nishant Sanjay Kumbhar
@goal : To Implement Class and Methods
"""


class Date:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

    def get_day(self) -> int:
        """
        :return: day component
        """
        return self.day

    def set_day(self, new_day) -> None:
        """
        Set the New day Component
        :param new_day: new day component
        :return: None
        """
        self.day = new_day

    def get_month(self) -> int:
        """
        :return: month component
        """
        return self.month

    def set_month(self, new_month) -> None:
        """
        Set the new Month Component
        :param new_month: new month Component
        :return: None
        """
        self.month = new_month

    def get_year(self) -> int:
        """
        :return: year component
        """
        return self.year

    def set_year(self, new_year) -> None:
        """
        Set the new Year Component
        :param new_year: new year Component
        :return: None
        """
        self.year = new_year


D = Date(2, 10, 2000)

dd = D.get_day()
print("Day:", dd)
D.set_day(25)
dd = D.get_day()
print("Modified day:", dd)

mm = D.get_month()
print("Month:", mm)
D.set_month(4)
mm = D.get_month()
print("Modified month:", mm)

yy = D.get_year()
print("Year:", yy)
D.set_year(2025)
yy = D.get_year()
print("Modified year:", yy)
