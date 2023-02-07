text = input()
length = len(text)
words = {}

for i in range(0, length, length // 3):
    word = text[i:i + length // 3]
    if word not in words:
        words[word] = 1
    else:
        print(word)
        break