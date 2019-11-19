import random


def func(arr, n, count):
    if n == 0:
        return count
    if arr[n - 1] == 0:
        return func(arr, n - 1, count + 1)
    if arr[n - 1] != 0:
        return func(arr, n - 1, count)


arr = [random.randint(-1, 1) for n in range(10)]  # array
n = 10  # array length
count = 0  # count zero elements
print(arr)
print('Count of zero elements:', func(arr, n, count))
