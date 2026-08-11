def merge_lists_to_dictionary(keys, values):
    result=dict()
    if len(keys)==len(values):
        for i in range(len(keys)):
            result[keys[i]]=values[i]
        return result
    else:
        return False

keys = ['a', 'b', 'c']
values = [1, 2, 3]

print(merge_lists_to_dictionary(keys, values))