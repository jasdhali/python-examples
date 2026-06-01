#Take input from user and convert to integer
n = int(input("Enter number: "))

#Variable to store the num
s = 0
for i in range(1, n+1):
    s += i
print("Sum is " , s)