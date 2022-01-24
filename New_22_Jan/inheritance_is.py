"""
@author : Nishant Sanjay Kumbhar
@goal : is s relation deep
"""


class Employee:
    def __init__(self):
        """
        Constructor of Employee Class
        """
        self.emp_sal = 30000

    def get_salary(self) -> int:
        return self.emp_sal


class Manager(Employee):
    def __init__(self):
        Employee.__init__(self)

    def get_salary(self) -> float:            # override the class behaviour
        manager_sal = Employee.get_salary(self)
        real_manager_salary = manager_sal * 1.3
        return real_manager_salary


nishant = Employee()
nishant_salary = nishant.get_salary()
print(f"Nishant Salary : {nishant_salary}")
bucky_robert = Manager()
bucky_salary = bucky_robert.get_salary()
print(f"Manager Bucky Salary is : {bucky_salary}")
