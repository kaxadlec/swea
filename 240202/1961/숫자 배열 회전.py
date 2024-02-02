T = int(input())


def rotate(arr):
    pass


for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    board = [[0]*3 for i in range(N)]
    # for j in range(N):
    #     for i in range(N):
    #         result = rotate(arr)
    #         board[i][j] = result

    print(f'#{tc+1}')
    print(board)

    for index in board:
        result = ' '.join(str(i) for i in index)
        print(result)