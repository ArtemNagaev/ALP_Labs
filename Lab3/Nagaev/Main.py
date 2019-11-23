# Использование листов
print ("Использование листов:")
numbers = [10 if n % 2 == 0 else n for n in range(20)]
print ("Исходный массив:")
print (numbers)
numbers.reverse()
print ("Развёрнутый массив:")
print (numbers)
numbers.clear()
print ("Очищенный массив:")
print (numbers)

numbers = [10 if n % 2 == 0 else n for n in range(20)]
numberClon = numbers.copy()
numbers.pop()
print ("Исходный массив:")
print (numbers)
print ("Скопированный массив массив:")
print (numberClon)


# Использование множеств
print ("\n Использование множеств:")
setA = {10 if n % 3 == 0 else n for n in range(20)}
setB = {10 if n % 5 == 0 else n for n in range(20)}
print("Множество А: ", setA)
print("Множество B: ", setB)
print("Пересечение: ", setA & setB)
setA^=setB
print("Симметрическая разность: ", setA)


# Использование словарей
print ("\n Использование словарей:")
RussianWords = ['Россия', 'Привет', 'Спасибо']
print('Русские слова:', RussianWords)
EnglishWords = ['Russia', 'Hello', 'Thanks']
print('Английские слова:', EnglishWords)
REDictionary = dict(zip(RussianWords, EnglishWords))
print('Словарь:', REDictionary)
print('Перевод слова привет:', REDictionary['Привет'])
REDictionary['До свидания'] = 'Good bye'
print('Добавление нового элемента', REDictionary)
