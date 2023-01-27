text = input()

if(len(text) < 80):
    words = text.split(" ")
    d = {}
    text = "yes"
    for i in words:
        if i.isupper():
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

    for i in d:
        if d[i] > 1:
            text = "no"
            break

    print(text)
