def fl(lst):
    flat_list = []
    for item in lst:
        if isinstance(item, list):
            flat_list.extend(fl(item))
        else:
            flat_list.append(item)
    return flat_list

def sort(lst):
    if len(lst) <= 1:
        return lst
    
    mid = len(lst) // 2
    left = sort(lst[:mid])
    right = sort(lst[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)
    result.extend(left)
    result.extend(right)
    return result

variable = [12, 1, [22, 3, [8, 14]], 2, 6, [11], 90]
variable = sort(fl(variable))
print(variable)