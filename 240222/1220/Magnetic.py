T = 10
for tc in range(T):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    deadlock_list = [[0]*N for _ in range(N)]
    deadlock = 0
    move = 0
    while 1:
        visited = [[0] * N for _ in range(N)]
        pre_move = move
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    if 0 <= (i + 1) < N:
                        if visited[i][j] == 0:
                            if board[i+1][j] == 2:
                                if deadlock_list[i][j] == 0:
                                    deadlock_list[i][j] = 1
                                    deadlock += 1
                                else:
                                    continue
                            elif board[i+1][j] == 1:
                                continue
                            else:
                                board[i + 1][j] = 1
                                visited[i+1][j] = 1
                                board[i][j] = 0
                                move += 1
                        else:
                            board[i][j] = 1

                    else:
                        board[i][j] = 0
                        move += 1

                elif board[i][j] == 2:
                    if 0 <= (i - 1) < N:
                        if visited[i][j] == 0:
                            if board[i-1][j] == 1:
                                if deadlock_list[i-1][j] == 0:
                                    deadlock_list[i-1][j] = 1
                                    deadlock += 1
                                else:
                                    continue
                            elif board[i-1][j] == 2:
                                continue
                            else:
                                board[i - 1][j] = 2
                                visited[i-1][j] = 1
                                board[i][j] = 0
                                move += 1
                        else:
                            board[i][j] = 2
                    else:
                        board[i][j] = 0
                        move += 1
        if move == pre_move:
            break


    print(f'#{tc + 1} {deadlock}')


