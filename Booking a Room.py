from random import randint

roomData = input()
roomCount, booked = roomData.split(" ")

if int(roomCount) == int(booked):
    print("too late")

else:
    rooms = []
    for i in range(int(booked)):
        rooms.append(int(input()))

    while True:
        randomRoom = randint(1, int(roomCount))
        if randomRoom not in rooms:
            print(randomRoom)
            break
