# def square(num):

# 	return num * num 

# a = square

# print(square)
# print(a(5))
#*****************************************************************************


# def square(num):

# 	return num * num 

# def cube(num):
# 	return num*num*num


# def my_map(square_fun, arg_list):   # Higher Order Function
# 	l = []
# 	for i in arg_list:
# 		l.append(square_fun(i))
# 	return l

# s = my_map(square, [1,2,3,4,5,6])
# print(s)
# c = my_map(cube, [1,2,3,4,5,6])
# print(c)

# ****************************************************************


# def outer(msg):
# 	a = 10
# 	def innner():
# 		print("In innner Function")
# 		print(f"{msg} : value inside outer : {a}")

# 	return innner

# print(locals())
# k = outer('Hello')
# print(locals())
# k()

#************************************************************

def html_tag(tag):
	def text_inside_tag(msg):
		print(f"<{tag}>{msg}</{tag}>")
	return text_inside_tag

h1 = html_tag('h1')
h1('Hello World')

p = html_tag('p')
p('lorem45')