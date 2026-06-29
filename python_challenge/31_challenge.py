'''
Check if all elements in a list are Unique
'''

def unique(n):
    lst=[]
    for i in n:
        if i in lst:
            flag=False
            break
        else:
            lst.append(i)
    else:
        flag= True
    
    return flag

n=int(input(f'Enter total number of elements to be inserted: '))
lst=[]
for i in range(n):
    lst.append(int(input(f'Enter lst[{i}]: ')))

print(f'Are all entered elements Unique: {unique(lst)}')