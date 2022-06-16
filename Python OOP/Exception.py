try:
	a = 8
	if a == 8:
		raise AttributeError 
except AttributeError:
	print("AttributeError happend")
except Exception as e:
	print(e)

else:
	print('It runs only when does not throws exception')
finally:
	print('It will exicute whatever happend')