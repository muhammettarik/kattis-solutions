size = int(input())

list = []

for i in range(size):
    element = input()
    list.insert(0, element)

for element in list:
    print(element)

# 75 Points

n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))

for i in range(n-1, -1, -1):
    print(numbers[i])

# 100 Points

n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))

for i in numbers[::-1]:
    print(i)

# 100 Points

def reverse_list(arr):
    left = 0
    right = len(arr) - 1
    while (left < right):
        # Swap
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left += 1
        right -= 1

    return arr


n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))

reversed = reverse_list(numbers)

for i in reversed:
    print(i)

# 100 Points