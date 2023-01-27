count = int(input())

for i in range(count):
    sentence = input()
    if len(sentence) < 10:
        print()
        continue
    if sentence[:10] == "simon says":
        print(sentence[11:])
        continue
    print()
