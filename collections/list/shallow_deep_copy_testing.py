import copy
original=[
    [1,2,3],
    [4,5,6]
]
cy=copy.copy(original)
print(cy is original)             # False 
print(cy[0] is original[0])       # True

dpcpy=copy.deepcopy(original)
print(dpcpy is original)          # False
print(dpcpy[0] is original[0])    # False

