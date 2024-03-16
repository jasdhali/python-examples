# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import physics
from physics import AngularMomentum
from physics import InvalidAgeException
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

ang_mom = AngularMomentum("jaspal")

print("@@@"+ang_mom.__str__())
print(ang_mom)
myage = 20;

try:
    if myage > 18:
        print("Hello buddy")
    else:
        raise InvalidAgeException
except InvalidAgeException:
    print("Exception occurred: Invalid Age")
