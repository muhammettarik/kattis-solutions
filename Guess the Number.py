start = 1
end = 1000
mid = int((start + end)/2)
lives = 10

while lives > 0:
    guess = mid
    print(guess)

    info = input()

    if(info == "higher"):
        start = guess + 1
    elif(info == "lower"):
        end = guess - 1
    elif(info == "correct"):
        break

    mid = int((start + end) / 2)
    lives -= 1