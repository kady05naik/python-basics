'''
Program to Reverse a List:

'''

def reverse_list(lst):
    lst.reverse()
    # lst[::-1]
    return lst

n=int(input(f'Enter Total number of list to be enter:'))
lst=[]
for i in range(n):
    lst.append(int(input(f'Enter lst[{i}] : ')))

print(f"Original: {lst}")
print(f'Reverse: {reverse_list(lst)}')