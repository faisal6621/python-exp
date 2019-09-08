# https://www.hackerrank.com/challenges/30-binary-numbers/
def swap_longest(t, l):
    if len(t) > len(l):
        l[:] = t
        t[:] = []
    else:
        t[:] = []


if __name__ == '__main__':
    N = int(input())
    binary = bin(N)
    longest_ones = []
    temp = []

    for b in binary[2:]:
        if int(b) == 0:
            swap_longest(temp, longest_ones)
        else:
            temp.append(b)

    swap_longest(temp, longest_ones)
    print(len(longest_ones))
