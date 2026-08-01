# combining
letter=['a','b','c']
numbers=[1,2,3]
comb=letter+numbers
print("+",comb)

letter=['a','b','c']
numbers=[1,2,3]
comb=letter*2
print("*",comb)

letter=['a','b','c']
numbers=[1,2,3]
letter.extend(numbers)
print("extend",letter)


letter=['a','b','c']
num=[1,2,3]
com=zip(letter,num)
print(com)


letter=['a','b','c']
num=[1,2]
com=list(zip(letter,num))
print(com)


letter=['a','b','c']
num=[1,2]
com=list(zip(letter,num,"Hello"))
print(com)