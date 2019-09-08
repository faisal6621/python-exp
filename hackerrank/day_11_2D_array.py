# https://www.hackerrank.com/challenges/30-2d-arrays/
if __name__ == '__main__':
    arr = []
    max_sum = 0
    tmp_sum = 0
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    for i in range(4):
        for j in range(4):
            print(arr[i][j], arr[i][j + 1], arr[i][j + 2])
            print(arr[i + 1][j + 1])
            print(arr[i + 2][j], arr[i + 2][j + 1], arr[i + 2][j + 2])
            tmp_sum += arr[i][j] + arr[i][j + 1] + arr[i][j + 2]
            tmp_sum += arr[i + 1][j + 1]
            tmp_sum += arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
            print('tmp_sum=', tmp_sum)
            if i == 0 and j == 0:
                max_sum = tmp_sum
            elif tmp_sum > max_sum:
                max_sum = tmp_sum
            tmp_sum = 0
        print('max_sum=', max_sum)

    print(max_sum)
