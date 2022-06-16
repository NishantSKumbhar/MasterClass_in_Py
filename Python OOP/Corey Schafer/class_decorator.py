class decorated_class(object):
	def __init__(self, fun):
		self.fun = fun

	def __call__(self, *args, **kwargs):
		print("Hello")
		return self.fun(*args, **kwargs)

@decorated_class
def display():
	print("This is display function")


@decorated_class
def display_info(name, age):
	print(f"This Function has Argument {name} and {age}")

display()
display_info('Nishant', 22)