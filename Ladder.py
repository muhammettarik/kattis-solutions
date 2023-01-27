import math

given = input()
height, angle = given.split(" ")

ladderLength = int(height) / math.sin(math.radians(int(angle)))

print(math.ceil(ladderLength))