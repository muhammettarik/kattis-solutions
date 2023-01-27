n = int(input())

if n in range(2,101):
    sum = -(n-1)
    for i in range(n):
        leng = int(input())
        if leng in range(1,51):
            sum += leng

    print(sum)
