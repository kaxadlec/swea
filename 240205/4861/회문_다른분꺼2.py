T = int(input())
for tc in range(1, T + 1):
    print(f'#{tc}', end=' ')
    N, M = map(int, input().split())
    board = [list(input()) for _ in range(N)]
    turned_board = list(zip(*board))
    done = False

    for row in range(N):
        for col in range(N):
            if col + M <= N:
                width_word = board[row][col:col + M]
            if row + M <= N:
                height_word = turned_board[col][row:row + M]

            if width_word == width_word[::-1]:
                print(*width_word, sep='')
                done = True
                break
            if height_word == height_word[::-1]:
                print(*height_word, sep='')
                done = True
                break

        if done:
            break