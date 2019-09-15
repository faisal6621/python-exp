# https://www.hackerrank.com/challenges/ctci-array-left-rotation/
def rotLeft(a, d):
    left = a[0:d]
    right = a[d:]
    result = []
    result.extend(right)
    result.extend(left)
    return result

if __name__ == '__main__':
    result = rotLeft([1, 2, 3, 4, 5], 4)
    print(' '.join(map(str, result)))
