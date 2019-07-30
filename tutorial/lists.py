# 1: A comma separated values (items) between square ([]) brackets are called lists
squares = [1, 4, 9, 16, 25]
print(squares)

# 2: list are Sequence types and can be indexed and sliced
print(squares[2])  # print the 3rd item in the list
print(squares[-1])  # print the last item in the list

# 3: slicing returns a new list of requested elements. The following slice is a new (shallow) copy of the list
sliced_squares = squares[2:]  # slicing the list from index 2 (included) to the end
print(sliced_squares[1])

# 4: lists can be concatenated
squares += [36, 49, 65, ]
print(squares)

# 5: lists are mutable and their content can be changed
squares[7] = 64  # square of 8 is 64 not 65
print(squares)

# 6: assignment to slice of list is possible and can be used to
# 6.1: replace some values
letters = ['a', 'b', 'f', 'g', 'h']
letters[2:] = ['c', 'd', 'e']
print(letters)
# 6.2: remove those values
letters[2:4] = []
print(letters)
# 6.3: clear/empty list by replacing all
letters[:] = []
print(letters)

# 7: a built-in function len() can be used to find the size of the list
print("length of letters:", len(letters))
print("length of squares:", len(squares))

# 8: lists can also be nested. A list containing other lists
letters = ['a', 'b', 'c', 'd']
numbers_letters = [squares, letters]
print(numbers_letters)
