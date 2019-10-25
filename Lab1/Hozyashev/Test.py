n = int(input("Введите n: "))
def factorial(n):
    if n == 0:
        return 1
    elif n < 0:
        print('n меньше нуля!')
    else:
        return n * factorial(n-1)
m=factorial(n)
print(m)
