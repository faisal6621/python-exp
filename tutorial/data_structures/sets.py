# 1: set is an unordered collection with no duplicate elements.
basket = {"apple", "banana", "papaya", "apple", "orange", "banana"}
print(basket)  # duplicates will be removed and order will be different on each execution
# an empty set must be created with set() instead of {} otherwise this will be treated as dictionary
a = set('abracadabra')  # will have set of unique chars in the given input
b = set('ace')
print(a, b)

# 2: mathematical operations like union, intersection, difference, and symmetric difference are supported
print(a - b)  # letters in a but not in b
print(a | b)  # letters in a or b or both
print(a & b)  # letters in both a and b
print(a ^ b)  # letters in a or b but not in both
