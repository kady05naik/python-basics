letters=['a','b']
# Matrix

letters.insert(1,'c')
print('insert:',letters)

matrix=[
    ['a','b'],
    ['c','d']
]
matrix.insert([2][0],['l','m'])
print('insert:',matrix)


# Append
letters=['a','b']
letters.append('c')
print(letters)

matrix=[
    ['a','b'],
    ['c','d']
]
matrix.append(['e','f'])
print(matrix)


# clear
letters=['a','b']
letters.clear()
print(letters)


# remove()
letters=['a','b','a','d']
letters.remove('b')
print(letters)

letters=['a','b','a','d']
letters.remove(letters[2])
print(letters)

matrix=[
    ['a','b'],
    ['c','d'],
    ['e','f']
]
matrix.remove(['e','f'])
print(matrix)

matrix=[
    ['a','b'],
    ['c','d'],
    ['e','f']
]
matrix[2].remove('f')
print(matrix)


# pop
letters=['a','c','b','c','a']
letters.pop(3)
print(letters)

letters=['a','c','b','c','a']
letters.pop()
print(letters)

matrix=[
    ['a','b'],
    ['c','d'],
    ['e','f']
]
matrix.pop()
print(matrix)

matrix=[
    ['a','b'],
    ['c','d'],
    ['e','f']
]
matrix[2].pop(0)
print(matrix)