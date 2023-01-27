inp = input('')
ara = inp.split(' ')

a = 1

if(1 <= int(ara[0]) < int(ara[1]) <= int(ara[2]) <= 100):
    while(a <= int(ara[2])):
        if(a % int(ara[0]) == 0):
            if (a % int(ara[1]) == 0):
                print("FizzBuzz")
            else:
                print("Fizz")
        elif(a % int(ara[1]) == 0):
            if (a % int(ara[0]) == 0):
                print("FizzBuzz")
            else:
                print("Buzz")
        else:
            print(a)
        a += 1