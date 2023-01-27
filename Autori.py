words = input()
words = words.split("-")

result = ""

for i in words:
    result += i[0]

print(result)