class Employee:
    # Class attributes

    def __init__(self,id, name, salary):
        # Instance variables (unique to each instance)
        self.id = id
        self.name = name
        self.salary = salary

    #Instance method
    def display(self):
        print(self.name)
        print(self.salary)

class   Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def greet(self):
        print(f'Hello, my name is {self.name}')

class Department:
    def __init__(self, id, department):
        self.id = id
        self.department = department


p1 = Person("John",36)
p1.greet()
#p1.department = Department(1,"Department 1")