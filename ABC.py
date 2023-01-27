line = input()
a, b, c = line.split()
a = int(a)
b = int(b)
c = int(c)

line2 = list(input())

max = max(a,b,c)
min = min(a,b,c)
mid = (a + b + c) - min - max

for i in line2:
    value = 0
    if i == "A":
        value = min
    elif i == "B":
        value = mid
    elif i == "C":
        value = max

    print(value, end=" ")