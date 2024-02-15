def othello(i, j, bw, board):
    stack = []
    di, dj = [-1, 1, 0, 0, -1, -1, 1, 1], [0, 0, -1, 1, -1, 1, 1, -1]   # 상하좌우, 대각선 4방향
    for k in range(8):
        ni = i + di[k]
        nj = j + dj[k]
        stack.append((ni, nj))
        while stack:
            si, sj = stack.pop()
            print('si sj', si, sj)
            if bw == 1 and i <= si < (N + 1) and j <= sj < (N + 1) and board[si][sj] != 0:
                if board[si][sj] == 2:
                    ni = si + di[k]
                    nj = sj + dj[k]
                    stack.append((ni, nj))

                elif board[ni][nj] == 1:
                    asd = stack.pop()
                    print('-------', asd)
            else:
                print("해당사항 없음")
                break
            # if bw == 2 and i <= ni < (N + 1) and j <= nj < (N + 1) and board[ni][nj] == 1:
            #     ni = ni + di[k]
            #     nj = nj + dj[k]
            #
            #     print('i, j', i, j)




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


        print('i j bw', i, j, bw)
        othello(i, j, bw, board)

        # print(board)

        for idx in board:
            result = ''.join(str(i) for i in idx)
            print(result)

    result = 0

    print(f'#{tc+1} {result}')
