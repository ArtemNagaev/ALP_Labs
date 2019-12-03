#Принимает число и считает для него число фибоначчи
def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

#Принимает лист чисел, для каждого из них считает число фибоначчи 
def fibList (numbers):
    for i in numbers:
        yield fib(i)

print("Вывод полученного листа при помощи итератора")
test = fibList([1,2,3])
print (next(test))
print (next(test))
print (next(test))

print("Вывод с использованием цикла for")
test = fibList([1,2,3])
for fibNumber in test:
    print (fibNumber)

print("Вывод переводом в список")
test = fibList([1,2,3])
print(list(test))

#Генератор листов также является генератором
print("Вывод списка полученного генератором списков")
test = (fib(n) for n in [1,2,3])
print (list(test))
