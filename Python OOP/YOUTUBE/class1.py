class Mobile:
	def __init__(self, name, price):
		self.name = name 
		self.price = price


	def show(self):
		print(f"Name : {self.name},  Price : {self.price} , RAM : {self.ram}")

	# static methods means they are does not contain self.
	# they can be called by class name.function()
	def static_methods():
		print("Hello Static Method")


m1 = Mobile("Note 10 Pro", 20000)
m1.ram = 89
m1.show()
print(m1.__dict__)
Mobile.static_methods()