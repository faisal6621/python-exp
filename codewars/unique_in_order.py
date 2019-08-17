def unique_in_order(iterable):
    unique = []
    prev = None
    for item in iterable:
        if item != prev:
            unique.append(item)
            prev = item
    return unique


print(unique_in_order('AAAABBBCCDAABBB'))
print(unique_in_order('ABBCcAD'))
print(unique_in_order([1, 2, 2, 3, 3]))
print(unique_in_order(''))
print(unique_in_order([]))
