# 1: defining a function requires the keyword - def
def greet(name):
    """A nice way to entertain your guest is to greet them with welcome"""
    print("Welcome", name)


greet("Faisal")

# 2: functions can be assigned to another name, which serves as a renaming mechanism
welcome = greet;
welcome("Sandeep")

# 3: is greet a function or procedure? function returns some value while procedures don't
# but in Python 'None' (a built-in name) is returned if there is no return value
print(greet("Vivek"))


# 4: a function can have variable number of arguments
# 4.1: an argument can have a default value
def hello(name="World"):
    print("Hello", name)


hello()


# 4.2: a function can be called with Keyword argument
# https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


parrot(1000)  # 1 positional argument
parrot(voltage=1000)  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')  # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)  # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')  # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword
# but all the following calls would be invalid:
# parrot()                     # required argument missing
# parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
# parrot(110, voltage=220)     # duplicate value for the same argument
# parrot(actor='John Cleese')  # unknown keyword argument
