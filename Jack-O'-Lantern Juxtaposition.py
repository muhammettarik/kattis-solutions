inp = input('')
ara = inp.split(' ')

if(1 <= int(ara[0]) <= 500 and 1 <= int(ara[1]) <= 500 and 1 <= int(ara[2]) <= 500 ):

    result = int(ara[0]) * int(ara[1]) * int(ara[2])
    print(result)
