def othello(i, j, bw, board):
    stack = []
    di, dj = [-1, 1, 0, 0, -1, -1, 1, 1], [0, 0, -1, 1, -1, 1, 1, -1]   # 상하좌우, 대각선 4방향
    for k in range(8):
        ni = i + di[k]
        nj = j + dj[k]
        stack.append((ni, nj))
        while stack:
            si, sj = stack[-1]
            if bw == 1 and 1 <= si < (N + 1) and 1 <= sj < (N + 1) and board[si][sj] != 0:
                if board[si][sj] == 2:
                    ni = si + di[k]
                    nj = sj + dj[k]
                    stack.append((ni, nj))
                elif board[ni][nj] == 1:
                    stack.pop()
                    while stack:
                        temp_i, temp_j = stack.pop()
                        board[temp_i][temp_j] = 1
                    break

            elif bw == 2 and 1 <= si < (N + 1) and 1 <= sj < (N + 1) and board[si][sj] != 0:
                if board[si][sj] == 1:
                    ni = si + di[k]
                    nj = sj + dj[k]
                    stack.append((ni, nj))
                elif board[ni][nj] == 2:
                    stack.pop()
                    while stack:
                        temp_i, temp_j = stack.pop()
                        board[temp_i][temp_j] = 2
                    break

            else:
                while stack:
                    stack.pop()
                break


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())    # 보드 한변의 길이 N, 플레이어가 돌을 놓는 횟수 M
    board = [[0]*(N+1) for _ in range(N+1)]

    # 초기 바둑판 상태
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

    result_black, result_white = 0, 0
    for bo in board:
        row = ''.join(str(i) for i in bo)
        result_black += row.count('1')
        result_white += row.count('2')

    print(f'#{tc+1} {result_black} {result_white}')
