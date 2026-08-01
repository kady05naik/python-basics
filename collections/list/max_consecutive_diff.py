def max_consecutive_difference(lst):
    max=0
    if len(lst)<=1:
        return "Add more elements to compare"
    else:
        for ind in range(1,len(lst)):
            if abs(lst[ind-1]-lst[ind])>max:
                max=abs(lst[ind-1]-lst[ind])
        return max

lst=[1,1,2]
print(max_consecutive_difference(lst))
