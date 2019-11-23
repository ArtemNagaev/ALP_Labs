# List
print('LIST')
numbers = [n for n in range(5)]
print('Original:', numbers)
numbers.remove(0)
print('Remove:', numbers)
numbers.extend(numbers)
print('Extend 1:', numbers)
numbers.extend([1, 0, 1])
print('Extend 2:', numbers)
numbers.insert(4, 0)
print('Insert:', numbers)
print('\n')

# Set
print('SET')
setA = {n for n in range(5)}
setB = {5 if n%2==0 else n for n in range(7)}
print('Set A', setA)
print('Set B', setB)
print('Union:', setA | setB)
print('Subset:', setB <= setA)
setA.add(5)
print('Add 5 in Set A:', setA)
print('Subset:', setB <= setA)
print('\n')

# Dictionary
print('DICTIONARY')
continent = ['Europe', 'Asia', 'North America', 'South America']
country = ['Germany', 'Singapore', 'USA', 'Peru']
dictionary = dict(zip(continent, country))
print('Orginal:', dictionary)
dictionary.update({'Africa' : 'Uganda'})
print('Update:', dictionary)
print('Contains:', 'South America' in dictionary)
print('Key = Asia:', dictionary['Asia'])