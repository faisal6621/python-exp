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
