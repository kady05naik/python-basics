import heapq

def headq_merge_two_sorted_lists(list1, list2):
    return list(heapq.merge(list1, list2))


list1=[2,3,4,5,6,7,8,9]
list2=[1,4,9]
print(headq_merge_two_sorted_lists(list1, list2))


