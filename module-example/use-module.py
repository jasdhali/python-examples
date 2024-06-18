import module
module.greeting('Jaspal')

a = module.person1['age']

print( a )

import platform
x = platform.system()

#x = platform.__annotations__
#y = platform.__path__

print(x)
from module import Person
from module import Employee

person = Person("Jaspal",30)

print(person)
print(person.method1('jas'))

