'''
Sum of List Elements:
Write a Python function that calculates the sum of all elements in a given list of integers.
'''

def sum_numbers(lst):
    return sum(lst)

lst=[]
n=int(input(f'Enter Total Number you want to insert in list: '))
for i in range(n):
    lst.append(int(input(f"Enter list[{i}]: ")))

print(lst)
print(f'Sum of list: {sum_numbers(lst)} ')

