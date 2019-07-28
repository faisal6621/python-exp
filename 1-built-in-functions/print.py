# 1: The old age "Hello World!"
print("Hello World!")
print('Hello, World!')

# 2: Printing objects
hello = "hello"
world = "world"
python = "python"
print(hello, world, python)  # hello world python

# 3: Separating objects using named parameter 'sep'
print(hello, world, python, sep=', ')  # hello, world, python

# 4: printing on multiple lines
fox_line = "The quick brown fox"
dog_line = "jumped over the lazy dog"
print(fox_line)  # same as 1
print(dog_line)  # same as 1

# 5: or keeping the cursor on same line at the 'end'
print(fox_line, end=", ")
print(dog_line)  # The quick brown fox, jumped over the lazy dog

# TODO using the 'file' and 'flush' named parameters
