s = input()
c = ""

if(3 <= len(s) <= 1000):
    for i in s:
        if(i == "e"):
            c += "ee"

    print("h" + c + "y")

