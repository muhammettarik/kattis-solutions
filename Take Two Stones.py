n = int(input())

if(n in range(1,10000000)):
    if(n & 1 == 1):
        print("Alice")
    else:
        print("Bob")