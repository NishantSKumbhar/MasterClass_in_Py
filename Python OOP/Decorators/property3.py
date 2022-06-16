class Employee:
	def __init__(self, first, last):
		self.first = first 
		self.last = last 
		#self.email = first + '.' + last + '@email.com'

	@property
	def email(self):
		return f"{self.first}.{self.last}@email.com"

	@email.setter
	def email(self, mail):
		m , s = mail.split('@')
		first, last = m.split('.')
		self.first = first
		self.last = last

	@property
	def full_name(self):
		return f"{self.first} {self.last}"

	@full_name.setter
	def full_name(self, name):
		first, last = name.split(' ')
		self.first = first
		self.last = last

	@full_name.deleter 
	def full_name(self):
		print("Deleted The full_name")
		self.first = None
		self.last = None

emp1 = Employee('nishant', 'kumbhar')
emp1.first = 'Sarang'
print(emp1.first)
print(emp1.last)
print(emp1.email) 
print(emp1.full_name)


emp1.email = "vipul.godase@hotmail.com"
#emp1.full_name = "John Wick"
# this error will be solved by using setter

print(emp1.email)

print(emp1.first)

del emp1.full_name