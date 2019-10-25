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

#####


def is_exist(num1, num2, num3):
    if num1 < num2 + num3 and num2 < num1 + num3 and num3 < num1 + num2:
        return True
    else:
        return False


a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))

if is_exist(a, b, c):
    print('Треугольник существует')
    if a ** 2 + b ** 2 == c ** 2:
        print('Треугольник прямоугольный')
    elif a ** 2 + b ** 2 > c ** 2:
        print('Треугольник остроугольный')
    elif a ** 2 + b ** 2 < c ** 2:
        print('Треугольник тупоугольный')
else:
    print('Треугольник не существует')
