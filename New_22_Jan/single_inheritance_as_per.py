"""
@author : Nishant Sanjay Kumbhar
@goal : implement  *** single inheritance *** from raj book ->Introduction to Computing and Problem Solving with Python  by- Jeeva jose and P. Sojan  lal
"""


class Mobile:
    def get_data_of_mobile(self, ram: int, rom: int, color: str):
        self.ram = ram
        self.rom = rom
        self.color = color

    def display_mobile(self):
        print(f"""
                    Hello There, hope you are Okay !
We have the Best Mobile Brand which has {self.ram} GB Ram and {self.rom} GB Internal Storage,
            which will available in {self.color} color.    
                """)


class My_mobile(Mobile):
    def get_specs(self, price: int, name: str):
        self.name = name
        self.price = price

    def display_my_specs(self):
        print(f"""
Here is Name of the product : {self.name} and Price strikes at {self.price} Rupees only.
                        """)


ram = int(input("Enter the Ram of Mobile : "))
rom = int(input("Enter the Rom of Mobile : "))
clr = input("Enter the Color of mobile : ")
name = input("Enter the Name of Mobile : ")
price = int(input("Enter the Price of Mobile : "))
print("Result : ")
my_mob = My_mobile()  # this is instance of child class
my_mob.get_data_of_mobile(ram, rom, clr)
my_mob.get_specs(price, name)
my_mob.display_mobile()
my_mob.display_my_specs()
