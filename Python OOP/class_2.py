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
	
	def compare(self, other):
		print(f"Name of 1 : " + self.m_name + "  ---- Name of 2 : " + other.m_name) 
		print(f"Price of 1: {self.m_price} ---- Price of 2: {other.m_price}")
		print(f"Color of 1: {self.m_color} ---- Color of 2: {other.m_color}")
		



	

m = Mobile("Apple", 40000, "Product Red")
print(m.__dict__)

n = Mobile("Samsung", 76222, "Aqua Blue")
print(n.__dict__)

m.compare(n)

