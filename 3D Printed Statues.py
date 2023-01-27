import math

n = int(input())

if(n in range(1,10001)):
    lo = int(math.log(n,2))
    print(math.ceil(lo + n/2**lo))