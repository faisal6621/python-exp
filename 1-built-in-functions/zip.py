# 1: aggregating element from each of the iterables
zipped = zip('ABC', 'xyz')
print(*zipped)
# 2: should only be used with unequal length inputs when you don’t care about trailing
print(*zip('PQRS', 'mno', 'HIJKL'))

# 3: a good example is transposing a matrix
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print(*zip(*matrix))
