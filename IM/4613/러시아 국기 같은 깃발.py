def color_list(idx):
    if color
    color[idx]
T = int(input())
for tc in range(T):
    N, M = map(int, input().split())    # N개의 줄, M개의 문자
    board = [list(input()) for _ in range(N)]
    color = [0]*N
    color[0], color[-1] = 'W', 'R'
    cnt = 0
    print(board)
    for idx in range(M):    # 첫째줄, 마지막 줄 변경
        if board[0][idx] != 'W':
            board[0][idx] = 'W'
            cnt += 1

        if board[-1][idx] != 'R':
            board[-1][idx] = 'R'
            cnt += 1

    color_list(1)
    print(f'#{tc+1} {cnt}')
    print(board)
    print()
