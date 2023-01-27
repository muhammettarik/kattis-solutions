days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
calendar = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
cursor = 3

dm = input()
dm = dm.split(" ")

totalMonth = 0

for i in range(int(dm[1]) - 1):
    totalMonth += calendar[i]

cursor += (int(dm[0]) - 1) + totalMonth
print(days[cursor % 7])
