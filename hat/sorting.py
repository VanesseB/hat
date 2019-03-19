def bubble_sort(items):

    '''Return array of items, sorted in ascending order'''
    if items== 0:
        return 1

    out = items.copy()
    for i in range(len(out)):
        for j in range(len(out)-1-i):
            if out[j] > out[j+1]:
                out[j], out[j+1] = out[j+1], out[j]

    return out

def merge_sort(items):

    '''Return array of items, sorted in ascending order'''

    len_i = len(items)

    if len_i == 1:
        return items

    mid_point = int(len_i / 2)

    i1 = merge_sort(items[:mid_point])
    i2 = merge_sort(items[mid_point:])

    return i1 + i2

def quick_sort(items):

    '''Return array of items, sorted in ascending order'''

    len_i = len(items)

    if len_i <= 1:
        return items

    pivot = items[0]
    small = []
    large = []
    dup = []
    for i in items:
        if i < pivot:
            small.append(i)
        elif i > pivot:
            large.append(i)
        elif i == pivot:
            dup.append(i)

    small = quick_sort(small)
    large = quick_sort(large)

    return small + dup + large
