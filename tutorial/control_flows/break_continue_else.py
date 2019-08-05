# 1: the break statement, breaks out the enclosing innermost for or while loop
for n in range(2, 15):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n // x)
            break
    else:  # this belongs to the for loop, not the if statement
        # this code block will run only if no break occurs above
        print(n, 'is prime')

# 2: the continue statement will continue on the next iteration
for n in range(1, 10):
    if n % 2 == 0:
        print(n, 'is even')
        continue
    print('skipping', n)


# https://docs.python.org/3/tutorial/controlflow.html#pass-statements
# 3: pass statement does nothing
def nothing():
    print('this is going to do nothing')
    pass


nothing()
