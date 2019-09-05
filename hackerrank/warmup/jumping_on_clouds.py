# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    safe_position = 0
    jumps = 0
    N = len(c)
    for i in range(N):
        if i == safe_position:
            if N - i == 3 or N - i == 2:
                jumps += 1
                safe_position = N  # end
                # print('j=', jumps, 's=', safe_position, end='| ')
                break
            if c[i + 2] == 0:
                jumps += 1
                safe_position += 2
                # print('j=', jumps, 's=', safe_position, end='| ')
                continue
            if c[i + 1] == 0:
                jumps += 1
                safe_position += 1
                # print('j=', jumps, 's=', safe_position, end='| ')

    # print('total jumps=', jumps)
    return jumps


if __name__ == '__main__':
    jumpingOnClouds([0, 1, 0, 0, 1, 0, 0, 0, 1, 0])
    jumpingOnClouds([0, 1, 0, 1, 0, 1, 0])
    jumpingOnClouds([0, 0, 1, 0, 1, 0, 1, 0])
