def my_def(N):
    start, end = 0, N
    i, j = 0, 0
    for j in range(start, end):
        arr[i][j] = j + 1
        temp = arr[i][j] - 1

    while arr[i][j] < N*N:
        for i in range(start, end):
            arr[i][j] = temp + 1
            temp = arr[i][j]
        temp = temp - 1

        for j in range(end-1, start-1, -1):
            arr[i][j] = temp + 1
            temp = arr[i][j]
        temp = temp - 1

        for i in range(end-1, start, -1):
            arr[i][j] = temp + 1
            temp = arr[i][j]
        temp = temp - 1

        for j in range(start, end-1):
            arr[i][j] = temp + 1
            temp = arr[i][j]
        temp = temp - 1

        start = start + 1
        end = end - 1


T = int(input())

for tc in range(T):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    my_def(N)

    print(f'#{tc + 1}')
    # print(arr)
    for index in arr:
        result = ' '.join(str(i) for i in index)
        print(result)
