cases = int(input())

if(1 <= cases <= 20):
    for i in range(1,cases + 1):
        powerStrips = input()
        result = 0
        inputs = powerStrips.split(" ")
        if(1 <= int(inputs[0]) <= 10):
            for i in range(1, len(inputs)):
                if(2 <= int(inputs[i]) <= 10):
                    if(i == int(inputs[0])):
                        result += int(inputs[i])
                    else:
                        result += int(inputs[i]) - 1
        print(result)
