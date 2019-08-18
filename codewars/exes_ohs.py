# https://www.codewars.com/kata/55908aad6620c066bc00002a/
def xo(s):
    ex_oh = {'x': 0, 'o': 0}
    for char in s:
        if char == 'x' or char == 'X':
            ex_oh['x'] += 1
        if char == 'o' or char == 'O':
            ex_oh['o'] += 1

    return True if ex_oh['x'] == ex_oh['o'] else False


print(xo('ooxx'))
print(xo('xooxx'))
print(xo('ooxXm'))
print(xo('zpzpzpp'))
print(xo('zzoo'))
