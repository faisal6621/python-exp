def find_smallest_int(arr):
    # Code here
    m = arr[0]
    for a in arr:
        if a < m:
            m = a
    return m


print(find_smallest_int([78, 56, 232, 12, 11, 43]))
