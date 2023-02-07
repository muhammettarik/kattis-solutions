n, k = input().split(" ")
n = int(n)
k = int(k)

sum = 0

for i in range(k):
    judge = int(input())
    sum += judge

if n == k:
    print(sum / k, sum / k)

else:
    minimum = (sum + (n - k) * -3) / n
    maximum = (sum + (n - k) * 3) / n
    print(minimum, maximum)
