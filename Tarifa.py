n = int(input())
sum = 0

if(n in range(1,101)):
    months = int(input())

    if(months in range(1,101)):
        for i in range(1,months+1):
            mb = int(input())
            if(mb in range(0,10000)):
                sum += n - mb

print(n + sum)