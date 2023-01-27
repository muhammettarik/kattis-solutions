coordinates = input()
coordinates = coordinates.split(" ")

width = float(coordinates[0]) - float(coordinates[2])
height = float(coordinates[1]) - float(coordinates[3])
area = abs(width * height)

print(area)