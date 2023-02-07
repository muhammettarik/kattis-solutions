while True:
    n, m = [int(number) for number in input().split(" ")]

    gameOver = False
    cost = 0

    heads = sorted([int(input()) for head in range(n)])
    knights = sorted([int(input()) for head in range(m)])

    if n > m:
        print("Loowater is doomed!")
        break

    if n == 0 and m == 0:
        break

    i = 0

    for head in heads:
        while i < len(knights) and head > knights[i]:
            i += 1

        if i >= len(knights):
            gameOver = True
            break

        cost += knights[i]

        i += 1

    if gameOver:
        print("Loowater is doomed!")
    else:
        print(cost)