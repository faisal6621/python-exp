# dictionaries are "set" of "key:value" pairs where the key must be immutable type
# dictionaries in python maintains insertion order
# in other programming languages such data structure is knows as "associative array" or "map"

# 1: dictionary must be enclosed in {}
cards = {'jack': 11, 'queen': 12, 'king': 13}
print(cards)

# 2: retrieving an element from dictionary
print(cards['king'])
print(cards.get('queen'))

# 3: adding item in dictionary
cards['ace'] = 1
cards['total'] = 50
print(cards)

# 4: updating a key's value
cards['total'] = 52
print(cards)

# 5: using del statement for deletion. deleting non-existent key results in error
del cards['total']

# 6: testing if element is present with the key
print('ace' in cards)
print('total' in cards)

# 7: getting list of all keys
# 7.1: in insertion order
print(list(cards))
# 7.2: in sorted order
print(sorted(cards))

# 8: dic() constructor builds dictionaries directly from sequences of key-value pairs
seq = [('one', 1), ('two', 2), ('three', 3), ('hundred', 100)]
numbers = dict(seq)
print(numbers)

# 9: When the keys are simple strings, it is sometimes easier to specify pairs using keyword arguments
cards.update(types=4)
print(cards)
print(dict(three=3, five=5, seven=7))
