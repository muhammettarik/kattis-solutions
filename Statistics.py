import sys

case = 1

for line in sys.stdin:
    given = line.split(" ")
    numberCount = int(given[0])
    numbers = [int(number) for number in given[1:]]
    maximum = max(numbers)
    minimum = min(numbers)
    rang = maximum - minimum

    print("Case " + str(case) + ": " + str(minimum) + " " + str(maximum) + " " + str(rang))
    case += 1