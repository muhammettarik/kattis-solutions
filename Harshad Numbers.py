number = input()

digitSum = 0

for digit in number:
    digitSum += int(digit)

number = int(number)

if number % digitSum == 0:
    print(number)

else:
    while True:
        number += 1
        digitSum = 0

        for digit in str(number):
            digitSum += int(digit)

        if number % digitSum == 0:
            print(number)
            break

