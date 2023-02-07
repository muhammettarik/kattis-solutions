def factorize(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def play_second_player(x):
    factors = factorize(x)
    k = len(factors)
    return k

x = int(input())
print(play_second_player(x))
