#
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def toString(self):
        return f'Employee first name {self.first} employee last name {self.last}'

