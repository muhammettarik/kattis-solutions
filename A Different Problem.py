import sys

for line in sys.stdin:
    a, b = line.split(" ")
    a, b = [int(number) for number in [a, b]]

    print(abs(a - b))
