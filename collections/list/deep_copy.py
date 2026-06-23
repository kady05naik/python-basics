import copy

matrix=[
    [1,2,3],
    [4,5,6]
]
matrixcpy=copy.deepcopy(matrix)
matrixcpy[1].append(7)
print("matrix",matrix)
print("matrixcpy:",matrixcpy)