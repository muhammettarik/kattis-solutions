numbers = input().split(" ")
a, b, c = [int(number) for number in numbers]

if a == b + c:
    print(str(a) + "=" + str(b) + "+" + str(c))
elif a == b - c:
    print(str(a) + "=" + str(b) + "-" + str(c))
elif a == b * c:
    print(str(a) + "=" + str(b) + "*" + str(c))
elif a == b / c:
    print(str(a) + "=" + str(b) + "/" + str(c))
elif a + b == c:
    print(str(a) + "+" + str(b) + "=" + str(c))
elif a - b == c:
    print(str(a) + "-" + str(b) + "=" + str(c))
elif a * b == c:
    print(str(a) + "*" + str(b) + "=" + str(c))
elif a / b == c:
    print(str(a) + "/" + str(b) + "=" + str(c))
