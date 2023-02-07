potionTime = input().split(" ")
potionCount, duration = [int(number) for number in potionTime]

potions = []

for i in range(potionCount):
    potions.append(int(input()))

potions = sorted(potions, reverse=True)

i = 0
passed = True

while i < len(potions):

    if i > 0:
        for j in range(i-1, -1, -1):

            potions[j] -= duration
            if potions[j] <= 0:
                print("NO")
                passed = False
                break
    i += 1

if passed:
    print("YES")
