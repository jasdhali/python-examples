#Created By : Jaspal Singh Dhaliwal
# Source: https://pynative.com/python-basic-exercise-for-beginners/?__cf_chl_f_tk=f9Rpc6pTmj_HaznHIWWWFxdTgcQx8J98NwvfO2wJRo4-1782754755-1.0.1.1-NJ67aI7cGuzR0KJei0Art07a.VxrIOu6uki5snznJPY
# https://pynative.com/python-exercises-with-solutions/
#
#
def add_or_multiply_two_numbers(a, b,operation):
    if operation == "+":
        return a+b
    elif operation == "*":
        return a*b

print(add_or_multiply_two_numbers(20,30,'*'))
print(add_or_multiply_two_numbers(40,30,'+'))
