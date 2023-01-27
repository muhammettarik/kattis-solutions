while True:
    edges = input()
    if edges == "0 0 0":
        break

    a, b, c = edges.split(" ")
    a, b, c = [int(edge) for edge in [a, b, c]]

    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b

    if a * a + b * b == c * c:
        print("right")
    else:
        print("wrong")