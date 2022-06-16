class Mobile:
	def __init__(self, name, price):
		self.name = name 
		self.price = price


	def show(self):
		print(f"Name : {self.name},  Price : {self.price}")


	def static_methods(mobiles_list):
		for i in mobiles_list:
			print(i)

	def __str__(self):
		return f"{self.name}"


Mobiles = [Mobile("Note 10 Pro", 20000),  Mobile("Note 5 Pro", 15000)]


#print(Mobiles[0].name)

Mobile.static_methods(Mobiles)
