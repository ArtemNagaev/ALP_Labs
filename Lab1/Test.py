n = int(input("Введите n: "))
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
m=factorial(n)
print(m)