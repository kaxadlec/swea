def my_def(n):
    i, j = 0, 0
    start, jump = 1, n
    if n == 1:
        arr[0][0] = 1
        return arr
    else:
        for value in range(n):
            arr[i][j] = value + 1
            j = j + 1

    start = n
    print(start, 'start')
    # while value <= n:
    for value in range(start, start + jump):
        arr[i][j] = value
        i = i + 1
    return arr






T = int(input())
for tc in range(T):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    my_def(N)

    # if arr[i][j] == 1:
    #     for value in range(1, N):
    #         j = j + 1   # 위치 옆으로 이동
    #         arr[i][j] = value+1
    # if arr[i][j] == N:
    #     for value in range(N+1, N*2):
    #         i = i + 1
    #         arr[i][j] = value
    # if arr[i][j] == N*2-1:
    #     for value in range(N*2, N*3-1):
    #         j = j - 1
    #         arr[i][j] = value
    # if arr[i][j] == N*3-2:
    #     for value in range(N*3-1, N*4-3):
    #         i = i - 1
    #         arr[i][j] = value
    # if arr[i][j] == N*4-4:
    #     for value in range(N*4-3, N*5-5):
    #         j = j + 1
    #         arr[i][j] = value
    # if arr[i][j] == N*5-6:
    #     for value in range(N*5-5, N*6-8):
    #         i = i + 1
    #         arr[i][j] = value
    # if arr[i][j] == N*6-9:
    #     for value in range(N*6-8, N*7-11):
    #         j = j - 1
    #         arr[i][j] = value
    # if arr[i][j] == N*7-12:
    #     for value in range(N*7-11, N*8-15):
    #         i = i - 1
    #         arr[i][j] = value


    print(f'#{tc + 1}')
    # print(arr)
    for index in arr:
        result = ' '.join(str(i) for i in index)
        print(result)
