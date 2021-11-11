"""
@author : Nishant Sanjay Kumbhar
@goal   : To implement class Mobile
"""

import sys


class cam:
    """
    This is Class is implemented because of we need camera data type in Mobile Class.
    """

    def __init__(self, rear: int, wide: int, macro: int):
        """
        Constructor of cam class
        :param rear: rear camera in Mega_pixel :int
        :param wide: wide angle camera in MP : int
        :param macro: macro sensor in MP    : int
        """
        if type(rear) != int or type(wide) != int or type(macro) != int:
            print("Bad Type parameter to cam class")
            sys.exit(-1)
        self.rear = rear
        self.wide = wide
        self.macro = macro


class Mobile:
    def __init__(self, company: str, series: str, model_no: int, camera: tuple, price: int):
        """
        This is Mobile Class Constructor
        :param company: name of Company : str
        :param series: series name : str
        :param model_no: model no in series : int
        :param camera: all camera defined in cam class : cam
        :param price: market retail price : int
        """

        if type(company) != str or type(series) != str or type(model_no) != int or type(camera) != tuple or type(price) != int:
            print("Bad Type parameter to Mobile Class")
            sys.exit(-1)

        self.company = company
        self.series = series
        self.model_no = model_no
        self.camera = cam(camera[0], camera[1], camera[2])
        self.price = price

    def show_name(self, param1):
        print(param1, self.company, " -> ", self.series, self.model_no, "Pro")
        

nishant = Mobile("Xiaomi", "Note", 10, (64, 12, 5), 19000)
print("nishant.__dict__ : ", nishant.__dict__)
print('nishant.__dict__["camera"].__dict__ : ', nishant.__dict__["camera"].__dict__)
nishant.show_name("Name of the Mobile : ")
