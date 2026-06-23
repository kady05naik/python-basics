# copying
lst=[1,2,8,4,5]
lst1=[7,8]

lst1=lst.copy()
print(lst1)

lst1.pop()
print("pop from list 2",lst1)

lst1.append(6)
print("append 6 list2:",lst, lst1)

matrix=[
    [1,2,3],
    [4,5,6]
]

matrixcpy=matrix.copy()
print(matrix,matrixcpy)
matrixcpy[1].append(9)
print(matrix,matrixcpy)

