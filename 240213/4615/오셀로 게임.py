def othello(i, j, board):
    di_other, dj_other = [0, 0, -1, 1, -1, -1, 1, 1], [-1, 1, 0, 0, -1, 1, 1, -1]
    di_self, dj_self = [0, 0, -2, 2, -2, -2, 2, 2], [-2, 2, 0, 0, -2, 2, 2, -2]
    for k in range(8):
        ni_other = i + di_other[k]
        nj_other = j + dj_other[k]
        ni_self = i + di_self[k]
        nj_self = j + dj_self[k]
        if 0<=ni_self<(N+1) and 0<=nj_self<(N+1) and 0<=ni_other<(N+1) and 0<=nj_other<(N+1):
            if board[ni_other][nj_other] != 0 and board[ni_self][nj_self] != 0:
                board[ni_other][nj_other] = board[ni_self][nj_self]

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())    # 보드 한변의 길이 N, 플레이어가 돌을 놓는 횟수 M
    board = [[0]*(N+1) for _ in range(N+1)]
    start_i, start_j = int(N//2), int(N//2)
    di, dj = [0, 1, 1, 0], [0, 0, 1, 1]
    for k in range(4):
        if k % 2 == 0:
            board[start_i+di[k]][start_j+dj[k]] = 2
        else:
            board[start_i+di[k]][start_j+dj[k]] = 1
    for _ in range(M):
        j, i, bw = (input().split())  # bw 1: 흑, 2: 백
        i, j, bw = int(i), int(j), int(bw)
        board[i][j] = bw
        othello(i, j, board)

        # print(board)
        print('i j bw', i, j, bw)
        for idx in board:
            result = ''.join(str(i) for i in idx)
            print(result)


    result = 0

    print(f'#{tc+1} {result}')
