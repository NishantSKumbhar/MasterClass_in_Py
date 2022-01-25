"""
@author : Nishant Sanjay Kumbhar
@goal : implement  *** Invoking the Base class Constructor *** from raj book ->Introduction to Computing and Problem Solving with Python  by- Jeeva jose and P. Sojan  lal
"""
# look out this program carefully note the imp points


class Mobile(object):
    def __init__(self, ram: int, rom: int, color: str):
        """
        This is Base class Mobile Constructor:
        :param ram: ram size : int
        :parom rom: rom size : int
        :param color: color of mobile : str
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
    def __init__(self, ram: int, rom: int, color: str, name: str, price: int):
        """
        This is Derived class Redmi Constructor
        :param name: name of Mobile
        :param price: price of Mobile
        """
        super().__init__(ram, rom, color)
        """if we use this line then note has all parameters or only two will there"""
        self.name = name
        self.price = price

    def display_redmi(self):
        print(f"""
        Here is Name of the product : {self.name} and Price strikes at {self.price} Rupees only.
        """)


ram = int(input("Enter the Ram of Mobile : "))
rom = int(input("Enter the Rom of Mobile : "))
clr = input("Enter the Color of mobile : ")
name = input("Enter the name of mobile : ")
price = int(input("Enter the Price of Mobile : "))

note = Redmi(ram, rom, clr, name, price)
print(note.__dict__)
note.display_mobile()
note.display_redmi()
