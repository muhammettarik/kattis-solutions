roomDetails = input()
length, partitionCount = roomDetails.split(" ")

partitions = input()
partitions = ["0"] + partitions.split(" ") + [length]

spaces = []

for partition in partitions:
    for partition2 in partitions:
        if abs(int(partition) - int(partition2)) not in spaces:
            spaces.append(abs(int(partition) - int(partition2)))

spaces.pop(0)
spaces.sort()
for space in spaces:
    print(space, end=" ")