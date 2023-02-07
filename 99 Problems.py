number = int(input())

remainder = number % 100

if number < 149:
    number = 99
else:
    if remainder >= 49:
        number += 99 - remainder
    else:
        number -= remainder + 1

print(number)