# 1: tuples are standard sequence data types containing heterogeneous data separated by comma
t = 1234, 25.75, 'Hello!'
print(t)

# 2: tuples are immutable, but they can be nested
# t[0] = "won't work" # TypeError: 'tuple' object does not support item assignment
u = t, 'xyz', (1, 5, 10)
print(u)

# 3: or can contain mutable objects (e.g., lists)
l = [5, 9, 25]
v = l, u
print(v)
l.insert(1, 36)
print(v)  # list has been updated and so the tuple

# 4: tuples are always enclosed in parentheses, so that nested tuples are interpreted correctly
# see output for above tuples

# 5: a special problem is the construction of tuples containing 0 or 1 items
empty_tuple = ()  # just parentheses to denote empty tuple
single_tuple = 'single',  # notice comma at the end
print(len(empty_tuple), 'item in empty_tuple', empty_tuple)
print(len(single_tuple), 'item in single_tuple', single_tuple)

# 6: originally comma separated items are packed into tuple and can be unpacked into variables too
x, y, z = t  # while unpacking variables on left side must be equal to items in the tuple
print('x =', x, 'y =', y, 'z =', z)
