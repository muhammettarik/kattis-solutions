amount = int(input())
sum = 0

if(1 <= amount <= 100):
    for i in range(amount):
        period = input()
        periods = period.split(" ")
        if((0 < float(periods[0]) <= 1) and (0 < float(periods[1]) <= 100)):
            sum += float(periods[0]) * float(periods[1])

print(sum)
