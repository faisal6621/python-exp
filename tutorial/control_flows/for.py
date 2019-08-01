# https://docs.python.org/3/tutorial/controlflow.html#for-statements
# 1: unlike other languages in Python you can iterate over the items of any sequence (list, string) in order they appear
for w in "Hello World":
    print(w, end=" ")
print()  # just for a new line

words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))
    # it is possible to modify list during iteration but it may have consequences
    # if len(w) == 3:
    #     words.insert(1, w)

# 2: using range() for iterating over sequence of numbers
for i in range(0, 10):  # range generates arithmetic progressions
    print(i, end=",")
print()  # just for a new line

# 3: combining range() with len() to iterate over a sequence
for i in range(len(words)):
    print(i, words[i])

# 4: or use enumerate to have index and the item at the same time from the sequence
for index, item in enumerate(words, start=5):  # with 'start' you can specify the first index
    print(item, index)
