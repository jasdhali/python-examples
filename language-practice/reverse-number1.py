num = 534
print(f"Module for {num} is {num%10}")
d = num//10
print(f" {d}")

while num > 0:
    d = num // 10
    x = num % 10
    #print(f"{num} ")
    print(f"{d} ==== {x}")
    num //= 10