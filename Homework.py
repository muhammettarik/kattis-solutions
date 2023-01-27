problems = input()
problems = problems.split(";")

totalProblems = 0

for problem in problems:
    if "-" in problem:
        edges = problem.split("-")
        totalProblems += int(edges[1]) - int(edges[0])
    totalProblems += 1

print(totalProblems)

# 100 Points