T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    check_arr = [[0] * 10 for _ in range(10)]   # 10 * 10 2차원 배열
    
    for idx in range(len(arr)):
        r1 = arr[idx][0]
        r2 = arr[idx][2]
        c1 = arr[idx][1]
        c2 = arr[idx][3]
        color = arr[idx][4]

        if color == 1:
            for i in range(r1, r2+1):
                for j in range(c1, c2+1):
                    check_arr[i][j] += 1
        elif color == 2:
            for i in range(r1, r2 + 1):
                for j in range(c1, c2 + 1):
                    check_arr[i][j] += 2
    cnt = 0
    for i in range(10):
        for j in range(10):
            if check_arr[i][j] ==3:
                cnt = cnt + 1

    print(f'#{tc+1} {cnt}')

