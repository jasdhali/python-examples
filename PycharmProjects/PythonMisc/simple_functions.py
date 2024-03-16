def is_divisible(x, y):
    if x % y == 0:
        return True
    else:
        return False


res = is_divisible(11, 2)
print(res)


def add_all(t):
    total = 0
    for x in t:
        total += x
    return total


