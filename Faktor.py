line = input()
a, b = line.split()
a = int(a)
b = int(b)

if 1 <= a <= 100 and 1 <= b <= 100:
    print(a * (b-1) + 1)