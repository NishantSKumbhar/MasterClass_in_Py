"""
@author : Nishant Sanjay Kumbhar
@goal : Implement a complete class conccepts
"""
import sys


class Mobile:

	def __init__(self, name:str, price:int, color:str):
		self.m_name = name
		self.m_price = price
		self.m_color = color
	
	

m = Mobile("Apple", 40000, "Product Red")
print(m.m_price)
print(m.m_name)
print(m.__dict__)



"""

class Mobile:
	def __init__(self ,s:dict):
		self.__dict__ = s

s = {
	'name' : 'Samsung',
	'color': 'Aqua Blue',
	'price' : 98222
}
m = Mobile(s)

print(m.price)
print(m.name)
print(m.__dict__)
"""
