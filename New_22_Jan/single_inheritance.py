"""
@author : Nishant Sanjay Kumbhar
@goal : implement  *** single inheritance *** from raj book ->Introduction to Computing and Problem Solving with Python  by- Jeeva jose and P. Sojan  lal
"""
# look out this program carefully note the imp points


class Mobile:
    def __init__(self, ram: int, rom: int, color: str):
        """
        This is Base class Mobile Constructor:
        :param ram: ram size : int
        :param rom: rom size : int
        :param color: color of mobile : str
        :param price: price of mobile
        """
        self.ram = ram
        self.rom = rom
        self.color = color

    def display_mobile(self):
        print(f"""
            Hello There, hope you are Okay !
      We have the Best Mobile Brand which has {self.ram} GB Ram and {self.rom} GB Internal Storage,
      which will available in {self.color} color.    
        """)


class Redmi(Mobile):
    def __init__(self, name: str, price: int):
        """
        This is Derived class Redmi Constructor
        :param name: name of Mobile
        :param price: price of Mobile
        """
        Mobile.__init__(self, 5, 55, 'jj')
        self.name = name
        self.price = price

    def display_redmi(self):
        print(f"""
        Here is Name of the product : {self.name} and Price strikes at {self.price} Rupees only.
        """)


ram = int(input("Enter the Ram of Mobile : "))
rom = int(input("Enter the Rom of Mobile : "))
clr = input("Enter the Color of mobile : ")
name = "Note 10 Pro"
price = 19000
m1 = Mobile(ram, rom, clr)
red = Redmi(name, price)
red.display_mobile()
red.display_redmi()
