cases = int(input())

if cases in range(1,51):
    for i in range(cases):
        inputs = input()
        sg = inputs.split(" ")
        students = int(sg[0])
        if students in range(1, 1001) and len(sg) == students + 1:
            sum = -students
            abv = 0
            for i in sg:
                sum += int(i)
            avg = sum / students
            for i in range(0,len(sg)):
                if(int(sg[i]) > avg and i != 0):
                    abv += 1
            print('{:.3f}'.format(abv/students * 100) + "%")

