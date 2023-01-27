number = input()
numbers = number.split(' ')
isZero = False

for i in numbers:
    if("0" in i):
        isZero = True

if(numbers[0] != numbers[1] and not isZero):
    if(int(numbers[0][::-1]) > int(numbers[1][::-1])):
        print(numbers[0][::-1])
    else:
        print(numbers[1][::-1])