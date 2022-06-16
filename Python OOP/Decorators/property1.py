class Employee:
	def __init__(self, first, last):
		self.first = first 
		self.last = last 
		self.email = first + '.' + last + '@email.com'

	def full_name(self):
		return f"{self.first} {self.last}"

emp1 = Employee('nishant', 'kumbhar')
emp1.first = 'Sarang'
print(emp1.first)
print(emp1.last)
print(emp1.email)    # although first is changed to Sarang but mail will be nishant.kumbhar@gmai.com
print(emp1.full_name())