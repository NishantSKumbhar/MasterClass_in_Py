"""
@author : Nishant Sanjay Kumbhar
@goal   : implement class and class methods for people id verification
"""
import sys


class Birth_date:
    def __init__(self, day: int, month: int, year: int):
        """
        this is a Birth date class constructor , used to store date of birth
        :param day: day parameter : int
        :param month: month parameter : int
        :param year: year parameter : int
        """
        if type(day) != int or type(month) != int or type(year) != int:
            print("Bad Type Parameter for date of Birth")
            sys.exit(-1)
        self.dd = day
        self.mm = month
        self.yy = year


class Id:
    def __init__(self, name: str, dob: tuple, gender: str, is_graduate: bool, blood_gp: str, height: float,
                 mob_no: int):
        """
        this is Class Id Constructor
        :param name: name of man or women : str
        :param dob: date of birth : tuple
        :param gender: male or female or shemale : str
        :param is_graduate: person is graduate or not : bool
        :param blood_gp: Blood Group of Person : str
        :param height: height of the person
        :param mob_no: Mobile Number of person
        """
        if type(name) != str or type(dob) != tuple or type(gender) != str or type(is_graduate) != bool or type(blood_gp) != str or \
                (type(height) != float and type(height) != int) or type(mob_no) != int:
            print("Bad Type Parameters for Id Class !")
            sys.exit(-1)

        self.name = name
        self.dob = Birth_date(dob[0], dob[1], dob[2])
        self.gender = gender
        self.is_graduate = is_graduate
        self.blood_gp = blood_gp
        self.height = height
        self.mob_no = mob_no

    def age(self) -> bool:
        present_year = 2021
        result_age = present_year - self.dob.yy  # imp : see how to access element
        if result_age >= 21:
            return True
        return False


shubhkd = Id("Shubham", (1, 11, 2000), "Male", False, "B+ve", 189, 8788986522)
print(shubhkd.__dict__)
print(shubhkd.__dict__['dob'].__dict__)
age_is = shubhkd.age()
print(age_is)
