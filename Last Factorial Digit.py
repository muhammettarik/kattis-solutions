def factorial(n):
    if n == 1:
        return 1
    else:
        return factorial(n-1) * n

cases = int(input())

for i in range(cases):
    n = int(input())
    f = factorial(n)
    print(str(f)[-1])