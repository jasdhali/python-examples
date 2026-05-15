def greeting(name):
    print("Hello, " + name + "!")
def check_age(age):
    if age < 10:
        raise ValueError("Age must be greater than 0!")
    return f"Age set to {age} years old!"
try:
    print(check_age(-5))
except ValueError as e:
    print(f"Invalid inputL {e}")
#greeting("Jaspal")