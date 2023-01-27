line = input()
a, b = line.split()
a = int(a)
b = int(b)

if(0 <= a <= 1000000 and 0 <= b <= 1000000 ):
    print(a + b)