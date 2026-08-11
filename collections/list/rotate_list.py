def rotate_list(lst,k):
    temp=[]
    l=len(lst)-k
    for i in range(l,len(lst)):
        temp.append(lst[i])

    for i in range(l):
        temp.append(lst[i])

    return temp

lst=[10,20,30,40,50]
k=6
print(rotate_list(lst,k))