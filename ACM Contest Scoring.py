problems = {}
score = 0
count = 0

while True:
    attempt = input()

    if attempt == "-1":
        break

    result = attempt.split(" ")
    if result[1] not in problems:
        problems[result[1]] = 0

    if result[2] == "wrong":
        problems[result[1]] += 1

    if result[2] == "right":
        score += int(result[0]) + (problems[result[1]] * 20)
        count += 1

print(count, score)