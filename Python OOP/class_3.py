import sys
class Date:
	def __init__(self, day:int, month:int, year:int):
		self.dd = day
		self.mm = month
		self.yy = year

	def __str__(self):
		return f"{self.dd} / {self.mm} / {self.yy}"

class Mobile:

	def __init__(self, name:str, price:int, color:str, date):
		self.m_name = name
		self.m_price = price
		self.m_color = color
		self.datee = date
	

m = Mobile("Apple", 40000, "Product Red", Date(12, 2, 1019))
print(m.__dict__)

n = Mobile("Samsung", 76222, "Aqua Blue", Date(8, 7, 6261))
print(n.__dict__)

print(m.__dict__['datee'].__dict__)
print(n.__dict__['datee'].__dict__)

print(Date)

print(m.datee.yy)
