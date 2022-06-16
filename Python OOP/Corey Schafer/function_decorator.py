# def decorator_function(fun):
# 	def inner():
# 		fun()

# 	return inner

# def display():
# 	print("This is a Display Function")


# decorated_display = decorator_function(display)

# decorated_display()


# #**************************************************************
# def decorator_function(fun):
# 	def inner():
# 		print("This is how we can modify the function")
# 		fun()

# 	return inner

# def display():
# 	print("This is a Display Function")


# decorated_display = decorator_function(display)

# decorated_display()

#**************************************************************
# def decorator_function(fun):
# 	def inner():
# 		print("This is how we can modify the function")
# 		fun()

# 	return inner


# @decorator_function
# def display():
# 	print("This is a Display Function")

# display()

#**************************************************************
def decorator_function(fun):
	def inner(*args, **kwargs):
		print("This is how we can modify the function")
		fun(*args, **kwargs)

	return inner


@decorator_function
def display():
	print("This is a Display Function")

@decorator_function
def display_info(name, age):
	print(f"This Function has Argument {name} and {age}")

display()

display_info('Nishant', 22)