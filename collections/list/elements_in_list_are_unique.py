def check_unique(lst):
    unique=[]
    for num in lst:
        if num in unique:
            break
        else:
            unique.append(num)
    else:
        return True

    return False

lst=[1,3,4,6,7,8,8]
print(check_unique(lst))