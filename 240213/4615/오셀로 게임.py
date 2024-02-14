def othello(i, j, bw, board):
    di, dj = [-1, 1, 0, 0, -1, -1, 1, 1], [0, 0, -1, 1, -1, 1, 1, -1]   # 상하좌우, 대각선 4방향
    stack = []
    for k in range(8):
        ni = i + di[k]
        nj = j + dj[k]
        while bw == 1 and i <= ni < (N + 1) and j <= nj < (N + 1) and board[ni][nj] == 2:
            stack.append((ni, nj))
            ni = ni + di[k]
            nj = nj + dj[k]


            print('stack', stack)

        while bw == 2 and i <= ni < (N + 1) and j <= nj < (N + 1) and board[ni][nj] == 1:
            ni = ni + di[k]
            nj = nj + dj[k]
            stack.append((ni, nj))
            print('i, j', i, j)
            print('ni, nj', ni, nj)
            print('stack', stack)

        if stack and bw == 1:
            ik, jk = stack.pop()
            board[ik][jk] = 1
        if stack and bw == 2:
            ik, jk = stack.pop()
            board[ik][jk] = 2


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())    # 보드 한변의 길이 N, 플레이어가 돌을 놓는 횟수 M
    board = [[0]*(N+1) for _ in range(N+1)]
    start_i, start_j = int(N//2), int(N//2)
    start_di, start_dj = [0, 1, 1, 0], [0, 0, 1, 1]
    for k in range(4):
        if k % 2 == 0:
            board[start_i+start_di[k]][start_j+start_dj[k]] = 2
        else:
            board[start_i+start_di[k]][start_j+start_dj[k]] = 1
    for _ in range(M):
        j, i, bw = (input().split())  # bw 1: 흑, 2: 백
        i, j, bw = int(i), int(j), int(bw)
        board[i][j] = bw
        othello(i, j, bw, board)

        # print(board)
        print('i j bw', i, j, bw)
        for idx in board:
            result = ''.join(str(i) for i in idx)
            print(result)

    result = 0

    print(f'#{tc+1} {result}')
