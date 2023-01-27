inp = input()
text = ""
temp = ""

if(1 <= len(inp) <= 250):
    for i in inp:
        if i != temp:
            text += i
        temp = i

    print(text)