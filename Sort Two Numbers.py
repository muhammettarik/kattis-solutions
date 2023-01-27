number = input()
a, b = number.split(" ")
a = int(a)
b = int(b)

if(a in range(0,10000000) and b in range(0,10000000)):
    print(min(a,b), max(a,b))