t = tuple('abx')
print(t)

uname,domain = 'jasdhali@gmail.com'.split('@')
print(uname)
print(domain)

d = {'a':0,'b':1,'c':2}
print(d)
t = d.items();
print(t)

if __name__ == "__main__":
   print("File one executed when ran directly")
else:
   print("File one executed when imported")