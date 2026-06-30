'''
Maximum difference between two consecutive elements in a list:

Write a Python program to find the maximum difference between two consecutive 
elements in the list using a brute-force approach.

'''

def max_consecutive_difference(lst):
    max_dif=0
    for i in range(1,n):
        if abs(lst[i]-lst[i-1])> max_dif :
            max_dif=abs(lst[i]-lst[i-1])

    return max_dif

n=int(input(f'Enter Total number of list to be enter:'))
lst=[]
for i in range(n):
    lst.append(int(input(f'Enter list[{i}]: ')))

print(f'The maximum difference is between is: {max_consecutive_difference(lst)}')