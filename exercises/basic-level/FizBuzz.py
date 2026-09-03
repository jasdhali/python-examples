for i in range(1,20+1):
    if (i % 3 == 0) & (i % 5 == 0):
        print("FizzBuuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
