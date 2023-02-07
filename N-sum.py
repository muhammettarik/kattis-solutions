count = int(input())

numbers = input()
numbers = numbers.split(" ")

sayilar = []

for number in numbers:
    sayilar.append(int(number))

print(sum(sayilar))