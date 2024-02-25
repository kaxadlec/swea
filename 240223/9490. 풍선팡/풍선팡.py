T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    max_result = 0
    for i in range(N):
        for j in range(M):
            mid_balloon_value = board[i][j]
            mid_balloon = i, j
            result = mid_balloon_value
            for k in range(4):
                i, j = mid_balloon
                for _ in range(mid_balloon_value):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if 0 <= ni < N and 0 <= nj < M:
                        result += board[ni][nj]
                        i, j = ni, nj
                    else:
                        continue
            if max_result < result:
                max_result = result

    print(f'#{tc+1} {max_result}')

