'''
Merge two Sorted List:
Write a Python function to merge two sorted lists into one sorted list.

'''

def merge_two_sorted_lists(lst1,lst2):
    lst3=lst1+lst2
    lst3.sort()
    return lst3



lst1=[1,3,7]
lst2=[3,4,6,8,9]
lst3=merge_two_sorted_lists(lst1,lst2)
print(lst3)