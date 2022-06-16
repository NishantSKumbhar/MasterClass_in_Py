def nishant_decorator(gun):
	def inner():
		print("Nishant Function Calling")
		return gun()
	return inner

@nishant_decorator
def addition():
	print(f"Addition is 32")


addition()
