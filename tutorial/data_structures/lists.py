# 1: lists are treated as sequences (discussed earlier in tutorial/lists.py).
# discussing here: methods available on list object
# https://docs.python.org/3/tutorial/datastructures.html#data-structures
from builtins import list
from collections import deque

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

# returns the number of times an item appeared in the list
apple_count = fruits.count('apple')
tangerine_count = fruits.count('tangerine')
print('there are', apple_count, 'apples and', tangerine_count, 'tangerine')

# returns zero-based index in the list of first item which is equal to the given value
banana_index1 = fruits.index('banana')
banana_index2 = fruits.index('banana', banana_index1 + 1)  # Find next banana starting from last index
print('the banana is found at', banana_index1, 'and', banana_index2, 'indexes')

# reversing the order of the list
fruits.reverse()
print('reversed', fruits)

# adding a new item at the end of the list
fruits.append('grape')
print('appended', fruits)

# adding a new item at the given index in the list
fruits.insert(2, 'papaya')
print('inserted', fruits)
# sorting the list
fruits.sort(key=lambda fruit: (len(fruit), fruit))
print('sorted by length', fruits)
fruits.sort()
print('default sort', fruits)

# return the last item by removing from the list
fruit = fruits.pop()
print('popped', fruit, 'from', fruits)

# 2: lists as stack
# since stacks have "last-in, first-out" operation, list's append and pop helps in achieve this
stack = [1, 2, 3]
print('original stack', stack)
stack.append(4)
stack.append(5)
print('updated stack', stack)
popped = stack.pop()
print('popped', popped, 'from', stack)

# 3: lists as queue
# since queues have "first-in, first-out" operation, pops from the beginning of a list is slow
queue = deque(stack)
print('original queue', queue)
queue.append(5)
print('updated queue', queue)
popleft = queue.popleft()
print('removed', popleft, 'from', queue)

# 4: list comprehensions
# concise way to create list
# 4.1: old school - looping
squares = []
for i in range(10):
    squares.append(i ** 2)
print(squares)

# 4.2: functional style - lambda and in-built methods
cubes = list(map(lambda x: x ** 3, range(10)))
print(cubes)

# 4.3: concise and comprehensive
twice = [x * 2 for x in range(10)]
print(twice)

# 4.4: more comprehensive (complex?)
pairs = [(x, y) for x in [1, 2, 3] for y in [3, 4, 1] if x != y]
print(pairs)

# 4.5: nested list comprehension (more complex?). e.g., transposing a matrix
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
transpose = [[row[i] for row in matrix] for i in range(4)]
# In the real world, you should prefer built-in functions to complex flow statements.
# The zip() function would do a great job for this use case
print(transpose)
