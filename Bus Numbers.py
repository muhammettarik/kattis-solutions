busCount = int(input())

buses = input()
buses = buses.split(" ")
buses = [int(bus) for bus in buses]
buses.sort()

output = []
start = buses[0]
end = buses[0]
for i in range(1, busCount):
    if buses[i] == end + 1:
        end = buses[i]
    else:
        if start == end:
            output.append(str(start))
        else:
            if end - start == 1:
                output.append(str(start))
                output.append(str(end))
            else:
                output.append(str(start) + '-' + str(end))
        start = buses[i]
        end = buses[i]

if start == end:
    output.append(str(start))
else:
    if end - start == 1:
        output.append(str(start))
        output.append(str(end))
    else:
        output.append(str(start) + '-' + str(end))

print(' '.join(output))
