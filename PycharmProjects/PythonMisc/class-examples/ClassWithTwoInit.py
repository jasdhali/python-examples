class Dog:
    kind = 'canine'     #class
    def __init__(self,name_v):
        self.name = name_v

    def greet(self):
        print('hi user')

d = Dog('goofy')
e = Dog('rocky')
print(d.greet());

print(function.__doc__)
#print(d.greet().__name__)