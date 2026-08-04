def linear_search(arr, target):
    arr_size=len(arr)
    for ind in range(0,arr_size):
        if arr[ind]==target:
            return ind
            break
    else:
        return -1


arr=[3,6,7,8,0]
target=0

print(linear_search([], 5))