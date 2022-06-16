
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"{self.day} / {self.month} / {self.year}"


class CreditCard:
    def __init__(self, card_name, card_number, cvv, exp_date):
        self.card_name = card_name
        self.card_number = card_number
        self.cvv = cvv
        self.exp_date = exp_date

    def __str__(self):
        return f"{self.card_name} : {self.card_number}"


class Person:
    def __init__(self, name, credit_card, gender, salary, is_married, ph_number):
        self.name = name
        self.credit_card = credit_card
        self.gender = gender
        self.salary = salary
        self.is_married = is_married
        self.ph_number = ph_number

    def show(self):
        print(f"Name = {self.name} , Credit Card Details : {self.credit_card}, Gender : {self.gender}")
        print(f"Credit Card Number : {self.credit_card.card_number}")
        print(f"Credit Card CVV : {self.credit_card.cvv}")
        print(f"Credit Card Expiry Date : {self.credit_card.exp_date}")
        print(f"Current Salary : {self.salary}")

    def __str__(self):
        return f"{self.name}"

    def bonus_calculator(self, bonus):
        a = (self.salary * bonus) / 100
        return self.salary + a


p1 = Person('Nishant', CreditCard("NISHANT SANJAY KUMBHAR", 406040986586, 123, Date(12, 5, 2022)), 'Male', 98000, False, 9822310562)
p1.show()
print(p1)

new_salary = p1.bonus_calculator(3.5)
print(new_salary)

print('*' * 30)

print(Person.__mro__)
print(CreditCard.__mro__)
print(Date.__mro__)

