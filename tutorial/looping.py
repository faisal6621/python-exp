# 1: looping on dictionaries: key and value can be retrieved at the same time using items()
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print('key:', k, 'value:', v, end=' | ')
print()

# 2: looping on sequence: position index and corresponding value retrived at the same time using enumerate()
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v, sep='=', end=' | ')
print()

# 3: looping on more than one sequence can be zipped to pair the entries using zip()
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

# 4: looping in reverse order
for i in reversed(range(1, 10, 2)):
    print(i, end=' ')
print()

# 5: looping in sorted order
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for fruit in sorted(set(basket)):
    print(fruit, end=' ')
print()
