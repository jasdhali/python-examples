def greeting(name):
    print("Hello," + name)

person1 = {
    "name": "John",
    "age": 36,
    "country": "Norway"
}
name = ''
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    #def __init__(self,age):        
    #    self.age = age

    def __str__(self):
        return 'Person s name is => '+ self.name

    def method1(self):
        print('hi -1')

    def method1(self,sal):
        self.sal = sal
        print('hi - 2')

class Employee(Person):
    def __init__(self,sal):
        self.salary = sal

    def __str__(self):
        return 'Employee name is => '+ self.name
  