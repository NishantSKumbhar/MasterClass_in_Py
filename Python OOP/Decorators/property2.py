class Employee:
	def __init__(self, first, last):
		self.first = first 
		self.last = last 
		#self.email = first + '.' + last + '@email.com'

	@property
	def email(self):
		return f"{self.first}.{self.last}@email.com"

	@property
	def full_name(self):
		return f"{self.first} {self.last}"

emp1 = Employee('nishant', 'kumbhar')
emp1.first = 'Sarang'
print(emp1.first)
print(emp1.last)
print(emp1.email) 
print(emp1.full_name)


emp1.email = "vipulgodase@hotmail.com"
emp1.full_name = "John Wick"
# this error will be solved by using setter