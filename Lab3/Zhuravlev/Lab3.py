# List
print('LIST')
numbers = [-1 if n % 3 == 0 else n for n in range(12)]
numbers.append(0)
print(numbers)
print('count:', numbers.count(-1))
print('index:', numbers.index(-1, 4))
print('pop[1]:', numbers.pop(1))
print('pop[-2]:', numbers.pop(-2))
print(numbers, '\n')

# Set
print('SET')
setA = {1, 2, 3, 4, 7, 8, 10, 42, 1, 1, 1}
setB = {4, 8, 15, 16, 23, 42}
setC = [15]
print(setA)
print(setA - setB)
# print(setB ^ setC)
print(setB.symmetric_difference(setC), '\n')

# Dictionary
print('DICTIONARY')
continent = ['Europe', 'Asia', 'North America', 'South America']
country = ['Germany', 'Singapore', 'USA', 'Peru']
dictionary = dict(zip(['Europe', 'Asia', 'North America', 'South America'], ['Germany', 'Singapore', 'USA', 'Peru']))
print(dictionary)
print('South America' in dictionary)
print(dictionary['Asia'])
