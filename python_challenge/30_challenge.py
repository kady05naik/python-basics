'''
Remove Duplicate in a List:
Write a Python program that removes any duplicate elements from the list and returns a new list with only unique elements.
'''

def remove_duplicates(lst):
    de_dup=[]
    for x in lst:
        if x not in de_dup:
            de_dup.append(x)
    return de_dup

lst=[]
n=int(input(f'Enter total number of list to be inserted: '))
for i in range(n):
    lst.append(int(input(f'Enter Element: ')))

print(f'Deduplicated List : {remove_duplicates(lst)}')