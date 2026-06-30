'''
Rotate a List:
Write a Python function to rotate the list to the right by k positions without 
using slicing.

'''

def rotate_list(lst, k):
    lst1=[]
    lst2=[]
    lst.reverse()
    lst1=lst[:k]
    print(lst1)
    lst1.sort()
    lst2=lst[k:]
    lst2.sort()
    lst=lst1+lst2
    return lst

lst=[10,20,30,40,50]

k=3
print(lst[k])
print(rotate_list(lst, k))