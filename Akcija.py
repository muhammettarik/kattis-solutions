n = int(input())
liste = []
toplam = 0

for i in range(n):
    x = int(input())
    liste.append(x)

liste.sort(reverse=True)

for i in range(len(liste)):
    if i % 3 != 2:
        toplam += liste[i]

print(toplam)