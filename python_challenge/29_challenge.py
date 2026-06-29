'''
Largest Element in a List:
Write a Python function that finds and returns the largest element in a given list 
of integers.

'''
def find_largest(numbers):
    return max(numbers)

n=int(input(f'Enter total number of elements to be enter insert :'))

lst=[]
for i in range(n):
    lst.append(int(input(f'Enter list[{i}]: ')))

print(f'Max element in the list: {find_largest(lst)}')