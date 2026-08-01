def remove_duplicates(lst):
    dedup=[]
    for num in lst:
        if num not in dedup:
            dedup.append(num)
    return dedup

lst=[9,2,7,7,5,9]
print(remove_duplicates(lst))





