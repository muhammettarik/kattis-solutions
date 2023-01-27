numbers = int(input())
sum = 0

if(1 <= numbers <= 10):
    for i in range(numbers):
        mistakenNumber = input()
        if(10 <= int(mistakenNumber) <= 9999):
            powa = int(mistakenNumber[-1])
            numba = int(mistakenNumber[:-1])
            sum += numba**powa

if(sum <= 1000000000):
    print(sum)