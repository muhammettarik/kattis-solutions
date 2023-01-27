inp = int(input(''))

start = 4
b = 1

if(1 <= inp <= 15):
    while(b <= inp):
        start = pow((pow(start, 0.5) * 2) - 1, 2)
        b += 1

print(int(start))