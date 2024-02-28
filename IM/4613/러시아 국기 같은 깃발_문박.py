T = int(input())
for tc in range(T):
    N, M = map(int, input().split())    # N행 M열
    board = [input() for _ in range(N)]

    max_cnt = 0
    for i in range(0, N-2):
        for j in range(i+1, N-1):
            cnt = 0
            for s in range(0, i+1):
                cnt += board[s].count('W')
            for s in range(i+1, j+1):
                cnt += board[s].count('B')
            for s in range(j+1, N):
                cnt += board[s].count('R')
            if max_cnt < cnt:
                max_cnt = cnt

    print(f'#{tc+1} {N*M-max_cnt}')
    # print(board)

