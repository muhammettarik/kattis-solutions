numbers = []

def sumDigits(number):
    sum = 0
    while number > 0:
        sum = sum + number % 10;
        number = number // 10;

    return sum


while True:
    number = int(input())
    if number == 0:
        break

    for p in range(11, 999999999):
        if sumDigits(number) == sumDigits(number * p):
            print(p)
            break