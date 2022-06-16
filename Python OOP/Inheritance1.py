class Employee:
	raise_percent = 1.04    # 4% of salary
	def __init__(self, f_name, l_name, pay):
		self.f_name = f_name
		self.l_name = l_name
		self.pay = pay

	def apply_raise(self):
		self.pay = self.pay * self.raise_percent


class Developer(Employee):
	raise_percent = 1.10
	def __init__(self, f_name, l_name, pay, pro_lang):
		super().__init__(f_name, l_name, pay)
		#Employee.__init__(self, f_name, l_name, pay)
		self.pro_lang = pro_lang


class Manager(Employee):			
	def __init__(self, f_name, l_name, pay, employees=None):
		super().__init__(f_name, l_name, pay)
		

		if employees is None:
			self.employees = []
		else:
			self.employees = employees

	def add_emp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)


	def print_emps(self):
		for emp in self.employees:
			print(f'-->{emp.f_name} {emp.l_name}')

e1 = Employee("John", "Marker", 40000)
print(e1.pay)
e1.apply_raise()
print(e1.pay)

print("*" * 20)
d1 = Developer("Riya", "Carter", 67000, "Python")
d2 = Developer("Saloni", "Corner", 56600, "SQL")
print(d1.pay)
# print(help(Developer))
d1.apply_raise()
print(d1.pay)
print(d1.pro_lang)

print("*" * 30)

mgr1 = Manager('Sue', 'Smith', 90000, [d1])
mgr1.print_emps()

mgr1.add_emp(d2)

mgr1.print_emps()

print('*' * 30)

print(isinstance(mgr1, Manager))
print(isinstance(mgr1, Employee))
print(isinstance(mgr1, Developer))

print('*' * 30)

print(issubclass(Developer, Employee))
print(issubclass(Manager, Employee))
print(issubclass(Employee, Employee))
print(issubclass(Employee, Developer))