tempCount = int(input())

temps = input().split()
temps = [int(temp) for temp in temps]

count = 0

for i in temps:
    if i < 0:
        count += 1

print(count)